#!/usr/bin/env python3
import random

def main():
    print("--- Content Idea Generator ---")
    niche = input("What is your niche? (e.g., SaaS, Personal Finance): ").strip()
    audience = input("Who is your target audience? (e.g., Solo founders, Students): ").strip()
    goal = input("Goal? (e.g., Build authority, Get newsletter signups): ").strip()

    frameworks = [
        {"name": "The contrarian take", "desc": "Identify a common belief in {niche} and explain why it's wrong for {audience}."},
        {"name": "The curated list", "desc": "Top 10 tools/resources that help {audience} achieve {goal}."},
        {"name": "The personal story", "desc": "How I went from [Problem] to [Result] in {niche} (and how {audience} can too)."},
        {"name": "The detailed 'How-to'", "desc": "A step-by-step guide for {audience} to master [Specific Skill] in {niche}."},
        {"name": "The 'What I learned'", "desc": "3 lessons from studying [Successful Person/Company] in {niche}."},
        {"name": "The system reveal", "desc": "The exact workflow I use for {niche} to reach {goal}."}
    ]

    print(f"\n--- Idea Prompts for {niche} ---")
    selected = random.sample(frameworks, 3)
    for i, framework in enumerate(selected, 1):
        prompt = framework["desc"].format(niche=niche, audience=audience, goal=goal)
        print(f"{i}. [{framework['name']}]\n   {prompt}\n")

if __name__ == "__main__":
    main()
