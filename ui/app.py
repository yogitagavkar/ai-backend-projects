import requests
import streamlit as st


try:
    test = requests.get("https://restaurant-order-chatbot-final.onrender.com/")
    st.write("Backend status:", test.json())
except Exception as e:
    st.error(f"Backend not reachable: {e}")