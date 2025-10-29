import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")

st.title("🏠 House Price Prediction")
st.caption("Demo app — plug your real model later. Ready for Streamlit Cloud.")

st.divider()
st.subheader("Enter features")

with st.form("predict_form"):
	sqft = st.number_input("Square Feet", min_value=100, value=1200, step=50)
	beds = st.number_input("Bedrooms", min_value=0, value=3, step=1)
	baths = st.number_input("Bathrooms", min_value=0, value=2, step=1)
	age_years = st.number_input("Age of house (years)", min_value=0, value=10, step=1)
	zipcode = st.text_input("ZIP Code (optional)")
	submitted = st.form_submit_button("Predict price")

def dummy_model_prediction(features_df: pd.DataFrame) -> float:
	base = 100000
	price = (
		base
		+ 230 * features_df["sqft"].iloc[0]
		+ 15000 * features_df["beds"].iloc[0]
		+ 12000 * features_df["baths"].iloc[0]
		- 800 * features_df["age_years"].iloc[0]
	)
	return float(price)

if submitted:
	features = pd.DataFrame(
		{
			"sqft": [sqft],
			"beds": [beds],
			"baths": [baths],
			"age_years": [age_years],
			"zipcode": [zipcode or ""],
		}
	)

	with st.spinner("Predicting..."):
		pred = dummy_model_prediction(features)

	st.success(f"Estimated price: ${pred:,.0f}")
	st.caption("This is a placeholder. Replace with your trained model.")

with st.expander("How to plug in your real model"):
	st.markdown(
		"""
		- Save your trained model as a pickle (e.g., `models/model.pkl`).
		- Replace `dummy_model_prediction` with a function that loads the model and predicts.
		- Add needed libraries to `requirements.txt` (e.g., scikit-learn, xgboost).
		"""
	)


