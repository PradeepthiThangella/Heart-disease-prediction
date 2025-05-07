import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu("Heart Disease Prediction System",
                           ["Heart Disease Prediction"],
                           icons=["heart-pulse"],
                           default_index=0)

# App title
st.markdown("<h1 style='text-align: center; color: white;'>Heart Disease Prediction System</h1>", unsafe_allow_html=True)

# Background image and overlay styling
def set_bg():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), 
                        url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768");
            background-size: cover;
            background-position: center;
            color: white;
        }
        h1, h2, h3, label {
            color: white !important;
        }
        div.stButton > button:first-child {
            background-color: #ff4b4b;
            color: white;
            border: None;
            border-radius: 8px;
            padding: 0.5em 1.5em;
            font-size: 1rem;
            font-weight: bold;
        }
        div.stButton > button:hover {
            background-color: #d43f3f;
        }
        </style>
    """, unsafe_allow_html=True)

set_bg()

# Prediction form
if selected == "Heart Disease Prediction":
    st.subheader("Enter Patient Data:")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=1)
        cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3)
        chol = st.number_input('Cholesterol (mg/dl)', min_value=0)
        restecg = st.number_input('Rest ECG (0=normal, 1=ST-T abnormality, 2=left ventricular hypertrophy)', min_value=0, max_value=2)
        oldpeak = st.number_input('Oldpeak (ST depression)', format="%.2f")

    with col2:
        sex = st.number_input('Sex (1=Male, 0=Female)', min_value=0, max_value=1)
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0)
        fbs = st.number_input('Fasting Blood Sugar > 120? (1=True, 0=False)', min_value=0, max_value=1)
        thalach = st.number_input('Max Heart Rate Achieved', min_value=0)
        slope = st.number_input('Slope (0=upsloping, 1=flat, 2=downsloping)', min_value=0, max_value=2)

    with col3:
        exang = st.number_input('Exercise-Induced Angina (1=Yes, 0=No)', min_value=0, max_value=1)
        ca = st.number_input('Number of Major Vessels (0-3)', min_value=0, max_value=3)
        thal = st.number_input('Thal (1=Normal, 2=Fixed Defect, 3=Reversible Defect)', min_value=1, max_value=3)

    # Prediction result
    heart_diagnosis = ""

    if st.button("Predict Heart Disease"):
        with st.spinner("Analyzing..."):
            prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs,
                                                       restecg, thalach, exang, oldpeak,
                                                       slope, ca, thal]])
            if prediction[0] == 1:
                heart_diagnosis = "🚨 The person **has** heart disease."
            else:
                heart_diagnosis = "✅ The person **does not have** heart disease."

    if heart_diagnosis:
        st.markdown(f"""
            <div style='
                margin-top: 2rem;
                padding: 1.5rem;
                background-color: #0e1117;
                color: white;
                border-radius: 10px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                font-size: 1.25rem;
                text-align: center;
            '>
                {heart_diagnosis}
            </div>
        """, unsafe_allow_html=True)

# Footer with credits
st.markdown("""
    <footer>
        <hr style='border: 1px solid white;'>
        <div style='text-align:center; padding: 10px 0; color: white;'>
            Built by <strong>Mohamed Shaad</strong> |
            <a href="https://www.linkedin.com/in/mohamedshaad" style="color:#0A66C2;" target="_blank">LinkedIn</a> |
            <a href="https://github.com/shaadclt" style="color:#fff;" target="_blank">GitHub</a>
        </div>
    </footer>
""", unsafe_allow_html=True)
