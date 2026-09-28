Cardiovascular Heart Disease (CHD) Risk Predictor

This application predicts a patient's 10-year risk of developing coronary heart disease (CHD) using a machine learning model trained on the Framingham Heart Study dataset. It is designed to be accessible to both clinicians and the general public, providing a fast, data-driven risk assessment based on 13 key health indicators — age, glucose level, diastolic blood pressure, cigarettes smoked per day, Body Mass Index, Prevalent Stroke, Total Cholestrol, Education, Heartrate, Bp Meds, Diabetes, Gender and prevalent hypertension.

The underlying model is a Random Forest Classifier, selected after a rigorous evaluation pipeline that included exploratory data analysis, feature selection using Mutual Information, Permutation Importance, and SHAP values, and cross-validated comparison across multiple models. Input ranges are restricted to values observed in the training dataset to minimise extrapolation beyond the model's learned domain.

Model Performance (Test Set)

On the held-out test set, the model achieved an accuracy of 76.0%, a precision of 34.2%, a recall of 62.1%, and an F1 score of 44.1%. Given the class imbalance inherent in cardiovascular disease datasets, Recall and F1 Score were prioritised over Accuracy as the primary evaluation metrics — ensuring the model is optimised to correctly identify as many at-risk patients as possible.

Disclaimer: This tool is built as a personal portfolio project and is intended for demonstrative purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for clinical decisions.
