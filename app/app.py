import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("model.pkl")

with st.form("predict"):
    locality = st.selectbox(
    "Choose a locality:",['Yalahanka','BTM Layout', 'Attibele', 'K R Puram ', 'Marathahalli', 'Indiranagar', 'Electronic City', 'Malleshwaram', 'Jayanagar'])
    area = st.number_input("Area", value=2661)
    rent = st.number_input("rent", value=100000)
    facing = st.selectbox(
    "Choose a facing:",['East','North-West',  'North', 'West', 'North-East', 'South-East', 'South', 'Missing'])
    bhk = st.selectbox(
    "Choose a bhk:",[1,2,3,4])
    bathrooms = st.number_input("bathrooms", value=2, min_value=1, max_value=26, step=1)
    parking = st.selectbox("Choose a parking:",['Bike', 'Bike and Car', 'Car', 'Missing'])
    submitted = st.form_submit_button("Predict")


if submitted:
    X = pd.DataFrame([{
        "locality": locality,
        "area": area,
        'rent':rent,
        "facing": facing,
        "BHK": bhk,
        "bathrooms": bathrooms,
        "parking": parking 
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price(price per sqft): {pred:,.2f}")
