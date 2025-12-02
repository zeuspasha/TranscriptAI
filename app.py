from flask import Flask, render_template, request, send_file
import os
import fitz  # PyMuPDF yüklenmesi gereken
import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))
API_KEY = "<---- API YAZ BURAYA"

def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def openai_metni_isle(metin):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Bu metni düzenli şekilde çıkar. Başlıkları koru, tabloları liste yap, okunaklı hale getir (NOT: Ders akts, harf notu vb. tablo oluştur  ve EKSİKSİZ YAZ HERŞEYİ):\n\n{metin}"}
        ],
        "max_tokens": 2000
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        return "HATA"
    return response.json()["choices"][0]["message"]["content"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "pdf_file" not in request.files:
        return "PDF dosyası seçilmedi."
    
    file = request.files["pdf_file"]
    if file.filename == "":
        return "Dosya seçilmedi."
    
    upload_folder = os.path.join(BASE_DIR, "uploads")
    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    metin = pdf_to_text(file_path)
    sonuc = openai_metni_isle(metin)

    if sonuc != "HATA":
        with open(os.path.join(BASE_DIR, "sonuc.txt"), "w", encoding="utf-8") as f:
            f.write(sonuc)
        return render_template("sonuc.html", sonuc=sonuc)
    else:
        return "Bir hata oluştu"

@app.route("/indir")
def indir():
    dosya_yolu = os.path.join(BASE_DIR, "sonuc.txt")
    if os.path.exists(dosya_yolu):
        return send_file(dosya_yolu, as_attachment=True)
    else:
        return "Dosya bulunamadı."

if __name__ == "__main__":
    app.run(debug=True)
