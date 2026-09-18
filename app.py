import streamlit as st
from PIL import Image
from src.extractor import extract_receipt_data
from src.calculator import calculate_split

st.set_page_config(page_title="Smart Split Bill", layout="wide")

st.title("🧾 Smart Split Bill PoC")
st.write("Upload nota belanja, pilih partisipan, dan hitung pembagian tagihan secara otomatis.")

uploaded_file = st.file_uploader("Unggah Struk Belanja (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    col1, col2 = st.columns([1, 1])
    
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption="Nota Pembelian", use_container_width=True)

    with col2:
        if st.button("Proses Struk dengan AI"):
            with st.spinner("Mengekstrak data transaksi..."):
                try:
                    st.session_state.receipt_data = extract_receipt_data(image)
                    st.success("Ekstraksi Berhasil!")
                except Exception as e:
                    st.error(f"Gagal mengekstrak struk: {e}")

if "receipt_data" in st.session_state:
    data = st.session_state.receipt_data
    st.divider()
    st.subheader("Detail Transaksi")
    
    # Ringkasan nota
    st.write(f"**Subtotal:** Rp {data.subtotal:,.2f}")
    st.write(f"**Pajak & Service Charge:** Rp {(data.tax + data.service_charge + data.other_fees):,.2f}")
    st.write(f"**Total Nota:** Rp {data.total_amount:,.2f}")

    # Input nama partisipan
    st.divider()
    participants_input = st.text_input("Masukkan nama partisipan (pisahkan dengan koma):", "Budi, Andi, Cici")
    participants = [p.strip() for p in participants_input.split(",") if p.strip()]

    if participants:
        st.subheader("Pembagian Item")
        item_assignments = {}
        
        for idx, item in enumerate(data.items):
            selected = st.multiselect(
                f"{item.name} ({item.quantity}x @ Rp {item.price_per_item:,.2f} = Rp {item.total_price:,.2f})",
                options=participants,
                key=f"item_{idx}"
            )
            item_assignments[idx] = selected

        if st.button("Hitung Split Bill"):
            totals = calculate_split(data, item_assignments)
            st.divider()
            st.subheader("Hasil Pembayaran per Orang")
            
            grand_total_calculated = sum(totals.values())
            
            for person, amount in totals.items():
                st.write(f"- **{person}**: Rp {amount:,.2f}")
                
            st.info(f"Total Keseluruhan Hasil Split: **Rp {grand_total_calculated:,.2f}** (Total Nota: Rp {data.total_amount:,.2f})")