import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from io import BytesIO
import pandas as pd

st.set_page_config(page_title="Future Color Bot", layout="centered")

# Title
st.title("🎨 Future Color Bot")
st.write("A Creative Project by Grade 7 • Amrita Vidyalayam")

# User inputs
name = st.text_input("Enter your Name")
age = st.text_input("Enter your Age")
city = st.text_input("Enter your City")

colors_list = ["Red", "Blue", "Yellow", "Green", "Pink", "Purple", "Orange"]
color = st.selectbox("Pick Your Favourite Color", colors_list)

messages = {
    "Red": "You are bold and passionate! Big adventures await you.",
    "Blue": "You are calm, wise, and creative. A bright future lies ahead!",
    "Yellow": "You are cheerful and full of energy. Happiness follows you!",
    "Green": "You are peaceful and smart. Success comes naturally to you.",
    "Pink": "You are loving, kind, and full of imagination!",
    "Purple": "You are unique and talented. Magic is in your future!",
    "Orange": "You are enthusiastic and confident. Great things await!"
}

excel_file = "futurecolor_data.xlsx"

# Ensure Excel exists
try:
    df = pd.read_excel(excel_file)
except:
    df = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message"])
    df.to_excel(excel_file, index=False)

# Button
if st.button("✨ Reveal My Future"):

    if not name or not age or not city:
        st.error("Please fill all fields!")
    else:
        msg = messages[color]

        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Save to Excel
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

        # Generate PDF Certificate
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)

        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(300, 740, "Certificate of Participation")

        c.setFont("Helvetica", 16)
        c.drawCentredString(300, 700, f"Presented to: {name}")

        c.setFont("Helvetica", 14)
        c.drawCentredString(300, 660, f"Age: {age}  |  City: {city}")

        c.drawCentredString(300, 620, f"Your future is: {msg}")

        c.setFont("Helvetica-Oblique", 12)
        c.drawCentredString(300, 560, "Amrita Vidyalayam • Computer Expo 2025")

        c.showPage()
        c.save()

        pdf_data = buffer.getvalue()

        st.download_button(
            label="📜 Download Certificate (PDF)",
            data=pdf_data,
            file_name=f"{name}_certificate.pdf",
            mime="application/pdf"
        )
