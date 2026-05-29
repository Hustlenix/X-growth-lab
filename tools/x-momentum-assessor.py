#!/usr/bin/env python3
import sys

def get_input(prompt, min_val=0, max_val=20):
    while True:
        try:
            val = int(input(f"{prompt} ({min_val}-{max_val}): "))
            if min_val <= val <= max_val:
                return val
            print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("--- X Momentum Assessor ---")
    print("Score each pillar based on your recent performance (0-20).\n")

    pillars = [
        "Signal Generation (Bookmarks, Replies)",
        "Algorithmic Velocity (Initial Engagement Spike)",
        "Out-of-Network Expansion (Non-follower Reach)",
        "Profile Conversion (Visit to Follow Ratio)",
        "Community Retention (Follower Loyalty)"
    ]

    scores = []
    for pillar in pillars:
        scores.append(get_input(pillar))

    total_score = sum(scores)

    print("\n--- Results ---")
    print(f"Total Momentum Score: {total_score}/100")

    if total_score <= 20:
        tier = "Starting"
        advice = "Foundation not yet built. Focus on Signal Generation - make your content more bookmarkable."
    elif total_score <= 40:
        tier = "Emerging"
        advice = "Identifying what works. Focus on consistency and stronger hooks to improve Velocity."
    elif total_score <= 60:
        tier = "Growing"
        advice = "Momentum is building. Focus on Profile Conversion - optimize your bio and pinned post."
    elif total_score <= 80:
        tier = "Scaling"
        advice = "Systems are working. Focus on Expansion and Velocity - experiment with broader topics."
    else:
        tier = "Dominant"
        advice = "Self-sustaining flywheel. Focus on Retention and high-level community strategy."

    print(f"Tier: {tier}")
    print(f"Recommendation: {advice}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
