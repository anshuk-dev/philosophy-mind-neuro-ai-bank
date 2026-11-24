import os
import glob
import re
import random
import json
from collections import Counter

BASE_DIR = "/Users/anshu_macmini/Downloads/Mind_Neuro_AI_Philosophy_Question_Bank"

def shuffle_question_text(q_text, target_ans, rng):
    # 1. Extract options
    opt_pattern = r'\n-\s*\(([A-D])\)\s*([\s\S]*?)(?=\n-\s*\([A-D]\)|\n\*\*Correct Answer\*\*|\n####|\Z)'
    opts_found = re.findall(opt_pattern, q_text)
    if len(opts_found) != 4:
        raise ValueError(f"Expected 4 options, found {len(opts_found)}")
    
    old_opts = {letter: body.strip() for letter, body in opts_found}
    
    # Target permutation: old 'A' goes to target_ans
    rem_slots = [l for l in ['A', 'B', 'C', 'D'] if l != target_ans]
    rng.shuffle(rem_slots)
    
    perm = {
        'A': target_ans,
        'B': rem_slots[0],
        'C': rem_slots[1],
        'D': rem_slots[2]
    }
    
    new_opts = {perm[old_l]: body for old_l, body in old_opts.items()}
    new_opts_str = '\n' + '\n'.join([f"- ({l}) {new_opts[l]}" for l in ['A', 'B', 'C', 'D']])
    
    # Replace options block in q_text
    opts_start = re.search(r'\n-\s*\(A\)', q_text).start()
    ans_start = re.search(r'\n\*\*Correct Answer\*\*:', q_text).start()
    
    q_text = q_text[:opts_start] + new_opts_str + '\n\n' + q_text[ans_start+1:]
    
    # Update Correct Answer
    q_text = re.sub(r'\*\*Correct Answer\*\*:\s*\**\(?[A-D]\)?\**', f'**Correct Answer**: **({target_ans})**', q_text, count=1)
    
    # Update Distractor Analysis
    dm = re.search(r'(#### Distractor Analysis:?)([\s\S]*?)(?=\*\*Primary Textual Reference\*\*|\n---|\Z)', q_text)
    if not dm:
        raise ValueError("Distractor analysis not found")
    
    d_header = dm.group(1)
    d_content = dm.group(2).strip()
    
    # Check for multi-letter bullet: e.g. (B), (C), and (D) are incorrect
    multi_m = re.search(r'^[ \t]*-[ \t]*\*\*\(?([A-D])\)?,?\s*\(?([A-D])\)?,?\s*and\s*\(?([A-D])\)?\s+are\s+incorrect\*\*:\s*([\s\S]*?)(?=^[ \t]*-[ \t]*\*\*|\Z)', d_content, re.MULTILINE)
    if multi_m:
        other_l = sorted([l for l in ['A', 'B', 'C', 'D'] if l != target_ans])
        body = multi_m.group(4).strip()
        new_bullets_str = f"- **({other_l[0]}), ({other_l[1]}), and ({other_l[2]}) are incorrect**: {body}"
    else:
        # Single bullets
        b_matches = list(re.finditer(r'^[ \t]*-[ \t]*\*\*\(([A-D])\)\s+(is\s+(?:incorrect|correct|false))\*\*:\s*([\s\S]*?)(?=^[ \t]*-[ \t]*\*\*|\Z)', d_content, re.MULTILINE))
        if not b_matches:
            raise ValueError(f"No bullets parsed in distractor analysis: {d_content[:100]}")
        
        updated_bullets = []
        for m in b_matches:
            old_l = m.group(1)
            status_str = m.group(2)
            body = m.group(3).strip()
            new_l = perm[old_l]
            updated_bullets.append((new_l, f"- **({new_l}) {status_str}**: {body}"))
        
        # Sort bullets alphabetically by new letter
        updated_bullets.sort(key=lambda x: x[0])
        new_bullets_str = '\n'.join([b[1] for b in updated_bullets])
    
    prefix = q_text[:dm.start(2)]
    suffix = q_text[dm.end(2):]
    q_text = prefix + '\n' + new_bullets_str + '\n\n' + suffix.lstrip('\n')
    
    return q_text, perm

def main():
    rng = random.Random(2026)
    
    all_files = sorted(glob.glob(os.path.join(BASE_DIR, "*", "*.md")))
    md_files = [f for f in all_files if "00_CURRICULUM" not in f and "README.md" not in f and "MASTER_INDEX.md" not in f]
    
    # 1. Read files and count questions
    file_questions = []
    file_counts = []
    
    for fpath in md_files:
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()
        qs = [q for q in re.split(r'\n(?=### Question\s*\d+:)', content) if q.strip().startswith("### Question")]
        file_questions.append((fpath, content, qs))
        file_counts.append(len(qs))
        
    total_q = sum(file_counts)
    print(f"Total questions to randomize across {len(md_files)} files: {total_q}")
    assert total_q == 304, f"Expected 304 questions, found {total_q}"
    
    # 2. Balanced distribution: exactly 76 of each letter
    remaining_needed = Counter({'A': 76, 'B': 76, 'C': 76, 'D': 76})
    file_allocations = []
    
    for k in file_counts:
        base = k // 4
        alloc = {'A': base, 'B': base, 'C': base, 'D': base}
        for l in 'ABCD':
            remaining_needed[l] -= base
        file_allocations.append(alloc)
        
    rem_slots_per_file = [k % 4 for k in file_counts]
    rem_letters = []
    for l, cnt in remaining_needed.items():
        rem_letters.extend([l] * cnt)
    rng.shuffle(rem_letters)
    
    idx = 0
    for i, rem_cnt in enumerate(rem_slots_per_file):
        for _ in range(rem_cnt):
            l = rem_letters[idx]
            file_allocations[i][l] += 1
            idx += 1
            
    # 3. Generate sequences with max streak <= 2
    file_sequences = []
    for alloc in file_allocations:
        letters = []
        for l, cnt in alloc.items():
            letters.extend([l] * cnt)
        
        for _ in range(5000):
            rng.shuffle(letters)
            streak = 1
            valid = True
            for j in range(1, len(letters)):
                if letters[j] == letters[j-1]:
                    streak += 1
                    if streak > 2:
                        valid = False
                        break
                else:
                    streak = 1
            if valid:
                break
        file_sequences.append(letters)
        
    all_flattened = [l for seq in file_sequences for l in seq]
    print(f"Global target answer distribution: {Counter(all_flattened)}")
    assert Counter(all_flattened) == {'A': 76, 'B': 76, 'C': 76, 'D': 76}
    
    # 4. Modify files
    for (fpath, full_content, qs), target_seq in zip(file_questions, file_sequences):
        header = re.split(r'\n(?=### Question\s*\d+:)', full_content)[0]
        new_qs = []
        
        for q_text, target_ans in zip(qs, target_seq):
            new_q, perm = shuffle_question_text(q_text, target_ans, rng)
            new_qs.append(new_q)
            
        new_file_content = header + '\n' + '\n'.join(new_qs)
        # Ensure trailing newline
        if not new_file_content.endswith('\n'):
            new_file_content += '\n'
            
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(new_file_content)
            
        rel_path = os.path.relpath(fpath, BASE_DIR)
        print(f"Updated {rel_path}: {Counter(target_seq)}")
        
    print("\nAll markdown files successfully updated!")

if __name__ == "__main__":
    main()
