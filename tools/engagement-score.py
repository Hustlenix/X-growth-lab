#!/usr/bin/env python3
"""
Engagement Score Estimator
Estimate engagement potential using simple heuristic scoring.
"""

def estimate_score(stats):
    # Simplified heuristic based on X Algorithm principles
    # High weight: Bookmarks, Replies
    # Medium weight: Reposts
    # Low weight: Likes

    score = (stats['bookmarks'] * 10) + (stats['replies'] * 5) + (stats['reposts'] * 3) + (stats['likes'] * 1)

    # Contextual multiplier (e.g., if views are known)
    if stats.get('views', 0) > 0:
        engagement_rate = (stats['bookmarks'] + stats['replies'] + stats['reposts'] + stats['likes']) / stats['views']
        return score, engagement_rate * 100

    return score, None

def main():
    print("Engagement Score Estimator")
    print("Enter the stats for your post:")

    try:
        stats = {
            'likes': int(input("Likes: ") or 0),
            'reposts': int(input("Reposts: ") or 0),
            'replies': int(input("Replies: ") or 0),
            'bookmarks': int(input("Bookmarks: ") or 0),
            'views': int(input("Views (optional, press Enter to skip): ") or 0)
        }
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    score, rate = estimate_score(stats)

    print("\n--- Engagement Report ---")
    print(f"Weighted Engagement Score: {score}")
    if rate is not None:
        print(f"Engagement Rate: {rate:.2f}%")
        if rate > 2:
            print("Status: High Engagement Potential! The algorithm is likely to amplify this.")
        elif rate > 0.5:
            print("Status: Healthy Engagement.")
        else:
            print("Status: Low Engagement. Try improving the hook or value proposition.")
    else:
        print("Tip: Use views to calculate your engagement rate for better insights.")

    print("\nRemember: Bookmarks are currently the strongest signal for the Heavy Ranker.")

if __name__ == "__main__":
    main()
