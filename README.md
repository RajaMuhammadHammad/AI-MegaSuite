
```markdown
# 🧠 AI-MegaSuite

**AI-MegaSuite** is a powerful, multi-feature AI-powered desktop web application built with Python and Streamlit. It provides a range of functionalities including Optical Character Recognition (OCR), text summarization, image sketching, text-to-speech, voice-to-text, and PDF report generation — all in one intuitive platform.

---

## 🚀 Features

- 📷 **OCR (Image to Text)**  
  Extract readable text from uploaded image files using Tesseract OCR.

- 📝 **Text Summarizer**  
  Summarize long paragraphs into shorter meaningful text.

- 🎨 **Image to Sketch**  
  Convert uploaded images into hand-drawn style sketches using image filters.

- 🔊 **Text-to-Speech**  
  Convert your written text into spoken audio using Google Text-to-Speech.

- 🎤 **Voice-to-Text**  
  Upload audio and convert voice into text using SpeechRecognition and Google API.

- 📄 **PDF Report Generator**  
  Compile all outputs into a downloadable PDF report of your session.

---

## 📁 Project Structure

```
AI-MegaSuite/
│
├── text_to_speech.py        # Main Streamlit application file
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
└── output/                  # Output files (PDFs, audio)
```

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AI-MegaSuite.git
cd AI-MegaSuite
```

### 2. Set Up Python Environment

Make sure Python 3.7+ is installed.

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

- 📦 [Download Tesseract OCR for Windows](https://github.com/tesseract-ocr/tesseract/wiki)
- Install it to the default directory:
  ```
  C:\Program Files\Tesseract-OCR\tesseract.exe
  ```
- Then ensure your code contains:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 🧪 Run the App

```bash
streamlit run text_to_speech.py
```

---

## 🧾 requirements.txt

Here’s what to include in your `requirements.txt`:

```txt
streamlit
pillow
pytesseract
gTTS
SpeechRecognition
fpdf
```


## 🤝 Contributing

Pull requests are welcome!  
If you find a bug or want to add new features, feel free to open an issue or submit a PR.

---

## 👨‍💻 Developed By

**Raja Muhammad Hammad**  
---

```
