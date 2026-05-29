# 🛠 X Growth Lab: Tooling Layer

## Introduction
The Tooling Layer turns the X Growth Lab from a learning resource into an executable toolkit. These tools are designed to run locally on your machine, helping you analyze, build, and optimize your X content strategy.

## Installation
All tools are written in Python and use the standard library, meaning no external dependencies are required.

1.  Ensure you have Python 3.6+ installed.
2.  Clone this repository.
3.  Navigate to the `tools/` directory.

```bash
cd tools/
```

## Tools Overview

### 1. X Momentum Assessor (`x-momentum-assessor.py`)
The flagship tool of the lab. It implements the **X Momentum Framework** to diagnose your account's health.
- **Usage:** `python3 x-momentum-assessor.py`
- **Output:** A total score (0-100), your momentum tier, and a specific recommendation on which pillar to focus on next.

### 2. Post Analyzer (`post-analyzer.py`)
Analyze your post drafts before you hit publish.
- **Usage:** `python3 post-analyzer.py`
- **Output:** Feedback on hook strength, formatting, and engagement potential.

### 3. Hook Generator (`hook-generator.py`)
Never stare at a blank screen again. Generate high-conversion hook ideas based on your topic.
- **Usage:** `python3 hook-generator.py`
- **Output:** 8+ hook templates customized for your audience and niche.

### 4. Engagement Score Estimator (`engagement-score.py`)
Understand how the algorithm weights your interactions.
- **Usage:** `python3 engagement-score.py`
- **Output:** A weighted engagement score and potential for algorithmic amplification.

### 5. Thread Builder (`thread-builder.py`)
Turn complex topics into readable, high-engagement threads.
- **Usage:** `python3 thread-builder.py`
- **Output:** A structured thread outline including hook, body, and CTA.

### 6. Content Idea Generator (`content-idea-generator.py`)
Generate a week's worth of content ideas in seconds.
- **Usage:** `python3 content-idea-generator.py`
- **Output:** Prompts for Educational, Contrarian, and Personal posts.

## Relation to Other Layers
- **Frameworks:** The `x-momentum-assessor.py` is powered by the [X Momentum Framework](../docs/x-momentum-framework.md).
- **Templates:** Use the outputs of `thread-builder.py` with our [Content Templates](../templates/).
- **Datasets:** Coming soon! Future tools will use [Datasets](../datasets/) to provide even more accurate benchmarks.

---

### 💡 Pro Tip
Run the `x-momentum-assessor.py` once a week to track your progress and adjust your strategy based on real data.
