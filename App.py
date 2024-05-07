import numpy as np
import pandas as pd
import pickle as pkl 
import streamlit as st

model = pkl.load(open('MIPML.pkl', 'rb'))

# Streamlit app header
st.header('Medical Insurance Premium Predictor')

# Function to validate yes/no inputs
def validate_yes_no_input(prompt):
    response = st.radio(prompt, ('Yes', 'No'))
    return response.lower()

# Function to validate integer inputs
def validate_integer_input(prompt):
    value = st.number_input(prompt, min_value=0, step=1)
    return int(value)

# Get user inputs
Age = validate_integer_input("Enter age: ")

Diabetes = validate_yes_no_input("Do you have diabetes?")

BloodPressureProblems = validate_yes_no_input("Do you have blood pressure problems?")

AnyTransplants = validate_yes_no_input("Have you undergone any transplants?")

AnyChronicDiseases = validate_yes_no_input("Do you have any chronic diseases?")

Height = validate_integer_input("Enter Height (in cm): ")

Weight = validate_integer_input("Enter Weight (in kg): ")

KnownAllergies = validate_yes_no_input("Do you have any known allergies?")

HistoryOfCancerInFamily = validate_yes_no_input("Is there a history of cancer in your family?")

number_of_major_surgeries = validate_integer_input("Enter the number of major surgeries: ")

# Map yes/no answers to 0 and 1
Diabetes = 1 if Diabetes == "yes" else 0
BloodPressureProblems = 1 if BloodPressureProblems == "yes" else 0
AnyTransplants = 1 if AnyTransplants == "yes" else 0
AnyChronicDiseases = 1 if AnyChronicDiseases == "yes" else 0
KnownAllergies = 1 if KnownAllergies == "yes" else 0
HistoryOfCancerInFamily = 1 if HistoryOfCancerInFamily == "yes" else 0

# Create input data array
input_data = ([Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies, HistoryOfCancerInFamily, number_of_major_surgeries])
input_data_array = np.asarray(input_data)
input_data_array = input_data_array.reshape(1,-1)

# Use the best model to make predictions
predicted_prem = model.predict(input_data_array)

# Convert predicted premium to float if necessary
predicted_prem = float(predicted_prem[0])


predicted_prem_in_rupees = predicted_prem 

# Display predicted insurance premium in rupees
display_string_rupees = f'Insurance Premium will be {predicted_prem_in_rupees:.2f} Rupees'
st.markdown(display_string_rupees)


