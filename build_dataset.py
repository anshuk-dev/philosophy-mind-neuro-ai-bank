import os
import re
import json
import glob

BASE_DIR = "/Users/anshu_macmini/Downloads/Mind_Neuro_AI_Philosophy_Question_Bank"
OUTPUT_FILE = os.path.join(BASE_DIR, "webapp_data.js")

DOMAIN_MAP = {
    "01_PHILOSOPHY_OF_MIND": "Philosophy of Mind",
    "02_NEUROPHILOSOPHY": "Neurophilosophy",
    "03_PHILOSOPHY_OF_AI": "Philosophy of AI",
    "04_EXPLANATION_AND_XAI": "Philosophy of Explanation & XAI",
    "05_AI_ETHICS_AND_GOVERNANCE": "AI Ethics & Governance",
    "06_MOCK_EXAMINATIONS": "Mock Examinations"
}

TIER_MAP = {
    "01_Basic_Foundations.md": "Tier 1: Basic / Foundational",
    "02_Moderate_Systematics.md": "Tier 2: Moderate / Systematic",
    "03_Advance_Dialectics.md": "Tier 3: Advance / Dialectical",
    "04_Conceptually_Hard_Frontiers.md": "Tier 4: Conceptually Hard / Frontiers"
}

def normalize_domain(domain_str):
    if not domain_str:
        return "Philosophy of Mind"
    d_lower = domain_str.lower()
    if "neuro" in d_lower:
        return "Neurophilosophy"
    elif "explanation" in d_lower or "xai" in d_lower or "science" in d_lower:
        return "Philosophy of Explanation & XAI"
    elif "ethics" in d_lower or "governance" in d_lower or "safety" in d_lower or "fairness" in d_lower:
        return "AI Ethics & Governance"
    elif "artificial intelligence" in d_lower or "philosophy of ai" in d_lower:
        return "Philosophy of AI"
    elif "mind" in d_lower or "cognitive" in d_lower:
        return "Philosophy of Mind"
    return domain_str.strip()

def clean_text(text):
    if not text:
        return ""
    # Strip trailing markdown horizontal rules and whitespace
    text = re.sub(r'\n*---+\s*$', '', text.strip())
    text = re.sub(r'\s*---+\s*$', '', text)
    return text.strip()

