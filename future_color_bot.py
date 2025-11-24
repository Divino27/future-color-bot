import streamlit as st
import pandas as pd

# ---- PAGE SETUP ----
st.set_page_config(page_title="Future Color Bot", layout="wide")

# Background Colour
st.markdown(
    """
    <style>
        body {
            background-color: #FFEBD4;
        }
        .main {
            background-color: #FFEBD4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- HEADER CARD ----
st.markdown(
    """
    <div style="
        background-color:#FFF4E6;
        padding:30px;
        border-radius:20px;
        text-align:center;
        border: 3px solid #FFB067;">
        
        <h1 style="color:#A0328C;">🌈 Welcome to the Computer Expo 2025!</h1>
        <h2 style="color:#FF4F70;">Amrita Vidyalayam</h2>
        <h4 style="color:#444;">A Creative Project by Grade 7 Students 💻✨</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- FUN IMAGES ----
st.write("")
st.write("")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3081/3081875.png", width=150)
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/527/527020.png", width=150)
with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/3793/3793447.png", width=150)

st.write("")

# ---- INPUT CARD ----
st.markdown(
    """
    <div style="
        background-color:#FFF9F0;
        padding:25px;
        border-radius:20px;
        border:2px solid #FFB067;">
        <h3 style="text-align:center; color:#B22E6F;">✨ Tell Us About You</h3>
    </div>
    """,
    unsafe_allow_html=True
)

name = st.text_input("🧒 Your Name")
age = st.text_input("🎂 Your Age")
city = st.text_input("🏙 Your City")

colors_list = ["Red", "Blue", "Yellow", "Green", "Pink", "Purple", "Orange"]
color = st.selectbox("🎨 Pick Your Favourite Colour", colors_list)

# ---- FUTURE MESSAGES ----
messages = {
    "Red": "🔥 You are bold and passionate! Big adventures await you.",
    "Blue": "🌊 You are calm, wise, and creative. A bright future lies ahead!",
    "Yellow": "🌟 You are cheerful and full of energy. Happiness follows you!",
    "Green": "🍀 You are peaceful and smart. Success comes naturally to you.",
    "Pink": "💖 You are loving, kind, and full of imagination!",
    "Purple": "🔮 You are unique and talented. Magic is in your future!",
    "Orange": "⚡ You are enthusiastic and confident. Great things await!"
}

excel_file = "futurecolor_data.xlsx"

# Make sure excel exists
try:
    df = pd.read_excel(excel_file)
except:
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_excel(excel_file, index=False)

# ---- BUTTON ACTION ----
if st.button("🌟 Reveal My Future!"):

    if not name or not age or not city:
        st.error("⚠️ Please fill all fields!")
    else:
        msg = messages[color]

        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Save to excel
        new_row = {
            "Name": name,
            "Age": int(age),
            "City": city,
            "Favorite Color": color,
            "Message": msg
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(excel_file, index=False)

        st.success("🎉 Saved your response! Thank you for visiting the Expo.")

# ---- FOOTER ----
st.write("")
st.markdown(
    """
    <div style="text-align:center; color:#A0328C; margin-top:40px;">
        <p>© 2025 • Amrita Vidyalayam • Grade 7 Computer Expo 🌟</p>
    </div>
    """,
    unsafe_allow_html=True
)
# Download Excel File
with open("futurecolor_data.xlsx", "rb") as f:
    excel_bytes = f.read()

st.download_button(
    label="📥 Download Visitor Excel Data",
    data=excel_bytes,
    file_name="futurecolor_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

