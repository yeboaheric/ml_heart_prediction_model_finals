import pickle
import streamlit as st
from streamlit_option_menu import option_menu 

#loading saved models
heart_disease_model = pickle.load(open('heart_disease.sav', 'rb'))


#page title
#page title
st.markdown("<h1 style='text-align: center;'> 🫀HEART DISEASE CHECKER</h1>", unsafe_allow_html=True)

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

#risk factors analysis
st.markdown("<h2 style='text-align: center;'> 🚨Risk Factors </h2>", unsafe_allow_html=True)

if age >= 50:
    st.warning("Age over 50 increases the risk of heart failure.")
if trestbps >= 130:
    st.warning("High resting blood pressure (130+ mmHg) idicates hypertension.")
if chol >= 240:
    st.warning("High cholesterol (240+ mg/dl) is a risk factor.")
if fbs == 1:
    st.warning("High fasting blood sugar indicates diabetes.")
if thalach <= 100:
    st.warning("Low max heart rate achieved is a risk factor.")
if exang == 1:
    st.warning("Exercise-induced angina is a risk factor.")
if oldpeak >= 2.0:
    st.warning("Significant ST depression (2.0+ mm) is a risk factor.")
if ca > 0:
    st.warning("Presence of major vessels colored by fluoroscopy is a risk factor.")
if thal > 0:
    st.warning("Abnormal thalassemia (fixed/reversible defect) indicates anemia.")



#result
survival_diagnosis = ''


#prepare for prediction
user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]


if st.button('Predict 1 Year Survival'):
    survival_prediction = heart_disease_model.predict([user_input])
    if (survival_prediction[0] == 1):
        survival_diagnosis = '⚠️ The patient is suffering from a heart disease and unlikely to survive beyond 1 year'
    else:
        survival_diagnosis = '✅ The patient has a normal condition and likely to survive at least 1 year.'

st.success(survival_diagnosis)
