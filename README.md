# Medi Score Calculator

## Overview

This program calculates the **Medi Score** for a patient from their physiological readings. The Medi Score is a simple rule-based scoring system that helps flag potentially unwell patients based on five observations: respiration rate, oxygen saturation, consciousness level, temperature, and whether the patient is receiving supplemental oxygen.

The program validates every input and rounds temperature values to one decimal place (as required by the test cases).

## How to run

### 1. Install Python (if you don't already have it)

Check whether Python is installed:

```bash
python --version
```

If it isn't, download it from [python.org](https://www.python.org/downloads/).

### 2. Run the script

From the project folder:

```bash
python medi_score.py
```

### 3. Follow the prompts

- Enter the patient's name.
- Enter the patient's physiological readings (respiration rate, oxygen saturation, temperature, and so on).
- The program validates each input to make sure it falls within an acceptable range.
- The final Medi Score is displayed, along with a breakdown of how it was calculated.

## Scoring system

Each observation is scored against defined physiological ranges, and the individual scores are summed to give the total Medi Score. The five inputs are:

- Respiration rate
- Oxygen saturation
- Consciousness level
- Temperature
- Supplemental oxygen

## Assumptions and considerations

- Temperature values are automatically rounded to one decimal place.
- All inputs are validated to prevent incorrect or out-of-range entries.
- Oxygen saturation scoring takes into account whether the patient is breathing air or on supplemental oxygen.
- Edge cases (for example, a patient on oxygen with a high saturation reading) are handled and scored correctly.
