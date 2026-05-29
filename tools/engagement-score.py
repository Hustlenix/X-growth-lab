#!/usr/bin/env python3
import sys

def calculate_score():
    print("--- Engagement Score Estimator ---")
    print("Answer these questions to estimate your post's potential (0-10 scale).\n")

    questions = [
        ("Novelty: Is this a fresh take or new information?", 1.5),
        ("Utility: Can the reader use this immediately?", 2.0),
        ("Relatability: Will people say 'that's so me'?", 1.2),
        ("Authority: Do you sound like an expert on this?", 1.0),
        ("Visual Clarity: Is it easy to skim?", 1.3),
        ("Controversy/Opinion: Does it spark a debate?", 1.0)
    ]

    total_weighted_score = 0
    max_possible = sum(q[1] * 10 for q in questions)

    for q, weight in questions:
        while True:
            try:
                val = float(input(f"{q} (0-10): "))
                if 0 <= val <= 10:
                    total_weighted_score += val * weight
                    break
                print("Please enter a value between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    final_score = (total_weighted_score / max_possible) * 100

    print(f"\nEstimated Engagement Potential: {final_score:.1f}/100")

    if final_score < 40:
        print("Verdict: Low Signal. Needs more value or a better hook.")
    elif final_score < 70:
        print("Verdict: Solid. Likely to perform well with your existing network.")
    else:
        print("Verdict: High Signal! Strong potential for out-of-network expansion.")

if __name__ == "__main__":
    try:
        calculate_score()
    except KeyboardInterrupt:
        print("\nExiting...")
