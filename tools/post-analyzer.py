#!/usr/bin/env python3
import sys

def analyze_post(post):
    length = len(post)
    words = post.split()
    word_count = len(words)

    # Simple heuristics
    has_question = "?" in post
    has_numbers = any(char.isdigit() for char in post)
    has_list = post.count("\n-") > 1 or post.count("\n*") > 1 or post.count("\n1.") > 0
    line_breaks = post.count("\n")

    print("\n--- Analysis Results ---")

    # Hook Strength
    first_line = post.split("\n")[0] if post else ""
    hook_score = 0
    if len(first_line) > 10 and len(first_line) < 80: hook_score += 40
    if "?" in first_line: hook_score += 20
    if any(char.isdigit() for char in first_line): hook_score += 20
    if len(first_line.split()) < 12: hook_score += 20

    print(f"Hook Strength: {hook_score}/100")

    # Clarity & Structure
    structure_score = min(100, (line_breaks * 20) + (20 if has_list else 0))
    print(f"Structure Score: {structure_score}/100")

    # Engagement Potential
    engagement_potential = 0
    if has_question: engagement_potential += 30
    if has_numbers: engagement_potential += 20
    if word_count > 10 and word_count < 50: engagement_potential += 30
    if line_breaks >= 2: engagement_potential += 20

    print(f"Engagement Potential: {engagement_potential}/100")

    print("\n--- Suggested Improvements ---")
    if hook_score < 60:
        print("- Make your first line punchier. Aim for < 12 words.")
    if structure_score < 50:
        print("- Add more white space and line breaks for readability.")
    if not has_question:
        print("- Consider adding a question to spark replies.")
    if not has_numbers:
        print("- Numbers or statistics often increase bookmark rates.")

def main():
    print("--- Post Analyzer ---")
    print("Paste your post draft below (Press Ctrl+D or Ctrl+Z then Enter to finish):")

    try:
        post = sys.stdin.read().strip()
    except EOFError:
        post = ""

    if not post:
        print("No post content provided.")
        return

    analyze_post(post)

if __name__ == "__main__":
    main()
