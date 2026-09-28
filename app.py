import joblib
import pandas as pd
import streamlit as st

### Loading saved model
model = joblib.load("model_final.pkl")

### Title
st.title("Cardiovascular Heart Disease (CHD) Risk Predictor")
st.markdown("Enter patient details below to predict **10-year cardiovascular disease risk.** - Input ranges were restricted to the ranges observed in the training dataset to reduce extrapolation beyond the model's training domain.")
st.divider()

### Setting user inputs
st.subheader("Patient Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=32,
        max_value=70,
        value=32,
        step=1
    )

    education = st.selectbox(
        "Education Level",
        options=[1, 2, 3, 4]
    )

    cigsperday = st.number_input(
        "Cigarettes Per Day",
        min_value=0,
        max_value=70,
        value=0,
        step=1
    )

    bpmeds = st.selectbox(
        "Blood Pressure Medication",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


with col2:
    
    diabp = st.number_input("Diastolic BP (mmHg)", min_value=48.0, max_value=142.5, value=48.0, step=0.1)

    prevalenthyp = st.selectbox(
        "Prevalent Hypertension",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    prevalentstroke = st.selectbox(
        "Previous Stroke",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    diabetes = st.selectbox(
        "Diabetes",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    totchol = st.number_input(
        "Total Cholesterol (mg/dL)",
        min_value=113.0,
        max_value=600.0,
        value=113.0,
        step=1.0
    )


with col3:

    bmi = st.number_input(
        "BMI",
        min_value=15.54,
        max_value=56.8,
        value=15.54,
        step=0.1
    )

    heartrate = st.number_input(
        "Heart Rate (bpm)",
        min_value=44.0,
        max_value=143.0,
        value=44.0,
        step=1.0
    )

    glucose = st.number_input(
        "Glucose (mg/dL)",
        min_value=40.0,
        max_value=394.0,
        value=40.0,
        step=0.1
    )

    male = st.selectbox(
            "Male",
            options=[0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )


st.divider()


### Prediction Button
if st.button("🔍 Predict Risk", use_container_width=True):

    # Assemble input using the SAME feature names used during training
    input_data = pd.DataFrame([{
        "age": age,
        "education": education,
        "cigsperday": cigsperday,
        "bpmeds": bpmeds,
        "prevalenthyp": prevalenthyp,
        "prevalentstroke": prevalentstroke,
        "diabetes": diabetes,
        "totchol": totchol,
        "diabp": diabp,
        "bmi": bmi,
        "heartrate": heartrate,
        "glucose": glucose,
        "male":male
    }])

    ### Prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]


    ### Prediction
    prediction  = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ **High Risk** — {probability*100:.1f}% probability of cardiovascular disease")
    else:
        st.success(f"✅ **Low Risk** — {probability*100:.1f}% probability of cardiovascular disease")

    # Probability bar
    st.markdown("**Risk Probability**")
    st.progress(float(probability))

    # Input summary
    with st.expander("📋 View Patient Summary"):
        st.dataframe(input_data.T.rename(columns={0: "Value"}))