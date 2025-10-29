# House Price Prediction (Streamlit App)

A minimal Streamlit app to demo house price prediction. It ships with a placeholder model you can replace with your trained model.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this folder to a public GitHub repository.
2. Go to Streamlit Community Cloud and create a new app, selecting your repo.
3. Set the main file to `app.py` (default), and deploy.

If you later add a real model, also update `requirements.txt` with any new libraries (e.g., scikit-learn, xgboost) so Streamlit can install them during build.

## Replacing the placeholder model
- Save your trained model (e.g., `models/model.pkl`).
- Replace `dummy_model_prediction` in `app.py` to load and use your model.
- Re-deploy (Streamlit Cloud auto-rebuilds on new commits).

## Files
- `app.py` — Streamlit UI and prediction logic (placeholder).
- `requirements.txt` — Python dependencies for the app runtime.
- `README.md` — Instructions.

## License
MIT
