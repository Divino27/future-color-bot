import streamlit as st
import pandas as pd
import os

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="FutureColor Bot - Computer Expo",
    page_icon="🎉",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe9d6, #fff4e3, #fbe4c2);
    background-size: cover;
}

.header-box {
    background: rgba(255,255,255,0.92);
    padding: 28px;
    border-radius: 25px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.22);
    text-align: center;
    margin-bottom: 25px;
}

.top-image {
    width: 200px;
    margin-bottom: 10px;
    border-radius: 20px;
}

.robot-image {
    width: 120px;
    margin-top: -15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER WITH FUN IMAGES ----------------

# Fun, kid-friendly images from the internet
fun_image = "https://yt3.ggpht.com/ytc/AIdro_lNE9F1qUp8GvAxWoWy67enscUnKgwEB5Rj00Fm35aa-w=s800-c-k-c0x00ffffff-no-rw"
robot_image = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png"

st.markdown(f"""
<div class="header-box">
    <img src="{fun_image}" class="top-image">
    <h1 style="color:#8A2BE2; font-weight:900;">Welcome to the Computer Expo 2025 🎉</h1>
    <h2 style="color:#FF1493;">Amrita Vidyalayam</h2>
    <h4 style="color:#333;">A Creative Project by V. Madhavan, 7A 💻✨</h4>
    <img src="{robot_image}" class="robot-image">
</div>
""", unsafe_allow_html=True)

# ---------------- EXCEL SETUP ----------------
excel_file = "futurecolor_data.xlsx"

if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_excel(excel_file, index=False)

# ---------------- FORM ----------------
st.markdown("<div class='form-box'>", unsafe_allow_html=True)

name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
color = st.selectbox(
    "🎨 Your Favourite Color",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Black", "White"]
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FUTURE MESSAGES ----------------
messages = {
    "Red": (
        "🔥 You are bold, passionate, and full of unstoppable energy! "
        "Your future is filled with exciting adventures and leadership opportunities. "
        "People naturally look up to you because of your confidence and strong personality. "
        "Whatever you dream of — sports, science, arts, or innovation — you will chase it with power! "
        "A bright and thrilling path awaits you!"
    ),

    "Blue": (
        "🌊 Calm, intelligent, and thoughtful — you are someone who brings peace wherever you go. "
        "Your future shows great success in academics and creative thinking. "
        "Because of your strong focus and clarity, you will solve complex problems that others find difficult. "
        "A future filled with knowledge, wisdom, and meaningful achievements waits for you!"
    ),

    "Green": (
        '🌿 You have a gentle heart and a peaceful soul. You care for people and nature equally. '
        "Your future shines brightly with kindness, creativity, and emotional strength. "
        "You will inspire many people with your calm presence, positive attitude, and ability to help others. "
        "A beautiful, harmonious journey lies ahead for you!"
    ),

    "Yellow": (
        "🌟 Cheerful, bright, and full of brilliant ideas — you are a natural creator! "
        "Your future is overflowing with creativity, imagination, and fun experiences. "
        "People love your positive energy, and you have the power to make any place happier. "
        "You will shine in everything you do, especially in areas like art, innovation, and teamwork!"
    ),

    "Purple": (
        "🔮 You are unique, imaginative, and full of deep thoughts. "
        "Your future holds extraordinary success in fields that require creativity, strategy, and innovation. "
        "You think differently from others — and that is your greatest strength. "
        "One day, your ideas will truly make a difference in the world!"
    ),

    "Pink": (
        "💖 You are loving, joyful, and full of kindness. "
        "Your future is filled with friendships, happy experiences, and opportunities to spread positivity. "
        "People enjoy being around you because you make them feel valued and special. "
        "A warm, cheerful, and exciting journey awaits you!"
    ),

    "Black": (
        "⚫ Strong, focused, and extremely determined — you never give up! "
        "Your future shows leadership, discipline, and major achievements. "
        "You have the power to stay calm under pressure and handle challenges better than most people. "
        "A successful and powerful destiny is waiting for you!"
    ),

    "White": (
        "🤍 Pure-hearted, calm, and peaceful — you bring comfort and clarity to everyone around you. "
        "Your future is full of balance, emotional strength, and gentle success. "
        "You will create harmony in your surroundings and become a source of inspiration for others. "
        "A serene and beautiful journey lies ahead for you!"
    )
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

# Download Excel File
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
