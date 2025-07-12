import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# --- Load and Train the Model ---
@st.cache_resource
def train_model():
    df = pd.read_csv("vertical_borer_5000_dataset.csv")
    X = df.drop("Maintenance_Needed", axis=1)
    y = df["Maintenance_Needed"]
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

model = train_model()

st.title("🔧 Predictive Maintenance: Vertical Borer Machine")
st.markdown("Enter sensor readings manually to check if maintenance is required:")

# --- Input Fields ---
temp = st.number_input("Temperature (°C)", min_value=30.0, max_value=150.0, value=75.0, step=0.1)
vib = st.number_input("Vibration (mm/s)", min_value=0.0, max_value=5.0, value=0.7, step=0.01)
oil = st.number_input("Oil Flow Rate (L/min)", min_value=0.0, max_value=10.0, value=5.5, step=0.1)

# --- Prediction Logic ---
input_data = pd.DataFrame([[temp, vib, oil]], columns=["Temperature_C", "Vibration_mm_s", "Oil_Flow_L_min"])

if st.button("Predict Maintenance"):
    result = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    # Show prediction result
    if result == 1:
        st.error(f"⚠️ Maintenance Needed (Confidence: {round(proba*100, 2)}%)")
    else:
        st.success(f"✅ No Maintenance Needed (Confidence: {round((1-proba)*100, 2)}%)")

    # --- Chart: Compare with Safe Ranges ---
    st.subheader("📊 Sensor Readings vs Safe Operating Ranges")

    safe_ranges = {
        "Temperature_C": (40, 85),
        "Vibration_mm_s": (0.2, 1.2),
        "Oil_Flow_L_min": (4.5, 7.5)
    }

    values = [temp, vib, oil]
    sensors = ["Temperature (°C)", "Vibration (mm/s)", "Oil Flow (L/min)"]
    safe_low = [safe_ranges["Temperature_C"][0], safe_ranges["Vibration_mm_s"][0], safe_ranges["Oil_Flow_L_min"][0]]
    safe_high = [safe_ranges["Temperature_C"][1], safe_ranges["Vibration_mm_s"][1], safe_ranges["Oil_Flow_L_min"][1]]

    fig, ax = plt.subplots()
    bars = ax.bar(sensors, values, color="skyblue", label="Input")

    # Add safe range lines and danger color
    for i, val in enumerate(values):
        if val < safe_low[i] or val > safe_high[i]:
            bars[i].set_color('red')
        ax.axhspan(safe_low[i], safe_high[i], color='lightgreen', alpha=0.3)

    ax.set_ylabel("Sensor Value")
    ax.set_title("Input vs Safe Operating Range")
    st.pyplot(fig)
