import streamlit as st
import joblib

model=joblib.load("logistic_regression_studyhours_model.pkl")
st.title("Student Pass/Fail based on Study Hours")
hours=st.number_input("Enter Study Hours:", min_value=0.0 ,max_value=15.0, value=5.0)
if st.button("Predict"):
  prediction=model.predict([[hours]])
  probability = model.predict_proba([[hours]])
  pass_prob=probability[0][1]*100
  fail_prob=probability[0][0]*100
  if prediction[0]==1:
    st.success("Pass")
    st.write("Probability of Pass:", round(pass_prob,2),"%")

  else:
    st.error("Fail")
    st.write("Probability of Fail:", round(fail_prob,2),"%")
