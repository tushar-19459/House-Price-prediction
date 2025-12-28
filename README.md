# 🏠 House Price Predictor (Streamlit App)

This project hosts a trained machine learning model locally using **Streamlit** to predict **house price per square foot** based on user inputs like locality, area, rent, BHK, bathrooms, facing, and parking.

---

## 📁 Project Structure

```
├── app.py                # Streamlit application
├── model.pkl             # Trained ML model (Joblib)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

---

## 🚀 Features

- Interactive Streamlit UI
- Loads a pre-trained model using `joblib`
- Predicts house price per sqft
- Runs fully **locally**

---

## 🧾 Requirements

- Python **3.8+**
- pip
- Virtual environment (recommended)

---

## 🔽 Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

> Replace `your-username/your-repo-name` with your actual GitHub repository URL.

---

## 🧪 Create & Activate Virtual Environment (Recommended)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Install Dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

Then run the install command again.

---

## ▶️ Run the Streamlit App Locally

```bash
streamlit run app.py
```

After running the command, Streamlit will open the app automatically in your browser, usually at:

```
http://localhost:8501
```

---

## 🧠 Model Input Features

- **Locality**
- **Area (sqft)**
- **Rent**
- **Facing**
- **BHK**
- **Bathrooms**
- **Parking**

---

## 📊 Output

- Predicted **Price per Square Foot**

---

## 🛠 Troubleshooting

- Ensure `model.pkl` exists in the project root
- Match feature names exactly as used during training
- Use the same preprocessing pipeline (if any)

---

## 📌 Notes

- This app assumes the model was trained with categorical handling (e.g., OneHotEncoder or pipeline)
- Best run inside a virtual environment

---

## 📄 License

This project is for educational purposes.

---

✨ Happy Coding!

