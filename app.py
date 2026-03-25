import streamlit as st
import random

st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("🏦 Smart Fraud Detection System")
st.markdown("### 💳 Digital Payment Security Demo")

st.divider()

# Input Section
st.subheader("Enter Transaction Details")

amount = st.number_input("Transaction Amount (₹)", min_value=0)
location = st.selectbox("Location", ["Same Country", "Different Country"])
time = st.selectbox("Time", ["Day", "Night"])
device = st.selectbox("Device", ["Known Device", "New Device"])

st.divider()

# Fraud Logic
fraud_score = 0

if amount > 5000:
    fraud_score += 30
elif amount > 1000:
    fraud_score += 15

if location == "Different Country":
    fraud_score += 25

if time == "Night":
    fraud_score += 20

if device == "New Device":
    fraud_score += 30

fraud_probability = min(fraud_score, 100)

# Show result
if st.button("🔍 Analyze Transaction"):
    st.subheader("Analysis Result")

    st.progress(fraud_probability / 100)
    st.write(f"### Fraud Probability: {fraud_probability}%")

    if fraud_probability > 70:
        st.error("🚨 High Risk Transaction Detected!")

        st.write("### 🔐 OTP Verification Required")
        otp = random.randint(1000, 9999)
        st.info(f"(Demo OTP: {otp})")

        user_otp = st.text_input("Enter OTP")

        if user_otp:
            if user_otp == str(otp):
                st.success("✅ Transaction Approved")
            else:
                st.error("❌ Incorrect OTP - Transaction Blocked")

    elif fraud_probability > 40:
        st.warning("⚠️ Suspicious Transaction - Monitoring")

    else:
        st.success("✅ Safe Transaction")

    # Transaction Log
    st.divider()
    st.subheader("📜 Transaction Summary")
    st.write(f"Amount: ₹{amount}")
    st.write(f"Location: {location}")
    st.write(f"Time: {time}")
    st.write(f"Device: {device}")
