"""
Verification Suite for ESPAÑOL 60-Day Handbook
"""
import os
import re
import json

def verify():
    base_dir = "d:/ag/espanol-handbook"
    print("=== STARTING ESPAÑOL HANDBOOK VERIFICATION ===")

    # 1. Check all essential files exist
    required_files = [
        "index.html",
        "css/styles.css",
        "js/app.js",
        "data/getting-started.js",
        "data/lessons/stage1.js",
        "data/lessons/stage2.js",
        "data/lessons/stage3.js",
        "data/lessons/stage4.js",
        "data/lessons/stage5.js",
        "data/lessons/stage6.js",
        "data/milestones.js",
        "data/grammar-reference.js",
        "data/vocabulary-index.js",
        "data/final-exam.js"
    ]

    for rf in required_files:
        p = os.path.join(base_dir, rf)
        assert os.path.exists(p), f"Missing file: {rf}"
        sz = os.path.getsize(p)
        print(f"✓ File exists: {rf} ({sz:,} bytes)")

    # 2. Check all 60 days
    all_days = []
    required_sections = [
        "day", "stage", "title", "subtitle", "goals", "bengaliNote",
        "vocabulary", "sentences", "grammar", "conversation",
        "reading", "exercises", "speakingChallenge", "dailyRevision", "checklist"
    ]

    total_vocab_count = 0

    for stage_idx in range(1, 7):
        p = os.path.join(base_dir, f"data/lessons/stage{stage_idx}.js")
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        json_str = re.sub(r"^[^{[]*", "", content)
        json_str = re.sub(r";\s*$", "", json_str)
        lessons = json.loads(json_str)
        print(f"\n--- Checking Stage {stage_idx}: {len(lessons)} lessons found ---")
        assert len(lessons) == 10, f"Stage {stage_idx} does not have exactly 10 lessons (found {len(lessons)})"

        for l in lessons:
            day_num = l["day"]
            all_days.append(day_num)
            for sec in required_sections:
                assert sec in l, f"Day {day_num} missing section '{sec}'"
            
            vocab_len = len(l["vocabulary"])
            total_vocab_count += vocab_len
            assert vocab_len >= 10, f"Day {day_num} has fewer than 10 vocabulary words ({vocab_len})"
            assert len(l["sentences"]) >= 5, f"Day {day_num} has fewer than 5 sentences ({len(l['sentences'])})"
            assert len(l["goals"]) >= 3, f"Day {day_num} has fewer than 3 goals ({len(l['goals'])})"
            assert len(l["checklist"]) >= 5, f"Day {day_num} has fewer than 5 checklist items ({len(l['checklist'])})"
            assert "questions" in l["reading"], f"Day {day_num} reading missing questions"

    assert len(all_days) == 60, f"Expected 60 total days, got {len(all_days)}"
    assert sorted(all_days) == list(range(1, 61)), "Days are not strictly 1 to 60 sequential"
    print(f"\n✓ All 60 Days verified with complete 10-part templates! Total vocabulary words: {total_vocab_count}")

    # 3. Check Vocabulary Index
    p_vocab = os.path.join(base_dir, "data/vocabulary-index.js")
    with open(p_vocab, "r", encoding="utf-8") as f:
        c = f.read()
    j_str = re.sub(r"^[^{[]*", "", c)
    j_str = re.sub(r";\s*$", "", j_str)
    vocab_idx = json.loads(j_str)
    print(f"✓ Vocabulary Index verified: {len(vocab_idx)} words indexed.")
    assert len(vocab_idx) == 600, f"Expected 600 vocabulary words, found {len(vocab_idx)}"

    # 4. Check Final Exam & Certificate
    p_exam = os.path.join(base_dir, "data/final-exam.js")
    with open(p_exam, "r", encoding="utf-8") as f:
        c = f.read()
    j_str = re.sub(r"^[^{[]*", "", c)
    j_str = re.sub(r";\s*$", "", j_str)
    exam_data = json.loads(j_str)
    assert exam_data["student"]["name"] == "Sakib Ahmed"
    assert exam_data["totalPoints"] == 100
    assert "certificate" in exam_data
    assert exam_data["certificate"]["recipient"] == "Sakib Ahmed"
    print(f"✓ Final Exam & Official Certificate for {exam_data['student']['name']} verified!")

    # 5. Check Milestones
    p_miles = os.path.join(base_dir, "data/milestones.js")
    with open(p_miles, "r", encoding="utf-8") as f:
        c = f.read()
    j_str = re.sub(r"^[^{[]*", "", c)
    j_str = re.sub(r";\s*$", "", j_str)
    miles_data = json.loads(j_str)
    assert len(miles_data) == 6
    print(f"✓ All 6 Milestones verified!")

    # 6. Check Grammar Reference
    p_gram = os.path.join(base_dir, "data/grammar-reference.js")
    with open(p_gram, "r", encoding="utf-8") as f:
        c = f.read()
    j_str = re.sub(r"^[^{[]*", "", c)
    j_str = re.sub(r";\s*$", "", j_str)
    gram_data = json.loads(j_str)
    assert len(gram_data) >= 10
    print(f"✓ Grammar Reference verified: {len(gram_data)} chapters.")

    print("\n🎉 ALL AUDITS PASSED WITH ZERO ERRORS! 100% PRODUCTION READY! 🎉")

if __name__ == "__main__":
    verify()
