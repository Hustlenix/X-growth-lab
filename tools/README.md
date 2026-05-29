# 🛠 X Growth Lab Toolkit

Welcome to the tools layer of the X Growth Lab. This directory contains practical, local-first Python scripts designed to help you analyze, generate, and optimize your content on X.

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher installed on your machine.

### Installation
1. Clone the repository (if you haven't already).
2. Navigate to the `tools/` directory.
3. (Optional) Create a virtual environment: `python -m venv venv && source venv/bin/activate`
4. Install requirements: `pip install -r ../requirements.txt` (Note: Currently, most tools use the Python standard library and have no external dependencies).

---

## 🧰 The Tools

### 1. X Momentum Assessor
**File:** `x-momentum-assessor.py`
**Purpose:** The most important tool in the kit. It scores your account across the 5 pillars of the X Momentum Framework (XMF).
- **Usage:** `python x-momentum-assessor.py`
- **Output:** A total score out of 100, your Momentum Tier, and a targeted recommendation for what to improve next.

### 2. Post Analyzer
**File:** `post-analyzer.py`
**Purpose:** Analyze a post draft for hook strength, readability, and engagement potential.
- **Usage:** `python post-analyzer.py` (Then paste your post and press Ctrl+D).
- **Output:** Scores for Hook Strength, Structure, and Engagement Potential with specific improvement tips.

### 3. Hook Generator
**File:** `hook-generator.py`
**Purpose:** Generate 5 proven hook templates based on your topic and target audience.
- **Usage:** `python hook-generator.py`
- **Sample Command:**
  ```bash
  $ python hook-generator.py
  Enter your topic: SEO
  Enter your target audience: beginners
  ```

### 4. Engagement Score Estimator
**File:** `engagement-score.py`
**Purpose:** A heuristic-based tool to estimate the "signal strength" of a content idea before you write it.
- **Usage:** `python engagement-score.py`
- **Logic:** Uses weighted scoring for Novelty, Utility, Relatability, and Authority.

### 5. Thread Builder
**File:** `thread-builder.py`
**Purpose:** Rapidly structure a multi-post thread from a set of main points.
- **Usage:** `python thread-builder.py`
- **Output:** A complete thread skeleton including hook, body posts, summary, and CTA.

### 6. Content Idea Generator
**File:** `content-idea-generator.py`
**Purpose:** Generate 3 unique content prompts based on your niche and goals using proven content frameworks.
- **Usage:** `python content-idea-generator.py`

---

## 🔗 Integration with the Lab

- **Datasets:** These tools are powered by heuristics derived from the [Algorithm Explained](../docs/algorithm-explained.md) and [Ranking Signals](../docs/ranking-signals.md) documentation.
- **Templates:** Use the [XMF Scorecard](../docs/xmf-scorecard.md) as a manual reference alongside the `x-momentum-assessor.py`.
- **Framework:** Every tool is built to support one or more pillars of the **X Momentum Framework**.

## 🛠 Contributing
Have an idea for a new tool? Check out [CONTRIBUTING.md](../CONTRIBUTING.md) and help us build the future of open-source creator tooling!
