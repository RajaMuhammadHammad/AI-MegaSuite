
---

# 🧠 AI-MegaSuite

**AI-MegaSuite** is a powerful, multi-feature AI-powered desktop web application built with Python and Streamlit. It combines functionalities like **OCR**, **text summarization**, **image sketching**, **text-to-speech**, **voice-to-text**, and **PDF report generation**, all in a single, intuitive platform.

---

## 🚀 Features

- 📷 **OCR (Image to Text)**  
  Extract readable text from uploaded image files using Tesseract OCR.

- 📝 **Text Summarizer**  
  Summarize lengthy paragraphs into concise and meaningful text.

- 🎨 **Image to Sketch**  
  Transform uploaded images into hand-drawn style sketches with image filters.

- 🔊 **Text-to-Speech**  
  Convert written text into spoken audio using Google Text-to-Speech.

- 🎤 **Voice-to-Text**  
  Upload audio files and transcribe voice into text using SpeechRecognition and Google API.

- 📄 **PDF Report Generator**  
  Compile all outputs into a downloadable PDF report for your session.

---

## 🛠️ Setup Instructions

### 1. Install Python
Make sure Python 3.8 or higher is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### 2. Install Tesseract OCR
Tesseract is required for OCR functionality. Follow these steps to install it:

- **For Windows**:
  1. Download the Tesseract installer from [Tesseract's official GitHub page](https://github.com/UB-Mannheim/tesseract/wiki).
  2. Run the installer and add Tesseract to the system PATH.
  
- **For Linux**:
  ```bash
  sudo apt update
  sudo apt install tesseract-ocr
  ```

- **For macOS**:
  ```bash
  brew install tesseract
  ```

### 3. Install Dependencies
Clone the repository and install the required dependencies using `requirements.txt`:

```bash
git clone https://github.com/RajaMuhammadHammad/AI-MegaSuite.git
cd AI-MegaSuite
pip install -r requirements.txt
```

### 4. Run the Application
Launch the Streamlit app with the following command:

```bash
streamlit run app.py
```

Once the app is running, open your browser and navigate to [http://localhost:8501](http://localhost:8501).

---

## 📄 Requirements File (`requirements.txt`)

The `requirements.txt` file includes all the dependencies required for the project. Here are some of the key libraries used:

```
streamlit
pytesseract
opencv-python
gtts
SpeechRecognition
fpdf
transformers
```

Use the following command to install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Developed By

AI-MegaSuite is developed by **Raja Muhammad Hammad**.  
Feel free to reach out for feedback or collaboration!  

---
