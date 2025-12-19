from joblib import load
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------
# Load Model
# ----------------------------------
classifier = load(open("insuranceclassifier.pkl", "rb"))

st.set_page_config(
    page_title="Insurance Premium Prediction",
    page_icon="💰",
    layout="centered"
)

# ----------------------------------
# Helpers
# ----------------------------------
def format_currency(amount):
    return f"₹ {amount:,.2f}"


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 🟦"
    elif bmi < 25:
        return "Normal 🟩"
    elif bmi < 30:
        return "Overweight 🟨"
    else:
        return "Obese 🟥"


def prediction(sex, age, bmi, children, smoker, region):
    sex = 0 if sex == "Male" else 1
    smoker = 0 if smoker == "No" else 1

    region_map = {"North": 0, "East": 1, "West": 2, "South": 3}
    region_num = region_map[region]

    return classifier.predict([[sex, age, bmi, children, smoker, region_num]])[0]


# ----------------------------------
# Dark Mode Toggle
# ----------------------------------
dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
        body, .stApp { background-color: #0f172a; color: #e5e7eb; }
        div[data-testid="stMetric"] { background-color: #020617; }
        </style>
    """, unsafe_allow_html=True)

# ----------------------------------
# Header
# ----------------------------------
st.markdown("""
<div style="padding:20px;border-radius:12px;
background:linear-gradient(135deg,#2563eb,#1e40af)">
<h1 style="color:white;text-align:center;">💰 Insurance Premium Prediction</h1>
<p style="color:#e5e7eb;text-align:center;">
ML-powered insurance premium estimator
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📋 Enter Your Details")

# ----------------------------------
# Inputs
# ----------------------------------
col1, col2 = st.columns(2)

with col1:
    sex = st.selectbox("👤 Gender", ("Male", "Female"))

    age = st.selectbox(
        "🎂 Age",
        options=list(range(18, 101)),
        index=25 - 18
    )

    smoker = st.selectbox("🚬 Smoker", ("No", "Yes"))

with col2:
    bmi = st.selectbox(
        "⚖️ BMI",
        options=list(range(15, 51)),
        index=25 - 15
    )

    children = st.selectbox("👶 Children", list(range(0, 6)))
    region = st.selectbox("🌍 Region", ("North", "East", "West", "South"))

# ----------------------------------
# BMI Helper
# ----------------------------------
st.info(f"🧮 **BMI Category:** {bmi_category(bmi)}")

st.markdown("---")

# ----------------------------------
# Prediction
# ----------------------------------
if st.button("🔮 Predict Premium", use_container_width=True):

    result = prediction(sex, age, bmi, children, smoker, region)

    st.success(f"💸 **Estimated Premium:** {format_currency(result)}")

    # ----------------------------------
    # BMI vs Premium Comparison Chart
    # ----------------------------------
    bmi_range = list(range(18, 36))
    premiums = [
        prediction(sex, age, b, children, smoker, region)
        for b in bmi_range
    ]

    df = pd.DataFrame({
        "BMI": bmi_range,
        "Premium": premiums
    })

    st.markdown("### 📊 Premium Comparison by BMI")

    fig, ax = plt.subplots()
    ax.plot(df["BMI"], df["Premium"], marker="o")
    ax.set_xlabel("BMI")
    ax.set_ylabel("Premium Amount")
    ax.set_title("Impact of BMI on Insurance Premium")

    st.pyplot(fig)

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("""
<hr>
<p style="text-align:center;font-size:12px;color:gray;">
Built with ❤️ using Streamlit & Machine Learning
</p>
""", unsafe_allow_html=True)
