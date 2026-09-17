import streamlit as st
import joblib

model = joblib.load("Logistic_regression_Student_StudyHrs_model(1).pkl")

st.title("Student Pass/Fail Prediction")

hours = st.number_input("Enter Study Hours:",min_value=0.0,max_value=15.0,value=5.0)

attendance = st.number_input("Enter Attendance:",min_value=0.0,max_value=100.0,value=75.0)

if st.button("Predict"):

    new_data = [[hours, attendance]]

    prediction = model.predict(new_data)

    probability = model.predict_proba(new_data)

    pass_prob = probability[0][1] * 100
    fail_prob = probability[0][0] * 100

    if prediction[0] == 1:
        st.success("Pass")
        st.write("Probability of Pass:", round(pass_prob, 2), "%")
        st.write("Probability of Fail:", round(fail_prob, 2), "%")

    else:
        st.error("Fail")
        st.write("Probability of Fail:", round(fail_prob, 2), "%")
        st.write("Probability of Pass:", round(pass_prob, 2), "%")
