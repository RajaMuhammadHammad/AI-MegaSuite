import streamlit as st
from PIL import Image, ImageFilter
import pytesseract
from gtts import gTTS
import speech_recognition as sr
import base64
from fpdf import FPDF
import datetime

# Helper Functions
def ocr_core(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update if different
    text = pytesseract.image_to_string(image)
    return text

def image_to_sketch(image):
    gray = image.convert("L")
    sketch = gray.filter(ImageFilter.CONTOUR)
    return sketch

def summarize_text(text):
    if len(text.split()) < 30:
        return text
    return " ".join(text.split()[:30]) + "..."

def convert_text_to_speech(text):
    tts = gTTS(text=text)
    tts.save("output.mp3")
    return "output.mp3"

def convert_voice_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio)
    except:
        return "Could not understand audio."

def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="AI App Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    pdf.cell(200, 10, txt=f"Generated: {now}", ln=True)

    for section, content in data.items():
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(200, 10, txt=section, ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=content)

    pdf.output("AI_Report.pdf")
    return "AI_Report.pdf"

# Streamlit UI
st.set_page_config(page_title="AI Mega App", layout="centered")
st.title("🧠 Multi-Feature AI Application")

menu = ["OCR", "Text Summarizer", "Sketch from Image", "Text-to-Speech", "Voice-to-Text", "PDF Report"]
choice = st.sidebar.selectbox("Choose a Feature", menu)

report_data = {}

if choice == "OCR":
    st.subheader("📷 OCR - Image to Text")
    img_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if img_file:
        image = Image.open(img_file)
        st.image(image, caption="Uploaded Image")
        text = ocr_core(image)
        st.success("Extracted Text:")
        st.write(text)
        report_data["OCR Output"] = text

elif choice == "Text Summarizer":
    st.subheader("📝 Text Summarizer")
    user_text = st.text_area("Enter long text")
    if st.button("Summarize"):
        summary = summarize_text(user_text)
        st.success("Summary:")
        st.write(summary)
        report_data["Summary"] = summary

elif choice == "Sketch from Image":
    st.subheader("🎨 Image to Sketch")
    sketch_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if sketch_file:
        image = Image.open(sketch_file)
        sketch = image_to_sketch(image)
        st.image(sketch, caption="Sketch Image")

elif choice == "Text-to-Speech":
    st.subheader("🔊 Text to Voice")
    text_input = st.text_area("Enter text to convert into voice")
    if st.button("Convert"):
        audio_path = convert_text_to_speech(text_input)
        audio_file = open(audio_path, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
        report_data["Text-to-Speech"] = text_input

elif choice == "Voice-to-Text":
    st.subheader("🎤 Voice to Text")
    audio_file = st.file_uploader("Upload audio file", type=["wav", "mp3"])
    if audio_file:
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_file.read())
        recognized = convert_voice_to_text("temp_audio.wav")
        st.success("Recognized Text:")
        st.write(recognized)
        report_data["Voice-to-Text"] = recognized

elif choice == "PDF Report":
    st.subheader("📄 Generate PDF Report")
    st.info("Generate a professional report of your session")
    if st.button("Generate Report"):
        filename = generate_pdf_report(report_data)
        with open(filename, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<a href="data:application/pdf;base64,{base64_pdf}" download="AI_Report.pdf">📄 Download Report</a>'
        st.markdown(pdf_display, unsafe_allow_html=True)
