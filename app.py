import streamlit as st
import random

st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("🏦 Smart Fraud Detection System")
st.markdown("### 💳 Advanced Digital Payment Security Demo")

st.divider()

# -----------------------------
# INPUT SECTION
# -----------------------------
st.subheader("Enter Transaction Details")

amount = st.number_input("Transaction Amount (₹)", min_value=0)

transaction_type = st.selectbox("Transaction Type", ["UPI", "Card", "Net Banking"])

account_age = st.selectbox("Account Age", ["Old Account", "New Account"])

fraud_history = st.selectbox("Previous Fraud History", ["No", "Yes"])

device = st.selectbox("Device", ["Known Device", "New Device"])

st.divider()

# -----------------------------
# FRAUD LOGIC
# -----------------------------
fraud_score = 0

# Amount check
if amount > 5000:
    fraud_score += 30
elif amount > 1000:
    fraud_score += 15

# Transaction type risk
if transaction_type == "Card":
    fraud_score += 15
elif transaction_type == "Net Banking":
    fraud_score += 10

# Account age
if account_age == "New Account":
    fraud_score += 25

# Login attempts
if login_attempts >= 3:
    fraud_score += 25

# Fraud history
if fraud_history == "Yes":
    fraud_score += 30

# Device check
if device == "New Device":
    fraud_score += 20

fraud_probability = min(fraud_score, 100)

# -----------------------------
# OUTPUT SECTION
# -----------------------------
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

    # -----------------------------
    # TRANSACTION SUMMARY
    # -----------------------------
    st.divider()
    st.subheader("📜 Transaction Summary")

    st.write(f"Amount: ₹{amount}")
    st.write(f"Transaction Type: {transaction_type}")
    st.write(f"Account Age: {account_age}")
    st.write(f"Login Attempts: {login_attempts}")
    st.write(f"Previous Fraud History: {fraud_history}")
    st.write(f"Device: {device}")
