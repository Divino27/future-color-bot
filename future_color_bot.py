# future_color_bot.py (online / cloud-safe version)
import streamlit as st
from datetime import date
import io
from PIL import Image, ImageDraw, ImageFont

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="FutureColor Bot - Expo", page_icon="🎉", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
  background: linear-gradient(135deg,#fff1e6,#fff8e1);
}
.header {
  background: rgba(255,255,255,0.95);
  padding: 18px;
  border-radius: 16px;
  text-align:center;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
  margin-bottom: 16px;
}
.form {
  background: rgba(255,255,255,0.98);
  padding: 14px;
  border-radius: 14px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
fun_image = "https://cdn-icons-png.flaticon.com/512/2729/2729007.png"
robot_image = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png"
st.markdown(f"""
<div class="header">
  <img src="{fun_image}" style="width:120px;border-radius:14px"><br>
  <h1 style="color:#7B2CBF; margin:6px 0 2px 0;">Welcome to the Computer Expo 2025 🎉</h1>
  <h3 style="color:#FF4D8D; margin:0;">Amrita Vidyalayam</h3>
  <p style="margin-top:8px;color:#333;">A creative project by Grade 7 students 💻✨</p>
</div>
""", unsafe_allow_html=True)

# ---------------- FORM ----------------
st.markdown('<div class="form">', unsafe_allow_html=True)
name = st.text_input("👤 Your Name")
age = st.number_input("🎂 Your Age", min_value=1, max_value=100, step=1)
city = st.text_input("🏙️ Your City")
color = st.selectbox("🎨 Your Favourite Color", ["Red","Blue","Green","Yellow","Purple","Pink","Black","White"])
st.markdown('</div>', unsafe_allow_html=True)

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

# Keep responses in session state (cloud-safe)
if "responses" not in st.session_state:
    st.session_state.responses = []

def make_certificate_image(student_name, message_text, school_name="Amrita Vidyalayam",
                           expo_name="Computer Expo 2025", cert_date=None, logo_path=None):
    """Create a colorful PNG certificate using Pillow and return bytes."""
    if cert_date is None:
        cert_date = date.today().strftime("%B %d, %Y")

    # Image size (landscape)
    W, H = 1400, 900
    img = Image.new("RGB", (W, H), "#FFF3E0")  # soft background

    draw = ImageDraw.Draw(img)

    # Draw top band
    draw.rounded_rectangle([30, 30, W-30, 150], radius=24, fill="#FFD1DC")
    # Draw bottom band
    draw.rounded_rectangle([30, H-150, W-30, H-30], radius=24, fill="#FFF2CC")

    # Title
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 48)
        big_font = ImageFont.truetype("arialbd.ttf", 44)
        med_font = ImageFont.truetype("arial.ttf", 24)
        small_font = ImageFont.truetype("arial.ttf", 18)
    except Exception:
        # fallback to default
        title_font = ImageFont.load_default()
        big_font = ImageFont.load_default()
        med_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Certificate title
    w = draw.textsize("Certificate of Participation", font=title_font)[0]
    draw.text(((W-w)/2, 50), "Certificate of Participation", font=title_font, fill="#6A1B9A")

    # Expo name subtitle
    subtitle = expo_name
    w = draw.textsize(subtitle, font=med_font)[0]
    draw.text(((W-w)/2, 110), subtitle, font=med_font, fill="#D81B60")

    # Student Name
    name_y = 270
    draw.text((W/2 - draw.textsize(student_name, font=big_font)[0]/2, name_y), student_name, font=big_font, fill="#333333")

    # Message (wrap)
    max_w = W - 160
    lines = []
    words = message_text.split()
    line = ""
    for word in words:
        test = (line + " " + word).strip()
        if draw.textsize(test, font=med_font)[0] <= max_w:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)
    y_text = name_y + 70
    for ln in lines:
        w = draw.textsize(ln, font=med_font)[0]
        draw.text(((W-w)/2, y_text), ln, font=med_font, fill="#444444")
        y_text += 34

    # Footer: school and date
    draw.text((60, H-100), f"Issued by: {school_name}", font=small_font, fill="#333333")
    draw.text((W-60-draw.textsize(cert_date,font=small_font)[0], H-100), f"Date: {cert_date}", font=small_font, fill="#333333")

    # Badge circle left bottom
    draw.ellipse([60, H-190, 60+120, H-70], fill="#FFB74D")
    draw.text((60+60 - draw.textsize("EXPO", font=med_font)[0]/2, H-140), "EXPO", font=med_font, fill="white")

    # Signature line right
    draw.line([W-380, H-120, W-160, H-120], fill="#666666", width=2)
    draw.text((W-160, H-100), "Principal", font=small_font, fill="#333333")

    # Add logo if exists (using provided path)
    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            # Resize logo
            max_logo_w = 160
            ratio = max_logo_w / logo.width
            new_size = (int(logo.width*ratio), int(logo.height*ratio))
            logo = logo.resize(new_size, Image.ANTIALIAS)
            img.paste(logo, (W - new_size[0] - 80, 40), logo)
        except Exception:
            pass

    # Save to bytes
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf.read()

# ---------------- SUBMIT ACTION ----------------
if st.button("✨ Reveal My Future"):
    if name.strip() == "" or city.strip() == "":
        st.error("Please fill all fields.")
    else:
        msg = messages[color]
        st.success(f"Hi **{name}**, here is your colourful future:")
        st.info(msg)

        # Store response in session only (cloud-safe)
        st.session_state.responses.append({
            "Name": name,
            "Age": int(age),
            "City": city,
            "Favorite Color": color,
            "Message": msg,
            "Date": date.today().isoformat()
        })

        # Create certificate image bytes
        # <-- Use the logo path you uploaded earlier (local path used in codespace)
        logo_path = "/mnt/data/13cf8c6e-fc5c-4e48-992a-02f728719cf0.png"
        # If running locally on school PC, put the logo file in project folder and use:
        # logo_path = "logo.png"

        png_bytes = make_certificate_image(student_name=name, message_text=msg,
                                           school_name="Amrita Vidyalayam",
                                           expo_name="Computer Expo 2025",
                                           cert_date=date.today().strftime("%B %d, %Y"),
                                           logo_path=logo_path)

        # Show the certificate preview
        st.image(png_bytes, use_column_width=True, output_format="PNG")

        # Download button
        st.download_button(
            label="📥 Download Certificate (PNG)",
            data=png_bytes,
            file_name=f"{name.replace(' ','_')}_certificate.png",
            mime="image/png"
        )

# ---------------- RESPONSES VIEW (optional) ----------------
with st.expander("See responses collected in this session (temporary)"):
    st.write(st.session_state.responses)

st.write("---")
st.caption("© 2025 • Computer Expo • Amrita Vidyalayam • Made with ❤️ by Grade 7 Students")
