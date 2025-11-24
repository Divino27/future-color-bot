import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="FutureColor Bot - Computer Expo",
    page_icon="🎉",
    layout="centered"
)

# ---------------- CUSTOM CSS (NEW & COLOURFUL) ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif !important;
}

body {
    background: linear-gradient(135deg, #FFD8C2, #FFF1CE, #FFE5D9);
    background-size: cover;
}

/* HEADER CARD */
.header-box {
    background: linear-gradient(135deg, #ffffff, #ffe9f5, #e8d9ff);
    padding: 40px;
    border-radius: 30px;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.18);
    text-align: center;
    margin-bottom: 35px;
    animation: fadeIn 1.2s ease-in-out;
}

.top-image {
    width: 180px;
    margin-bottom: 15px;
    border-radius: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

/* Robot floating animation */
.robot-image {
    width: 110px;
    margin-top: 10px;
    animation: float 3s infinite ease-in-out;
}

/* Floating cute animation */
@keyframes float {
 0% { transform: translateY(0px); }
 50% { transform: translateY(-12px); }
 100% { transform: translateY(0px); }
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #ff77c8, #9c6bff);
    color: white;
    font-size: 18px;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.2);
}

/* Inputs */
input, select, textarea {
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER WITH FUN IMAGES ----------------

logo_url = "https://www.amrita.edu/wp-content/uploads/2022/09/amrita-vidyalayam-logo.png"
robot_image = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png"

st.markdown(f"""
<div class="header-box">

    <img src="{logo_url}" class="top-image">

    <h1 style="color:#8A2BE2; font-weight:900; line-height:1.2;">
        Welcome to the <br> Computer Expo 2025 🎉
    </h1>

    <h2 style="color:#FF1493; font-weight:700;">
        Amrita Vidyalayam
    </h2>

    <h4 style="color:#333; font-weight:600;">
        A Creative Project by V. Madhavan, 7A 💻✨
    </h4>

    <img src="{robot_image}" class="robot-image">

</div>
""", unsafe_allow_html=True)

# ---------------- EXCEL SETUP ----------------

excel_file = "futurecolor_data.xlsx"
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_excel(excel_file, index=False)

# ---------------- FORM ----------------

name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
color = st.selectbox(
    "🎨 Your Favourite Color",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"]
)

# ---------------- FUTURE MESSAGES ----------------

messages = {
    "Red": "🔥 You are bold and passionate! Big adventures await you.",
    "Blue": "🌊 Calm and intelligent — academic success is in your future!",
    "Green": "🌿 Kind-hearted and peaceful — you will inspire many people.",
    "Yellow": "🌟 Cheerful and creative — amazing ideas are coming your way!",
    "Purple": "🔮 Unique thinker — you will shine in unexpected ways!",
    "Pink": "💖 Positive and loving — people enjoy being around you.",
    "Black": "⚫ Strong, focused, and determined — success is guaranteed.",
    "White": "🤍 Calm and pure — you bring peace wherever you go."
}

# ---------------- SUBMIT BUTTON ----------------

if st.button("✨ Reveal My Future"):
    if name == "" or city == "":
        st.error("Please fill all fields!")
    else:
        msg = messages[color]

        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Save to Excel
        df = pd.read_excel(excel_file)
        new_row = {
            "Name": name,
            "Age": int(age),
            "City": city,
            "Favorite Color": color,
            "Message": msg
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(excel_file, index=False)

        st.success("Your response has been saved to Excel! 📘")

# ---------------- DOWNLOAD BUTTON ----------------

with open("futurecolor_data.xlsx", "rb") as f:
    excel_bytes = f.read()

st.download_button(
    label="📥 Download Visitor Excel Data",
    data=excel_bytes,
    file_name="futurecolor_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ---------------- FOOTER ----------------
st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
