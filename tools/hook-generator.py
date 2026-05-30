#!/usr/bin/env python3
import sys
import random

def generate_hooks(topic, audience):
    templates = [
        f"How to [Benefit] for {audience} (without [Pain Point]):",
        f"I studied 100+ {topic} examples so you don't have to.",
        f"The most underrated skill in {topic} is often ignored.",
        f"Most {audience} fail at {topic} because of this one mistake:",
        f"7 tools that will save you 10+ hours on {topic}:",
        f"Everything I know about {topic} in 5 simple steps:",
        f"Stop doing [Common Action] if you want to master {topic}.",
        f"The secret to {topic} isn't [Common Myth]. It's this:"
    ]

    return random.sample(templates, 5)

def main():
    print("--- Hook Generator ---")
    topic = input("Enter your topic (e.g., SEO, Coding, Cooking): ").strip()
    audience = input("Enter your target audience (e.g., beginners, founders): ").strip()

    if not topic or not audience:
        print("Topic and audience are required.")
        return

    print(f"\n--- Hook Ideas for {topic} targeting {audience} ---")
    hooks = generate_hooks(topic, audience)
    for i, hook in enumerate(hooks, 1):
        print(f"{i}. {hook}")

if __name__ == "__main__":
    main()
