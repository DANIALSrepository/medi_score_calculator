class Patient:
    def __init__(self, name, respiration_rate, oxygen_saturation, consciousness, temperature, supplemental_oxygen):
        self.name = name
        self.respiration_rate = respiration_rate
        self.oxygen_saturation = oxygen_saturation
        self.consciousness = consciousness  # 0 if alert, 3 if CVPU state
        self.temperature = temperature  # Rounded to 1 decimal place
        self.supplemental_oxygen = supplemental_oxygen

def calculate_medi_score(patient):
    score = 0
    breakdown = []

    # Respiration Rate Scoring 
    if patient.respiration_rate < 8 or patient.respiration_rate > 25:
        score += 3
        breakdown.append("Respiration rate is critical (<8 or >25) (+3)")
    elif 21 <= patient.respiration_rate <= 24:
        score += 2
        breakdown.append("Respiration rate is high (21-24) (+2)")
    elif 9 <= patient.respiration_rate <= 11:
        score += 1
        breakdown.append("Respiration rate is slightly low (9-11) (+1)")
    elif 12 <= patient.respiration_rate <= 20:
        breakdown.append("Respiration rate is normal (12-20) (+0)")

    # Oxygen Saturation Scoring 
    if patient.oxygen_saturation < 84:
        score += 3
        breakdown.append("Oxygen saturation is dangerously low (<84) (+3)")
    elif 84 <= patient.oxygen_saturation <= 85:
        score += 2
        breakdown.append("Oxygen saturation is very low (84-85) (+2)")
    elif 86 <= patient.oxygen_saturation <= 87:
        score += 1
        breakdown.append("Oxygen saturation is low (86-87) (+1)")
    elif 88 <= patient.oxygen_saturation <= 92 or (patient.oxygen_saturation >= 93 and not patient.supplemental_oxygen):
        breakdown.append("Oxygen saturation is normal (88-92 or ≥93 on air) (+0)")
    elif 93 <= patient.oxygen_saturation <= 94 and patient.supplemental_oxygen:
        score += 1
        breakdown.append("Oxygen saturation is slightly low on oxygen (93-94 on oxygen) (+1)")
    elif 95 <= patient.oxygen_saturation <= 96 and patient.supplemental_oxygen:
        score += 2
        breakdown.append("Oxygen saturation is moderate on oxygen (95-96 on oxygen) (+2)")
    elif patient.oxygen_saturation >= 97 and patient.supplemental_oxygen:
        score += 3
        breakdown.append("Oxygen saturation is high on oxygen (≥97 on oxygen) (+3)")

    # Consciousness Scoring 
    if patient.consciousness:  # 3 if confused/unresponsive, 0 if alert
        score += 3
        breakdown.append("Patient is confused, responding only to voice/pain, or unresponsive (CVPU) (+3)")
    else:
        breakdown.append("Patient is fully alert (+0)")

    # Temperature Scoring 
    if patient.temperature <= 35.0:
        score += 3
        breakdown.append("Temperature is critically low (≤35.0°C) (+3)")
    elif 35.1 <= patient.temperature <= 36.0:
        score += 1
        breakdown.append("Temperature is slightly low (35.1-36.0°C) (+1)")
    elif 36.1 <= patient.temperature <= 38.0:
        breakdown.append("Temperature is normal (36.1-38.0°C) (+0)")
    elif 38.1 <= patient.temperature <= 39.0:
        score += 1
        breakdown.append("Temperature is slightly high (38.1-39.0°C) (+1)")
    elif patient.temperature >= 39.1:
        score += 2
        breakdown.append("Temperature is high (≥39.1°C) (+2)")

    # Supplemental Oxygen Scoring
    if patient.supplemental_oxygen:
        score += 2
        breakdown.append("Patient requires supplemental oxygen (+2)")
    else:
        breakdown.append("Patient is breathing normal air (+0)")

    return score, breakdown

# Function to get valid user input with ranges that are checked & rounding Temperature
def get_valid_input(prompt, min_value, max_value, value_type=int):
    while True:
        try:
            value = value_type(input(f"{prompt} (inclusive range: {min_value}-{max_value}, {('decimal allowed' if value_type == float else 'whole numbers only')}): "))
            if min_value <= value <= max_value:
                if value_type == float:
                    value = round(value, 1)  # Ensuring temperature is rounded to 1 decimal place
                return value
            else:
                print(f" Please enter a value between {min_value} and {max_value}, including these numbers.")
        except ValueError:
            print(f" Invalid input! Please enter a {value_type.__name__}.")

# Function that obtains consciousness input (Yes/No)
def get_consciousness_input():
    while True:
        response = input("Is the patient confused, responding only to voice/pain, or unresponsive? (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            return 3 if response == "yes" else 0
        else:
            print(" Please enter 'yes' or 'no'.")

# Function that collects all patient data
def get_patient_data():
    print("\n--- Enter Patient Data ---")
    name = input("Enter patient's name: ").strip()
    respiration_rate = get_valid_input("Enter respiration rate", 5, 40, int)
    oxygen_saturation = get_valid_input("Enter oxygen saturation (%)", 50, 100, int)
    consciousness = get_consciousness_input()
    temperature = get_valid_input("Enter temperature (°C)", 30, 42, float)  # This will now be rounded to 1 decimal place

    while True:
        oxygen_input = input("Is the patient on supplemental oxygen? (yes/no): ").strip().lower()
        if oxygen_input in ["yes", "no"]:
            supplemental_oxygen = oxygen_input == "yes"
            break
        else:
            print(" Please enter 'yes' or 'no'.")

    return Patient(name, respiration_rate, oxygen_saturation, consciousness, temperature, supplemental_oxygen)

# Geting input and calculate Medi Score
patient = get_patient_data()
score, breakdown = calculate_medi_score(patient)

# Displaing the structured result with patient's name
print(f"\n--- {patient.name}'s Medi Score Report ---")
for item in breakdown:
    print(f"- {item}")
print(f"\nFinal Medi Score for {patient.name}: {score}")
