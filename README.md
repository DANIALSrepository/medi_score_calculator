# Medi Score Calculation Program

##  Overview
This program calculates the *Medi Score* for a patient based on their *physiological ranges* 
The Medi Score is a *simple rule-based scoring system* that helps identify *ill patients* based on their *respiration rate, oxygen saturation, consciousness level, temperature, and supplemental oxygen use*.

The program **validates all inputs** and ensures that *temperature values are rounded to 1 decimal place* (as per test requirements).

---

## How to Run the Program

### *1 Install Python (if not already installed)*
You can check if Python is installed by running:

If Python is not installed, download it from [Python.org](https://www.python.org/downloads/).

### *2 Run the Script*
To run the program, use code:


### *3 Follow the Prompts*
- Enter the patient's **name*.
- Input the patient's **physiological data** (respiration rate, oxygen saturation, temperature, etc.).
- The program will *validate your inputs* to ensure they are within the correct range.
- The final *Medi Score* will be displayed, along with a breakdown of how it was calculated.

---

##  Scoring System
### * Respiration Rate*
### * Oxygen Saturation*
### * Consciousness*
### * Temperature*
### * Supplemental Oxygen*


##  Assumptions & Considerations
- *Temperature values are automatically rounded to 1 decimal place.*
- *All input values are validated** to prevent incorrect data entries.
- *Oxygen saturation scoring accounts for whether the patient is on oxygen or not.*
- *Edge cases* (e.g., a patient on oxygen with high saturation) are correctly assigned.