def parse_markdown_file(filepath):
    rel_path = os.path.relpath(filepath, BASE_DIR)
    parts = rel_path.split(os.sep)
    domain_folder = parts[0]
    filename = parts[1]
    
    is_mock = "MOCK" in domain_folder or "Mock" in filename
    domain_name = DOMAIN_MAP.get(domain_folder, domain_folder)
    default_tier = TIER_MAP.get(filename, "Tier 2: Moderate / Systematic")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by questions: ### Question
    raw_questions = re.split(r'\n(?=### Question\s*\d+:)', content)
    questions = []

    for idx, raw_q in enumerate(raw_questions):
        if not raw_q.strip().startswith("### Question"):
            continue

        lines = raw_q.strip().split("\n")
        title_line = lines[0]
        title_match = re.search(r'### Question\s*\d+:\s*(.*)', title_line)
        title = title_match.group(1).strip() if title_match else f"Question {idx+1}"

        rest = "\n".join(lines[1:])

        # Extract tier if specified in text
        tier_match = re.search(r'\*\*Difficulty Tier\*\*:\s*([^\n]+)', rest)
        if tier_match:
            tier_raw = tier_match.group(1).strip()
            if "Basic" in tier_raw:
                tier = "Tier 1: Basic / Foundational"
            elif "Moderate" in tier_raw:
                tier = "Tier 2: Moderate / Systematic"
            elif "Advance" in tier_raw or "Dialectical" in tier_raw:
                tier = "Tier 3: Advance / Dialectical"
            elif "Hard" in tier_raw or "Frontier" in tier_raw:
                tier = "Tier 4: Conceptually Hard / Frontiers"
            else:
                tier = tier_raw
        else:
            tier = default_tier

        # Extract thinkers
        thinkers_match = re.search(r'\*\*Primary Thinkers?\*\*:\s*([^\n]+)', rest)
        thinkers = thinkers_match.group(1).strip() if thinkers_match else ""

        # Extract domain if explicitly given (e.g. in mock exams)
        domain_match = re.search(r'\*\*Domain\*\*:\s*([^\n]+)', rest)
        if domain_match:
            raw_domain = domain_match.group(1).strip()
            q_domain = normalize_domain(raw_domain)
        else:
            q_domain = normalize_domain(domain_name)

        # Extract correct answer
        ans_match = re.search(r'\*\*Correct Answer\*\*:\s*\**\(?([A-D])\)?\**', rest)
        correct_option = ans_match.group(1).strip() if ans_match else "A"

        # Split into Options
        opt_pattern = r'\n-\s*\(([A-D])\)\s*([\s\S]*?)(?=\n-\s*\([A-D]\)|\n\*\*Correct Answer\*\*|\n####|\Z)'
        opts_found = re.findall(opt_pattern, rest)
        options = {}
        for opt_letter, opt_body in opts_found:
            options[opt_letter] = clean_text(opt_body)

        # Question prompt
        prompt_match = re.search(r'(?:### Question[^\n]*\n)([\s\S]*?)(?=\n-\s*\(A\))', raw_q)
        if prompt_match:
            prompt_block = prompt_match.group(1).strip()
            prompt_clean_lines = []
            for pline in prompt_block.split("\n"):
                if pline.startswith("**Format**:") or pline.startswith("**Difficulty Tier**:") or pline.startswith("**Primary Thinkers**:") or pline.startswith("**Domain**:") or pline.startswith("---"):
                    continue
                prompt_clean_lines.append(pline)
            question_text = "\n".join(prompt_clean_lines).strip()
        else:
            question_text = "See question options and grounding."

        # Grounding
        grounding_match = re.search(r'#### Philosophical Grounding & Demonstration:?([\s\S]*?)(?=#### Distractor Analysis|\*\*Primary Textual Reference\*\*|\n---|\Z)', rest)
        grounding = grounding_match.group(1).strip() if grounding_match else ""

        # Distractor Analysis
        distractor_match = re.search(r'#### Distractor Analysis:?([\s\S]*?)(?=\*\*Primary Textual Reference\*\*|\n---|\Z)', rest)
        distractor_analysis = distractor_match.group(1).strip() if distractor_match else ""

        # If grounding was not in a separate section (e.g. in mock exams), extract the correct diagnosis as grounding
        if not grounding and distractor_analysis:
            corr_bullet_match = re.search(r'-\s*\*\*\(?[A-D]\)?\s*is\s*correct\*\*:\s*([\s\S]*?)(?=\n-\s*\*\*\(?[A-D]\)?\s*is\s*incorrect|\Z)', distractor_analysis)
            if corr_bullet_match:
                grounding = corr_bullet_match.group(1).strip()
            else:
                grounding = distractor_analysis

        # Primary Textual Reference
        ref_match = re.search(r'\*\*Primary Textual Reference\*\*:\s*([^\n]+)', rest)
        reference = ref_match.group(1).strip() if ref_match else ""

        q_id = f"{filename}_{idx+1}"

        questions.append({
            "id": q_id,
            "filename": filename,
            "folder": domain_folder,
            "is_mock": is_mock,
            "domain": q_domain,
            "tier": tier,
            "title": title,
            "thinkers": thinkers,
            "question": clean_text(question_text),
            "options": options,
            "correct_option": correct_option,
            "grounding": clean_text(grounding),
            "distractor_analysis": clean_text(distractor_analysis),
            "reference": clean_text(reference)
        })

    return questions

def main():
    all_files = glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True)
    all_questions = []

    for fpath in sorted(all_files):
        if "00_CURRICULUM_AND_BLUEPRINT" in fpath or "README.md" in fpath or "MASTER_INDEX.md" in fpath:
            continue
        qs = parse_markdown_file(fpath)
        all_questions.extend(qs)

    domains = {}
    tiers = {}
    mock_count = 0
    topicwise_count = 0
    for q in all_questions:
        d = q["domain"]
        t = q["tier"]
        domains[d] = domains.get(d, 0) + 1
        tiers[t] = tiers.get(t, 0) + 1
        if q["is_mock"]:
            mock_count += 1
        else:
            topicwise_count += 1

    stats = {
        "total_questions": len(all_questions),
        "topicwise_count": topicwise_count,
        "mock_count": mock_count,
        "domains": domains,
        "tiers": tiers
    }

    data = {
        "stats": stats,
        "questions": all_questions
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("window.MIND_AI_DATA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

    print(f"Successfully wrote data to {OUTPUT_FILE}")
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
