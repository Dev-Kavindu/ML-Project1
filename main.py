import streamlit as st
import joblib
import numpy as np
import pandas as pd

# -----------------------
# Load trained model
# -----------------------
model = joblib.load("Notebooks/model1.pkl")  # Your trained model that predicts in millions

# -----------------------
# Currency options
# -----------------------
currencies = {
    "USD": "$",
    "LKR": "රු",
    "EUR": "€",
    "GBP": "£",
    "INR": "₹",
    "AUD": "A$",
    "CAD": "C$"
}

currency_names = {
    "USD": "US Dollars",
    "LKR": "Sri Lankan Rupees",
    "EUR": "Euro",
    "GBP": "British Pound",
    "INR": "Indian Rupees",
    "AUD": "Australian Dollars",
    "CAD": "Canadian Dollars"
}

# -----------------------
# Page config
# -----------------------
st.set_page_config(
    page_title="📊 Sales Prediction App",
    page_icon="💰",
    layout="wide"
)

# -----------------------
# Responsive CSS
# -----------------------
st.markdown("""
    <style>
    body { background-color: #F0F2F6; color: #000; }
    .stNumberInput input { font-size:18px; }
    div[data-baseweb="select"] > div { cursor:pointer !important; }
    div[data-baseweb="select"]:hover { border:2px solid #4CAF50; border-radius:8px; }

    .prediction-card {
        background: linear-gradient(135deg, #26a69a, #004d40);
        color: #e0f7fa;
        padding: 40px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }
    .prediction-title { font-size:32px; font-weight:bold; margin-bottom:15px; }
    .prediction-value { font-size:60px; font-weight:bold; margin:0; }
    .prediction-currency { font-size:22px; margin-top:10px; }

    @media only screen and (max-width: 600px) {
        .prediction-value { font-size:40px; }
        .prediction-title { font-size:24px; }
        .prediction-currency { font-size:16px; }
        .stNumberInput input { font-size:16px; }
    }
    @media only screen and (min-width:601px) and (max-width:1024px) {
        .prediction-value { font-size:48px; }
        .prediction-title { font-size:28px; }
        .prediction-currency { font-size:18px; }
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# Title
# -----------------------
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>📈 Sales Prediction App</h1>
    <p style='text-align: center; font-size: 18px;'>
        Predict sales using advertising budgets trained with a machine learning model.
    </p>
    <hr>
""", unsafe_allow_html=True)

# -----------------------
# Currency selection
# -----------------------
currency_display = st.selectbox(
    "🌍 Select Currency Symbol",
    list(currencies.keys()),
    index=0,
    help="Choose currency symbol for predicted sales"
)
symbol = currencies[currency_display]
currency_name_full = currency_names[currency_display]

# -----------------------
# Input fields
# -----------------------
st.markdown("### 🧮 Enter Advertising Budget Values")
col1, col2, col3 = st.columns([1,1,1])
with col1:
    tv = st.number_input(f"📺 TV Budget ({symbol})", min_value=0.0, value=100.0)
with col2:
    radio = st.number_input(f"📻 Radio Budget ({symbol})", min_value=0.0, value=20.0)
with col3:
    newspaper = st.number_input(f"📰 Newspaper Budget ({symbol})", min_value=0.0, value=30.0)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------
# Prediction
# -----------------------
if st.button("🔮 Predict Sales", use_container_width=True):
    X = np.array([[tv, radio, newspaper]])
    prediction = model.predict(X)[0]  # Model already predicts in millions

    # Prediction output card
    st.markdown(f"""
        <div class="prediction-card">
            <h2 class="prediction-title">✅ Predicted Sales</h2>
            <h1 class="prediction-value">{symbol} {prediction:,.2f} Million</h1>
            <p class="prediction-currency">({currency_name_full})</p>
        </div>
    """, unsafe_allow_html=True)

    # Simulated historical chart (optional)
    history_df = pd.DataFrame({
        "Day": np.arange(1, 8),
        "Predicted Sales": np.random.normal(prediction, prediction*0.05, 7)
    })
    st.markdown("### 📊 Predicted Sales History (Last 7 Days)")
    st.line_chart(history_df.rename(columns={"Predicted Sales": f"Sales ({symbol}M)"}).set_index("Day"))

    st.balloons()

# -----------------------
# Footer
# -----------------------
st.markdown("""
    <hr>
    <p style="text-align: center; color: #666;">
        Developed by <b>Kavindu Chamod</b> — Machine Learning Project 🚀
    </p>
""", unsafe_allow_html=True)
