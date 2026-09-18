import os
from dotenv import load_dotenv
from google import genai

# Load API key dari file .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ API Key tidak ditemukan! Cek kembali file .env kamu.")
else:
    print("🔑 API Key ditemukan, mencoba koneksi ke Gemini...")
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents="Halo Gemini, respons 'Koneksi Berhasil' jika kamu bisa membaca pesan ini."
        )
        print("✅ KONEKSI BERHASIL!")
        print(f"Jawaban dari Gemini: {response.text}")
    except Exception as e:
        print("❌ KONEKSI GAGAL!")
        print(f"Error detail: {e}")
