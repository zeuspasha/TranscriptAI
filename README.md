
<!--  Dil Seçici  -->
<p align="right">
  <a href="#-transcriptai---smart-transcript-editor-using-ocr--gpt">🇬🇧 English</a> |
  <a href="#-transcriptai---ocr-ve-gpt-ile-akıllı-transkript-düzenleyici">🇹🇷 Türkçe</a>
</p>

# 🎓 TranscriptAI - Smart Transcript Editor using OCR & GPT

TranscriptAI is a lightweight, intelligent, and efficient tool that reads your university transcripts or any academic PDF using Python and converts them into clean, readable text with OpenAI GPT. Transcripts are no longer just documents – they become meaningful and analyzable data.

![image](https://github.com/user-attachments/assets/ab0a7487-1bad-469d-af10-f4c937eb03ee)

---

## ✨ Features

- 📄 Text extraction from PDFs – High-accuracy OCR using PyMuPDF (fitz)  
- 🤖 AI-powered formatting – Enhanced with GPT-3.5 for structured headings, lists, and readable table formatting  
- 💾 Auto save – Output saved to `sonuc.txt` automatically  
- 🔒 User-specific API key – Safe and personalized usage

---

## 🚀 Required Libraries

```python
import fitz  # PyMuPDF --> install with "pip install PyMuPDF"
import requests
import json
import os
```

To use OpenAI GPT, generate an OpenAI API key and update this line in the `.py` file:

```python
API_KEY = "sk-..."  # ← Paste your own API key here
```

⚠️ Never share your API key publicly or on GitHub.

Place your `transkript.pdf` file in the project directory and run the script from the terminal.

---

## 🤝 Contribute

This is an open-source project and contributions are welcome. You can suggest new features, report bugs, or submit pull requests.

---

## 🧠 Why TranscriptAI?

Because documents should be more than just text – they should be structured and meaningful.  
TranscriptAI does that for you.

📫 Developer: [Pasha]  
📅 Version: 1.0  
🔗 License: MIT

---

# 🎓 TranscriptAI - OCR ve GPT ile Akıllı Transkript Düzenleyici

TranscriptAI, üniversite transkriptlerinizi ya da herhangi bir akademik PDF belgesini Python kullanarak okuyup, OpenAI GPT ile düzenli ve okunabilir metne çeviren hafif, akıllı ve etkili bir araçtır. Transkriptler artık sadece bir belge değil, anlamlı ve analiz edilebilir bir yapıya kavuşuyor.

---

## ✨ Özellikler

- 📄 PDF’den metin çıkarımı – PyMuPDF (fitz) ile yüksek doğrulukta OCR işlemi  
- 🤖 Yapay Zeka destekli biçimlendirme – OpenAI GPT-3.5 ile başlıkları koruyan, listeler oluşturan, tabloyu metne döken düzenleme  
- 💾 Otomatik kayıt – Çıktılar `sonuc.txt` olarak diske kaydedilir  
- 🔒 Kullanıcıya özel API anahtarı – Güvenli ve kişiselleştirilmiş kullanım

---

## 🚀 Yüklemen Gereken Kütüphaneler

```python
import fitz  # yani --> PyMuPDF "pip install PyMuPDF" <--
import requests
import json
import os
```

OpenAI GPT’yi kullanabilmek için OpenAI API Key oluşturun ve `.py` dosyasında şu satırı güncelleyin:

```python
API_KEY = "sk-..."  # ← kendi API anahtarınızı buraya yapıştırın
```

⚠️ API anahtarınızı GitHub'da veya herkese açık ortamlarda asla paylaşmayın.

`transkript.pdf` adlı dosyanızı proje dizinine koyun. Terminalden aşağıdaki komutu çalıştırın.

---

## 🤝 Katkı Sağla

Bu proje açık kaynaklıdır ve katkıya açıktır. Yeni özellik önerileri, hata bildirimleri ya da doğrudan pull request’ler gönderebilirsiniz.

---

## 🧠 Neden TranscriptAI?

Çünkü bir belge sadece yazıdan ibaret olmamalı. Bilgi düzenli olmalı. Anlam ön planda olmalı.  
TranscriptAI, bunu sizin için yapar.

📫 Geliştirici: [Pasha]  
📅 Sürüm: 1.0  
🔗 Lisans: MIT
