# 🔧 Predictive Maintenance System for Vertical Borer Machine (BHEL)

This project implements an AI-powered Predictive Maintenance System using machine learning and real-time sensor inputs. Built specifically for a **Vertical Borer Machine (VBM)**, the system predicts whether maintenance is needed based on parameters like **Temperature, Vibration, and Oil Flow Rate**.

> ✅ Developed under the guidance of BHEL, Haridwar  
> ✅ Built with Python, Streamlit, and Random Forest Classifier  
> ✅ Designed for early failure detection to reduce unplanned downtime

---

## 📌 Features

- **Manual Input Interface** for entering sensor readings
- **Real-Time Predictions** on maintenance needs
- **Confidence Score** for each prediction
- **Safe Range Comparison Chart** with color-coded alerts
- **Random Forest Classifier** trained on synthetic dataset
- Fully functional **Streamlit Web App**

---

## 📊 Input Parameters

| Sensor              | Unit         | Safe Range        |
|---------------------|--------------|-------------------|
| Temperature         | °C           | 40 – 85           |
| Vibration           | mm/s         | 0.2 – 1.2         |
| Oil Flow Rate       | L/min        | 4.5 – 7.5         |

If any of these parameters fall outside the safe range, the app highlights them visually.

---
## 🚀 How to Run the App

streamlit run app.py
