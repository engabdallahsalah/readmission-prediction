import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\Abd-Allah\Downloads\readmission_predictor.pkl")  

# Title
st.title("🏥 Diabetes Readmission Prediction App")

st.write("""
This app predicts **whether a diabetic patient is likely to be readmitted** to the hospital.
Just fill in the patient information below:
""")

# Function to extract midpoint from age range
def age_range_to_numeric(age_range):
    # Extract numbers from the range string
    numbers = [int(s) for s in age_range.replace('[', '').replace(')', '').split('-')]
    # Return the midpoint of the range
    return sum(numbers) / len(numbers)

# Input features
def user_input_features():
    # Basic patient information
    age_range = st.selectbox('Age Range', ['[0-10)', '[10-20)', '[20-30)', '[30-40)', '[40-50)',
                                     '[50-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)'])
    
    gender = st.selectbox("Gender", ['Male', 'Female'])
    race = st.selectbox("Race", ['Caucasian', 'AfricanAmerican', 'Hispanic', 'Asian', 'Other'])
    
    # Hospital stay information
    time_in_hospital = st.slider('Time in Hospital (days)', 1, 14, 3)
    
    # Medical procedures and diagnoses
    num_lab_procedures = st.slider('Number of Lab Procedures', 0, 132, 40)
    num_procedures = st.slider('Number of Procedures', 0, 20, 1)
    num_medications = st.slider('Number of Medications', 0, 81, 10)
    number_diagnoses = st.slider('Number of Diagnoses', 1, 16, 5)
    
    # The missing columns from the error message
    total_diagnoses = st.slider('Total Diagnoses', 1, 30, 7)
    total_procedures = st.slider('Total Procedures', 0, 30, 5)
    medication_intensity = st.slider('Medication Intensity', 0.0, 10.0, 3.0)
    service_intensity = st.slider('Service Intensity', 0.0, 10.0, 3.0)
    
    # Diabetes-specific information
    A1Cresult = st.selectbox("A1C Result", ['None', 'Norm', '>7', '>8'])
    insulin = st.selectbox("Insulin Treatment", ['No', 'Up', 'Down', 'Steady'])

    # Dictionary of features
    data = {
        'age': age_range_to_numeric(age_range),  # Convert age to numeric
        'gender': gender,  # Keep as is
        'race': race,  # Keep as is
        'time_in_hospital': float(time_in_hospital),
        'num_lab_procedures': float(num_lab_procedures),
        'num_procedures': float(num_procedures),
        'num_medications': float(num_medications),
        'number_diagnoses': float(number_diagnoses),
        'total_diagnoses': float(total_diagnoses),
        'total_procedures': float(total_procedures),
        'medication_intensity': float(medication_intensity),
        'service_intensity': float(service_intensity),
        'A1Cresult': A1Cresult,
        'insulin': insulin
    }
    
    # Create display data with original age range
    display_data = data.copy()
    display_data['age'] = age_range
    
    return pd.DataFrame([data]), pd.DataFrame([display_data])

# Get user input
prediction_df, display_df = user_input_features()

# Show user input (with readable age range)
st.subheader("Entered Patient Data:")
st.write(display_df)

# Predict button
if st.button("Predict Readmission"):
    try:
        # Make prediction
        prediction = model.predict(prediction_df)[0]
        prediction_proba = model.predict_proba(prediction_df)[0][1]

        if prediction == 1:
            st.error(f"🔁 Patient is **likely to be readmitted**. (Probability: {prediction_proba:.2f})")
        else:
            st.success(f"✅ Patient is **not likely to be readmitted**. (Probability: {prediction_proba:.2f})")
    
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
        
        # More detailed error information
        import traceback
        st.write("Detailed error:")
        st.code(traceback.format_exc())
        
        # Debug information
        if hasattr(model, 'feature_names_in_'):
            st.write("Model expects these features:")
            st.write(model.feature_names_in_)
            
            expected_features = set(model.feature_names_in_)
            actual_features = set(prediction_df.columns)
            
            st.write("Missing features:")
            st.write(expected_features - actual_features)
            
            st.write("Extra features:")
            st.write(actual_features - expected_features)

# Footer
st.markdown("---")
st.caption("📅 Built by **Abdallah Salah**, 2025")          