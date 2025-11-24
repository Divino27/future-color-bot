# future_color_bot.py
import streamlit as st
import pandas as pd
import os
from datetime import date
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.lib.units import mm

# ---------------- Page setup ----------------
st.set_page_config(
    page_title="FutureColor Bot - Computer Expo",
    page_icon="🎉",
    layout="centered"
)

# ---------------- Styling ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe9d6, #fff4e3, #fbe4c2);
    background-size: cover;
}
.header-box {
    background: rgba(255,255,255,0.92);
    padding: 22px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
}
.top-image { width: 150px; border-radius:18px; }
.form-box {
    background: rgba(255,255,255,0.95);
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0px 6px 12px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header (fun images) ----------------
fun_image = "https://cdn-icons-png.flaticon.com/512/2729/2729007.png"
robot_image = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png"

st.markdown(f"""
<div class="header-box">
    <img src="{fun_image}" class="top-image"><br>
    <h1 style="color:#8A2BE2; margin:6px 0;">Welcome to the Computer Expo 2025 🎉</h1>
    <h3 style="color:#FF1493; margin:0;">Amrita Vidyalayam</h3>
    <p style="color:#333; margin-top:6px;">A Creative Project by Grade 7 Students 💻✨</p>
    <img src="{robot_image}" style="width:90px; margin-top:6px;">
</div>
""", unsafe_allow_html=True)

# ---------------- Data (Excel) setup ----------------
excel_file = "futurecolor_data.xlsx"
if not os.path.exists(excel_file):
    df_init = pd.DataFrame(columns=["Name", "Age", "City", "Favorite Color", "Message", "Date"])
    df_init.to_excel(excel_file, index=False)

# ---------------- Form ----------------
st.markdown('<div class="form-box">', unsafe_allow_html=True)
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100)
city = st.text_input("🏙️ Your City")
color = st.selectbox("🎨 Your Favourite Color", ["Red","Blue","Green","Yellow","Purple","Pink","Black","White"])
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- Messages ----------------
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

# ---------------- Helper: create certificate PDF (colorful fun style) ----------------
def create_certificate_pdf(student_name, message_text, school_name="Amrita Vidyalayam",
                           expo_name="Computer Expo 2025", cert_date=None, logo_path=None):
    """Return bytes of a PDF certificate."""
    if cert_date is None:
        cert_date = date.today().strftime("%B %d, %Y")

    buffer = io.BytesIO()
    # Use landscape A4
    c = canvas.Canvas(buffer, pagesize=landscape(A4))
    width, height = landscape(A4)

    # Draw colorful background rectangles (fun)
    c.setFillColor(colors.HexColor("#FFF3E0"))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    # soft top band
    c.setFillColor(colors.HexColor("#FFD1DC"))
    c.roundRect(20*mm, height - 40*mm, width - 40*mm, 30*mm, 8*mm, fill=1, stroke=0)
    # bottom band
    c.setFillColor(colors.HexColor("#FFF2CC"))
    c.roundRect(20*mm, 10*mm, width - 40*mm, 28*mm, 8*mm, fill=1, stroke=0)

    # Title
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(colors.HexColor("#6A1B9A"))
    c.drawCentredString(width/2, height - 28*mm, f"Certificate of Participation")

    # Expo subtitle
    c.setFont("Helvetica", 16)
    c.setFillColor(colors.HexColor("#D81B60"))
    c.drawCentredString(width/2, height - 36*mm, expo_name)

    # Student name box
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawCentredString(width/2, height - 62*mm, student_name)

    # Message below name
    c.setFont("Helvetica-Oblique", 18)
    c.setFillColor(colors.HexColor("#444444"))
    text_y = height - 80*mm
    # Wrap message if needed
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import Paragraph
    style = ParagraphStyle(name='Normal', fontName='Helvetica-Oblique', fontSize=16, alignment=1, textColor=colors.HexColor("#444444"))
    p = Paragraph(message_text, style)
    w, h = p.wrap(width - 80*mm, 60*mm)
    p.drawOn(c, 40*mm, text_y - h/2)

    # School and date
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawString(40*mm, 30*mm, f"Issued by: {school_name}")
    c.drawRightString(width - 40*mm, 30*mm, f"Date: {cert_date}")

    # Place a small badge/icon on left bottom
    c.setFillColor(colors.HexColor("#FFB74D"))
    c.circle(30*mm, 40*mm, 12*mm, fill=1, stroke=0)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.white)
    c.drawCentredString(30*mm, 40*mm - 4, "EXPO")

    # Add signature line (right)
    c.setStrokeColor(colors.HexColor("#666666"))
    c.setLineWidth(1)
    c.line(width - 110*mm, 45*mm, width - 40*mm, 45*mm)
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawRightString(width - 40*mm, 35*mm, "Principal")

    # Add logo if available (try to load)
    if logo_path and os.path.exists(logo_path):
        try:
            img = ImageReader(logo_path)
            # draw it top-right
            img_w = 30*mm
            img_h = 30*mm
            c.drawImage(img, width - 40*mm - img_w, height - 40*mm - img_h/2, width=img_w, height=img_h, mask='auto')
        except Exception:
            pass

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.read()

# ---------------- Submit action & Certificate download ----------------
if st.button("✨ Reveal My Future"):
    if name.strip() == "" or city.strip() == "":
        st.error("Please fill all fields!")
    else:
        msg = messages.get(color, "")
        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Save to Excel locally
        df = pd.read_excel(excel_file)
        new_row = {
            "Name": name,
            "Age": int(age),
            "City": city,
            "Favorite Color": color,
            "Message": msg,
            "Date": date.today().isoformat()
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(excel_file, index=False)
        st.success("Your response has been saved to Excel! 📘")

        # Create certificate bytes
        # LOGO: use uploaded path from session, or local "logo.png" if present in project folder.
        # Default here uses the uploaded path used earlier in this chat.
        logo_path = "/mnt/data/13cf8c6e-fc5c-4e48-992a-02f728719cf0.png"
        # If you're running on school computer, copy that logo into the project folder as "logo.png"
        # and uncomment the following line instead:
        # logo_path = "logo.png"

        pdf_bytes = create_certificate_pdf(student_name=name, message_text=msg,
                                          school_name="Amrita Vidyalayam",
                                          expo_name="Computer Expo 2025",
                                          cert_date=date.today().strftime("%B %d, %Y"),
                                          logo_path=logo_path)

        # Show download button
        st.download_button(
            label="📥 Download Certificate (PDF)",
            data=pdf_bytes,
            file_name=f"{name.replace(' ','_')}_certificate.pdf",
            mime="application/pdf"
        )

# ---------------- Footer ----------------
st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
