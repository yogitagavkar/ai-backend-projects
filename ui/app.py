# ui/app.py

import streamlit as st
import requests

st.set_page_config(page_title="Restaurant Chatbot")

API_URL = "https://restaurant-order-chatbot-final.onrender.com/chat"

st.title("🍽️ AI Restaurant Chatbot")

# ✅ Persist chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Enter your message", key="input_box")

if st.button("Send") and user_input:

    try:
        res = requests.post(API_URL, json={"user_input": user_input})
        if res.status_code != 200:
            st.error(f"API Error: {res.status_code}")
            st.stop()

        try:
            data = res.json()
        except Exception:
            st.error("Invalid JSON response from API")
            st.stop()

        # Save user message
        st.session_state.messages.append(("user", user_input))

        # Save bot response
        if data.get("response"):
            st.session_state.messages.append(("bot", data["response"]))

        if data.get("bill"):
            st.session_state.messages.append(("bot", data["bill"]))

    except Exception as e:
        st.error(f"Request failed: {e}")
        st.stop()

# 🔥 Display chat history
for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        if isinstance(msg, dict):  # bill
            st.markdown("**🧾 Bill:**")
            for item in msg["items"]:
                st.write(f"{item['qty']} x {item['name']} = ₹{item['line_total']}")
            st.write("---")
            st.write(f"Subtotal: ₹{msg['subtotal']}")
            st.write(f"Tax: ₹{msg['tax']}")
            st.write(f"Tip: ₹{msg['tip']}")
            st.write(f"Discount: ₹{msg['discounts']}")
            st.write(f"### 💰 Total: ₹{msg['total']}")
        else:
            st.markdown("**🤖 Bot:**")
            st.text(msg)