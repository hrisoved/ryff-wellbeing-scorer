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
- 🔄 **Reverse Scoring**: Applies scoring logic for negatively worded items using a configurable formula:  
  `(SCALE_POINTS + 1) - response`   
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

- Loads metadata from a `.csv` file containing:
  - Question text
  - Subscale category
  - Reverse-scored flag
- The user responds to each item using a **1–7 Likert scale**
- After responses are collected:
  - Applies reverse scoring to items marked as reverse-scored
  - Merges metadata with user responses into a single `ScoredResponse`DataFrame
  - Computes subscale scores by grouping responses and summing them
- All outputs are saved as `.csv` files for easy review or further analysis

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

### 🧩 Version Flexibility

This tool now supports:

- **42-item Ryff Scale** (default)
- **18-item Ryff Scale** (a shorter version)

To select the version, use the `--version` flag when running the script:

```bash
python score-riff.py --version 42   # for the full version  
```
```bash

python score-riff.py --version 18   # for the short version
```


## 📚 Source

This project offers both the 42-item and 18-item version of the **Ryff Psychological Wellbeing Scale**, as published by Stanford SPARQ:  
🔗 [Psychological Wellbeing Scale – SPARQTools.org](https://sparqtools.org/mobility-measure/psychological-wellbeing-scale/)

