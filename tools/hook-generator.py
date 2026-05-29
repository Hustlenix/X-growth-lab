#!/usr/bin/env python3
"""
Hook Generator
Generate hook ideas based on topic, audience, and tone.
"""

def generate_hooks(topic, audience):
    templates = [
        f"How to [achieve result] in [time] (without [common pain point]).",
        f"I studied {topic} for 100+ hours so you don't have to. Here's what I found:",
        f"Most {audience} fail at {topic} because of this one mistake:",
        f"Unpopular opinion: {topic} is overrated. Here's why:",
        f"Stop scrolling. If you're a {audience} interested in {topic}, read this:",
        f"The secret to mastering {topic} isn't what you think.",
        f"If you want to [goal] in 2024, you need to understand {topic}.",
        f"7 tools that will save you 10+ hours on {topic}:"
    ]
    return templates

def main():
    print("X Hook Generator")
    topic = input("Enter your topic (e.g., Python, Solopreneurship): ")
    audience = input("Enter your target audience (e.g., Beginners, Developers): ")

    print(f"\n--- Hook Ideas for {topic} targeting {audience} ---")
    hooks = generate_hooks(topic, audience)
    for i, hook in enumerate(hooks, 1):
        print(f"{i}. {hook}")

    print("\nTip: Choose the one that best fits your content's core value.")

if __name__ == "__main__":
    main()
