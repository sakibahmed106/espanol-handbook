"""
Vocabulary Index Builder for ESPAÑOL 60-Day Handbook
Parses all 6 stages and creates data/vocabulary-index.js with ~600 words
"""
import json
import re

all_words = []
stage_files = [
    ("Stage 1", "d:/ag/espanol-handbook/data/lessons/stage1.js"),
    ("Stage 2", "d:/ag/espanol-handbook/data/lessons/stage2.js"),
    ("Stage 3", "d:/ag/espanol-handbook/data/lessons/stage3.js"),
    ("Stage 4", "d:/ag/espanol-handbook/data/lessons/stage4.js"),
    ("Stage 5", "d:/ag/espanol-handbook/data/lessons/stage5.js"),
    ("Stage 6", "d:/ag/espanol-handbook/data/lessons/stage6.js")
]

for stage_name, filepath in stage_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip window.STAGE_X_LESSONS = ... ;
    json_str = re.sub(r"^[^{[]*", "", content)
    json_str = re.sub(r";\s*$", "", json_str)
    lessons = json.loads(json_str)
    
    for lesson in lessons:
        day_num = lesson.get("day")
        lesson_title = lesson.get("title")
        for v in lesson.get("vocabulary", []):
            entry = {
                "word": v.get("word"),
                "translation": v.get("translation"),
                "pos": v.get("pos", "noun"),
                "gender": v.get("gender"),
                "example": v.get("example"),
                "exampleTranslation": v.get("exampleTranslation"),
                "day": day_num,
                "stage": lesson.get("stage"),
                "lessonTitle": lesson_title
            }
            all_words.append(entry)

# Sort words alphabetically by Spanish word (ignoring punctuation/articles)
def clean_sort_key(item):
    w = item["word"].lower()
    w = re.sub(r"^(el|la|los|las|un|una|unos|unas|¡|¿)\s+", "", w)
    w = w.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "nz")
    return w

all_words.sort(key=clean_sort_key)

# Add unique ID to each
for idx, item in enumerate(all_words):
    item["id"] = f"vocab-{idx+1:03d}"

print(f"Extracted and indexed {len(all_words)} total vocabulary items across all 60 days!")

# Save to data/vocabulary-index.js
with open("d:/ag/espanol-handbook/data/vocabulary-index.js", "w", encoding="utf-8") as f:
    f.write("// Complete 600-Word A-Z Alphabetical Vocabulary Index\n")
    f.write("window.HANDBOOK_VOCABULARY_INDEX = ")
    json.dump(all_words, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Saved data/vocabulary-index.js successfully.")
