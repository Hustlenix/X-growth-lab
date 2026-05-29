#!/usr/bin/env python3
"""
Post Analyzer
Analyze a post draft for hook strength, clarity, and engagement potential.
"""

import sys

def analyze_post(content):
    lines = content.strip().split('\n')
    if not lines:
        return "Empty content."

    hook = lines[0]
    word_count = len(content.split())

    analysis = []

    # Hook analysis
    if len(hook) > 100:
        analysis.append("- Hook is too long. Try to keep it under 80 characters for better mobile readability.")
    elif len(hook) < 20:
        analysis.append("- Hook might be too short or vague. Ensure it creates enough curiosity.")
    else:
        analysis.append("+ Hook length is optimal.")

    if any(q in hook.lower() for q in ['?', 'how', 'why', 'what']):
        analysis.append("+ Hook uses an inquiry/curiosity gap.")

    # Structure analysis
    if len(lines) == 1:
        analysis.append("- Single line post. Consider adding spacing or a thread structure for better engagement.")
    elif len(lines) > 1 and lines[1].strip() != "":
        analysis.append("- Lack of whitespace after hook. Add a line break to make it more readable.")
    else:
        analysis.append("+ Good use of whitespace.")

    # Clarity & Engagement
    if word_count > 50:
        analysis.append("- Content is getting long for a single post. If it's a deep dive, consider a thread.")

    if "?" in content[len(hook):]:
        analysis.append("+ Includes a question for engagement.")
    else:
        analysis.append("- No Call to Action (CTA) or question found in the body. Invite people to reply.")

    return analysis

def main():
    print("X Post Analyzer")
    print("Paste your post draft below (Press Ctrl+D or Ctrl+Z then Enter when finished):")

    try:
        content = sys.stdin.read()
    except EOFError:
        content = ""

    if not content.strip():
        print("Error: No content provided.")
        return

    print("\n--- Analysis Report ---")
    results = analyze_post(content)
    for res in results:
        print(res)
    print("\nKeep experimenting!")

if __name__ == "__main__":
    main()
