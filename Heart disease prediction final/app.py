import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Load model
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Set page config
st.set_page_config(page_title="Heart Disease Prediction App", layout="centered")

# Custom background image
def set_bg_from_url(url, opacity=1):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('{url}') no-repeat center center fixed;
            background-size: cover;
        }}
        .block-container {{
            background-color: rgba(2, 3, 4, {opacity});
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_from_url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768", opacity=0.95)

# Navigation Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Predict", "About"],
        icons=["activity", "info-circle"],
        default_index=0
    )

if selected == "Predict":
    st.title("\U0001F49B Heart Disease Prediction")
    st.write("Fill out the details below to predict heart disease risk.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input('Age', min_value=0, max_value=120)
            sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
            cp = st.slider('Chest Pain Type (0–3)', 0, 3)
            trestbps = st.number_input('Resting Blood Pressure')
            chol = st.number_input('Cholesterol (mg/dl)')
            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
            restecg = st.slider('Resting ECG Results (0–2)', 0, 2)

        with col2:
            thalach = st.number_input('Max Heart Rate Achieved')
            exang = st.selectbox('Exercise Induced Angina', [0, 1])
            oldpeak = st.number_input('ST Depression', step=0.1)
            slope = st.slider('Slope of Peak ST (0–2)', 0, 2)
            ca = st.slider('Number of Major Vessels (0–4)', 0, 4)
            thal = st.slider('Thal (0 = normal, 1 = fixed, 2 = reversible)', 0, 2)

        submitted = st.form_submit_button("Predict")

        if submitted:
            features = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                         exang, oldpeak, slope, ca, thal]]
            prediction = heart_disease_model.predict(features)[0]
            if prediction == 1:
                st.error("\U0001F494 The person **has heart disease**.")
            else:
                st.success("\U0001F496 The person **does not have heart disease**.")

elif selected == "About":
    st.title("About this App")
    st.markdown("""
        This **Heart Disease Prediction App** uses machine learning to predict if someone
        is likely to have heart disease based on medical inputs.

        - Model: Trained using standard heart datasets.
        - Developer: Thangella Pradeepthi
        - Powered by: [Streamlit](https://streamlit.io/)
    """)
