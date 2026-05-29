#!/usr/bin/env python3
import sys

def main():
    print("--- Thread Builder ---")
    topic = input("Thread Topic: ").strip()
    main_points = input("Enter 3-5 main points (comma separated): ").split(",")
    cta = input("What is the final Call to Action? (e.g., Follow, Newsletter): ").strip()

    if not topic or not main_points:
        print("Topic and main points are required.")
        return

    print("\n--- Generated Thread Structure ---\n")
    print(f"Post 1 (The Hook):\n[Insert strong hook about {topic}]\n\nHere's the breakdown:\n")

    for i, point in enumerate(main_points, 1):
        print(f"Post {i+1} (Point {i}):\n- {point.strip()}\n- [Add detail or example]\n- [Add a practical takeaway]\n")

    print(f"Post {len(main_points)+2} (Summary):\nQuick recap:\n" + "\n".join([f"- {p.strip()}" for p in main_points]))
    print(f"\nPost {len(main_points)+3} (CTA):\nIf you found this helpful:\n1. Follow @[YourHandle] for more on {topic}.\n2. RT the first post to help others.\n\nCTA: {cta}")

if __name__ == "__main__":
    main()
