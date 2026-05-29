#!/usr/bin/env python3
"""
X Momentum Assessor (XMF-A)
A tool to score your growth momentum using the X Momentum Framework.
"""

import sys

def get_score(pillar_name, description, levels):
    print(f"\n--- {pillar_name} ---")
    print(description)
    for i, level in enumerate(levels):
        print(f"[{i*5 + 1}-{(i+1)*5}]: {level}")

    while True:
        try:
            score = int(input(f"Enter your score for {pillar_name} (0-20): "))
            if 0 <= score <= 20:
                return score
            print("Please enter a score between 0 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_tier(total_score):
    if total_score <= 20:
        return "Starting", "Foundation not yet built. Focus on Signal Generation."
    elif total_score <= 40:
        return "Emerging", "Identifying what works. Focus on consistency and hooks."
    elif total_score <= 60:
        return "Growing", "Momentum is building. Focus on Profile Conversion."
    elif total_score <= 80:
        return "Scaling", "Systems are working. Focus on Expansion and Velocity."
    else:
        return "Dominant", "Self-sustaining flywheel. Focus on Retention and high-level strategy."

def main():
    print("Welcome to the X Momentum Assessor (XMF-A)")
    print("This tool helps you evaluate your account's growth momentum.")
    print("Answer honestly for the most accurate diagnostic.")

    pillars = [
        {
            "name": "Signal Generation",
            "desc": "The ability to generate high-value interactions (Bookmarks, Replies).",
            "levels": [
                "Most posts get views but almost no bookmarks or replies.",
                "Occasional bookmarks on 'best' posts, but mostly likes.",
                "Consistent bookmarks and at least 2-3 replies per post.",
                "Posts regularly generate 10+ bookmarks and active discussions."
            ]
        },
        {
            "name": "Algorithmic Velocity",
            "desc": "The speed of signal accumulation in the first 60 minutes.",
            "levels": [
                "Posts get engagement slowly over several days.",
                "Most engagement happens in the first 4-6 hours.",
                "Clear 'spike' of engagement in the first 60 minutes.",
                "Content often 'takes off' immediately with rapid signal accumulation."
            ]
        },
        {
            "name": "Out-of-Network Expansion",
            "desc": "Breaking out of your existing follower base into the 'For You' feed.",
            "levels": [
                "Content is only seen by existing followers.",
                "Occasional 'For You' feed appearances.",
                "30-50% of impressions come from non-followers.",
                "Viral reach; most impressions are regularly from non-followers."
            ]
        },
        {
            "name": "Profile Conversion",
            "desc": "Turning impressions into followers via your profile page.",
            "levels": [
                "High profile visits but almost no new followers.",
                "Conversion rate is around 1-2%.",
                "Conversion rate is healthy (3-5%).",
                "High-efficiency profile; >5% conversion from visit to follow."
            ]
        },
        {
            "name": "Community Retention",
            "desc": "Building a loyal 'Inner Circle' that engages consistently.",
            "levels": [
                "Followers rarely engage with new posts.",
                "A small group of 'regulars' always engage.",
                "Strong 'Inner Circle' that provides consistent initial distribution.",
                "Highly loyal community; every post starts with a massive signal boost from followers."
            ]
        }
    ]

    scores = {}
    for p in pillars:
        scores[p["name"]] = get_score(p["name"], p["desc"], p["levels"])

    total_score = sum(scores.values())
    tier, recommendation = get_tier(total_score)

    print("\n" + "="*40)
    print("X MOMENTUM SCORECARD RESULTS")
    print("="*40)
    for name, score in scores.items():
        print(f"{name:25}: {score}/20")
    print("-" * 40)
    print(f"TOTAL SCORE: {total_score}/100")
    print(f"TIER:        {tier}")
    print(f"DIAGNOSTIC:  {recommendation}")
    print("="*40)

    lowest_pillar = min(scores, key=scores.get)
    print(f"\nIMMEDIATE ACTION: Your lowest pillar is '{lowest_pillar}'.")
    print(f"Focus your next 7 days on improving {lowest_pillar} to unblock your growth.")
    print("="*40)

if __name__ == "__main__":
    main()
