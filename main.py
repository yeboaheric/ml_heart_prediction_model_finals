import pickle
import streamlit as st
from streamlit_option_menu import option_menu 

#loading saved models
heart_disease_model = pickle.load(open('/Users/user/Desktop/codes/finals for mac/saved prediction model/heart_disease_final.sav', 'rb'))


#page title
st.markdown("<h1 style='text-align: center;'> 🫀iHEART CHECKER</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    age = int(st.number_input('Age'.upper(), min_value=0))
with col2:
    sex = int(st.number_input('Sex (0 = female, 1 = male)'.upper(), min_value=0, max_value=1))

with col1:
    cp = int(st.number_input('Chest Pain types (0-3)'.upper(), min_value=0, max_value=3))
with col2:
    trestbps = int(st.number_input('Resting Blood Pressure'.upper(), min_value=0))

with col1:
    chol = int(st.number_input('Serum Cholesterol in mg/dl'.upper(), min_value=0))
with col2:
    fbs = int(st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)'.upper(), min_value=0, max_value=1))

with col1:
    restecg = int(st.number_input('Resting Electrocardiographic results (0-2)'.upper(), min_value=0, max_value=2))
with col2:
    thalach = int(st.number_input('Maximum Heart Rate Achieved'.upper(), min_value=0))

with col1:
    exang = int(st.number_input('Exercise Induced Angina (1 = yes, 0 = no)'.upper(), min_value=0, max_value=1))
with col2:
    oldpeak = float(st.number_input('ST depression induced by exercise'.upper()))

with col1:
    slope = int(st.number_input('Slope of the peak exercise ST segment (0-2)'.upper(), min_value=0, max_value=2))
with col2:
    ca = int(st.number_input('Major vessels colored by fluoroscopy (0-3)'.upper(), min_value=0, max_value=3))

with col1:
    thal = int(st.number_input('Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible defect)'.upper(), min_value=0, max_value=2))



#result
survival_diagnosis = ''


#prepare for prediction
user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]


if st.button('Predict Heart Disease'):
    survival_prediction = heart_disease_model.predict([user_input])
    if (survival_prediction[0] == 1):
        survival_diagnosis = "⚠️ Oops, you have a heart disease!"
    else:
        survival_diagnosis = "✅ Good news! you don't have a heart disease."

st.success(survival_diagnosis)
