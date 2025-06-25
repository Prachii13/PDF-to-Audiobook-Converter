import pyttsx3
import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
    return text

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def main():
    print("📘 PDF to Audiobook Converter")
    file_path = input("Enter PDF file path (e.g., sample.pdf): ")
    try:
        text = read_pdf(file_path)
        print("✅ Text extracted. Starting audio...")
        text_to_speech(text)
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
