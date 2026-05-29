#!/usr/bin/env python3
"""
Content Idea Generator
Generate content ideas from niche, audience, and goal.
"""

import random

def generate_ideas(niche, audience, goal):
    frameworks = [
        {
            "type": "Educational (Authority)",
            "prompts": [
                f"How {niche} actually works in 2024.",
                f"The 5 tools every {audience} needs for {niche}.",
                f"A step-by-step guide to {goal} using {niche}."
            ]
        },
        {
            "type": "Contrarian (Reach/Engagement)",
            "prompts": [
                f"Why everything you've heard about {niche} is wrong.",
                f"Stop doing [common practice] if you want to {goal}.",
                f"The truth about {niche} that most {audience} ignore."
            ]
        },
        {
            "type": "Personal/Story (Conversion/Retention)",
            "prompts": [
                f"How I went from zero to {goal} in {niche}.",
                f"The biggest mistake I made when starting in {niche}.",
                f"What 3 years of {niche} taught me about {audience}."
            ]
        }
    ]
    return frameworks

def main():
    print("X Content Idea Generator")
    niche = input("Your Niche (e.g., AI, Coding, Fitness): ")
    audience = input("Target Audience (e.g., Beginners, SaaS Founders): ")
    goal = input("Primary Goal (e.g., get more followers, make $1k/mo): ")

    print(f"\n--- Content Idea Roadmap for {niche} ---")
    frameworks = generate_ideas(niche, audience, goal)

    for f in frameworks:
        print(f"\n[{f['type']}]")
        for prompt in f['prompts']:
            print(f"- {prompt}")

    print("\nNext Action: Pick one idea and use the Hook Generator to start your draft.")

if __name__ == "__main__":
    main()
