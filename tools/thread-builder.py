#!/usr/bin/env python3
"""
Thread Builder
Turn a topic into a structured thread outline.
"""

def build_thread(topic, key_points):
    thread = []
    # Hook
    thread.append(f"1/ [HOOK]: The secret to mastering {topic} in 2024.\n\nMost people think it's about [common myth].\nBut the reality is much simpler.\n\nHere is the {len(key_points)}-step framework: 🧵")

    # Body
    for i, point in enumerate(key_points, 2):
        thread.append(f"{i}/ {point}\n\n[Explain why this matters or how to implement it].")

    # Closing
    final_count = len(key_points) + 2
    thread.append(f"{final_count}/ TL;DR on {topic}:\n\n" + "\n".join([f"- {p}" for p in key_points]))

    thread.append(f"{final_count + 1}/ If you found this useful:\n\n1. Follow me @[Handle] for more on {topic}.\n2. RT the first tweet to share the value with others.\n\nThanks for reading! 🫡")

    return thread

def main():
    print("X Thread Builder")
    topic = input("What is the main topic of your thread? ")
    points_input = input("Enter your key points (separated by commas): ")
    key_points = [p.strip() for p in points_input.split(',') if p.strip()]

    if not key_points:
        print("Please provide at least one key point.")
        return

    print(f"\n--- Your {topic} Thread Outline ---")
    thread = build_thread(topic, key_points)
    for tweet in thread:
        print("-" * 20)
        print(tweet)
    print("-" * 20)
    print("\nTip: Refine each tweet to be under 280 characters and add relevant emojis.")

if __name__ == "__main__":
    main()
