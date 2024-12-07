

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/ayush/OneDrive/Desktop/ML/ML deployed model/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/ayush/OneDrive/Desktop/ML/ML deployed model/heart_model.sav','rb'))





# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
       age = st.text_input('Age', value="0")
        
    with col2:
       sex = st.text_input('Sex (0: Female, 1: Male)', value="0")
       
    with col3:
        cp = st.text_input('Chest Pain types (0-3)', value="0")
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', value="0")
        
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl', value="0")
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (0 or 1)', value="0")
        
    with col1:
        restecg = st.text_input('Resting ECG results (0-2)', value="0")
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved', value="0")
        
    with col3:
        exang = st.text_input('Exercise Induced Angina (0 or 1)', value="0")
        
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise', value="0.0")
        
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment (0-2)', value="0")
        
    with col3:
        ca = st.text_input('Number of Major Vessels (0-4)', value="0")
        
    with col1:
        thal = st.text_input('Thalassemia (0: Normal, 1: Fixed Defect, 2: Reversible Defect)', value="0")
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), float(trestbps), float(chol), int(fbs),
                int(restecg), float(thalach), int(exang), float(oldpeak),
                int(slope), int(ca), int(thal)]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        