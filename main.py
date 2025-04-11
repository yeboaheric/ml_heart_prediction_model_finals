import pickle
import streamlit as st
from streamlit_option_menu import option_menu 

#loading saved models
heart_disease_model = pickle.load(open('heart_disease.sav', 'rb'))


#page title
st.title('HEART DISEASE CHECKER')

col1, col2 = st.columns(2)

with col1:
    age = int(st.number_input('Age'.upper()))

with col2:
    sex = int(st.number_input('Sex (0 = female, 1 = male)'.upper()))

with col1:
    cp = int(st.number_input('Chest Pain types (0-3)'.upper()))

with col2:
    trestbps = int(st.number_input('Resting Blood Pressure'.upper()))

with col1:
    chol = int(st.number_input('Serum Cholesterol in mg/dl'.upper()))

with col2:
    fbs = int(st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)'.upper()))

with col1:
    restecg = int(st.number_input('Resting Electrocardiographic results (0-2)'.upper()))

with col2:
    thalach = int(st.number_input('Maximum Heart Rate Achieved'.upper()))

with col1:
    exang = int(st.number_input('Exercise Induced Angina (1 = yes, 0 = no)'.upper()))

with col2:
    oldpeak = float(st.number_input('ST depression induced by exercise'.upper()))

with col1:
    slope = int(st.number_input('Slope of the peak exercise ST segment (0-2)'.upper()))

with col2:
    ca = int(st.number_input('Major vessels colored by fluoroscopy (0-3)'.upper()))

with col1:
    thal = int(st.number_input('Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible defect)'.upper()))

#code for heart disease prediction 
    heart_diagnosis = ''

#creating a button for prediction
user_input = [
    age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
]

#reshape for scikit-learn's 2D requirement

if st.button('Heart Disease Test Results'):
        heart_prediction = heart_disease_model.predict([user_input])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'Sorry, you have a heart disease.'
        else:
            heart_diagnosis = 'Good News! you do not have a heart disease.'

st.success(heart_diagnosis)

