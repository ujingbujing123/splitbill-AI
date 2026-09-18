import os
import time
from typing import List
from PIL import Image
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

class BillItem(BaseModel):
    name: str = Field(description="Nama produk/item belanja")
    quantity: int = Field(description="Jumlah item yang dibeli")
    price_per_item: float = Field(description="Harga per satu item")
    total_price: float = Field(description="Total harga untuk item ini (quantity * price_per_item)")

class ReceiptData(BaseModel):
    items: List[BillItem]
    subtotal: float = Field(description="Jumlah total semua item sebelum pajak/service")
    tax: float = Field(default=0.0, description="Biaya pajak (PPN/VAT)")
    service_charge: float = Field(default=0.0, description="Biaya layanan/service charge")
    other_fees: float = Field(default=0.0, description="Biaya tambahan lainnya jika ada")
    total_amount: float = Field(description="Total akhir bill yang harus dibayar")

def extract_receipt_data(image: Image.Image) -> ReceiptData:
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    prompt = (
        "Ekstrak seluruh informasi transaksi dari gambar nota/struk belanja ini. "
        "Pastikan detail per item, subtotal, pajak, biaya service, dan grand total terbaca dengan akurat."
    )

    model_name = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")
    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=[image, prompt],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ReceiptData,
                    temperature=0.1,
                ),
            )
            return ReceiptData.model_validate_json(response.text)
        except Exception as e:
            error_str = str(e)
            # Jika server busy / 503, tunggu jeda beberapa detik lalu coba lagi
            if ("503" in error_str or "UNAVAILABLE" in error_str) and attempt < max_retries - 1:
                time.sleep(2 * (attempt + 1))  # Tunggu 2s, lalu 4s
                continue
            raise e