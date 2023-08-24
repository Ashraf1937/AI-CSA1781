% Define a database of diseases and their recommended diets
disease(heart_disease, low_fat_diet).
disease(diabetes, low_sugar_diet).
disease(high_blood_pressure, low_sodium_diet).

% Define the rule for suggesting a diet based on a disease
suggest_diet(Disease, Diet) :- disease(Disease, Diet).