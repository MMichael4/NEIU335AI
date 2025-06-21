# Interactive expert system simulation
rules = [
    {"if": ["fever", "sore_throat"], "then": "possible_strep_throat"},
    {"if": ["fever", "cough"], "then": "possible_flu"},
    {"if": ["headache"], "then": "possible_migraine"},
    {"if": ["sore_throat"], "then": "possible_common_cold"},
]

user_input = input("Enter your symptoms separated by commas: ").lower().split(',')
facts = {symptom.strip(): True for symptom in user_input}

# Inference engine
inferred = []

for rule in rules:
    if all(facts.get(condition, False) for condition in rule["if"]):
        inferred.append(rule["then"])

if inferred:
    print("Based on your symptoms, possible conditions include:", ", ".join(inferred))
else:
    print("No conditions matched your symptoms. Please consult a medical professional.")
