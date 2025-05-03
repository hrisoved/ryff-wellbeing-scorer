![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Required-blue?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)


# 🎯 Ryff Psychological Wellbeing Scorer

This project implements a command-line Python tool for administering and scoring **Carol Ryff’s Psychological Wellbeing Scale**.  
The tool allows users to answer all 42 questions interactively, handles reverse scoring, and computes final scores across six psychological wellbeing subscales.

---

## 🔍 Features

- 📋 **Questionnaire Prompt**: Presents all 42 Ryff items using a 1–7 Likert scale  
- ✅ **Input Validation**: Ensures only valid numeric responses are accepted  
- 🔄 **Reverse Scoring**: Applies scoring logic for negatively worded items using `8 - response`  
- 📊 **Subscale Scoring**: Calculates total scores for each of the following:
  - Autonomy  
  - Environmental Mastery  
  - Personal Growth  
  - Positive Relations with Others  
  - Purpose in Life  
  - Self-Acceptance  
- 💾 **Data Export**:
  - `user_responses.csv`: Raw input from the user
  - `scored_responses.csv`: Includes metadata and reverse-scored answers
  - `subscale_summary.csv`: Final total scores per subscale
- 🚫 **Duplicate Protection**: If a previous response file exists, the user is prompted before overwriting

---

## 📃 Logic Overview

- The program reads `questions.csv`, which defines:
  - The question text
  - Associated subscale
  - Whether the item is reverse-scored  
- The user responds to each item using a **1–7 Likert scale**
- After all responses:
  - Reverse scoring is applied where appropriate
  - A merged DataFrame is created with `ScoredResponse`
  - Subscale scores are calculated by grouping and summing
- All outputs are saved as `.csv` files for easy reuse

---

## 🛠️ Technologies

- Python 3.12.6  
- pandas  
- os (included in Python standard library)

---

## 📦 Installation & Usage

### ✅ Requirements

Make sure you have Python and `pandas` installed.

```bash
pip install pandas
```

🧩 Version Flexibility

This tool now supports:

- **42-item Ryff Scale** (default)
- **18-item Ryff Scale** – a shorter version based on the official [SPARQ Tools source](https://sparqtools.org/mobility-measure/psychological-wellbeing-scale/)

To use the 18-item version, replace `questions.csv` with `questions_18.csv` or modify the script to accept a `--version` flag (e.g., via argparse).

🔄 **Reverse Scoring Note**:
The reverse scoring logic uses a SCALE_POINTS constant set to the default `7` as per method described in the source documentation. This can be changed if needed.

## 📚 Source

This project uses the 42-item version of the **Ryff Psychological Wellbeing Scale**, as published by Stanford SPARQ:  
🔗 [Psychological Wellbeing Scale – SPARQTools.org](https://sparqtools.org/mobility-measure/psychological-wellbeing-scale/)

