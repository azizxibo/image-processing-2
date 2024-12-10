import streamlit as st
from rembg import remove
from PIL import Image
import io

# Judul aplikasi
st.title("Aplikasi Penghapusan Background Gambar")

# Instruksi
st.write("Unggah gambar, dan backgroundnya akan dihapus. Anda dapat mengunduh gambar hasilnya.")

# Mengunggah gambar
uploaded_file = st.file_uploader("Unggah gambar Anda di sini:", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Menampilkan gambar asli
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar Asli", use_column_width=True)

    # Tombol untuk menghapus background
    if st.button("Hapus Background"):
        with st.spinner("Memproses gambar..."):
            # Proses penghapusan background
            img_no_bg = remove(image.tobytes())
            image_no_bg = Image.open(io.BytesIO(img_no_bg))

            # Menampilkan gambar tanpa background
            st.image(image_no_bg, caption="Gambar Tanpa Background", use_column_width=True)

            # Membuat file download
            buf = io.BytesIO()
            image_no_bg.save(buf, format="PNG")
            buf.seek(0)

            # Tombol untuk mengunduh
            st.download_button(
                label="Unduh Gambar Tanpa Background",
                data=buf,
                file_name="gambar_tanpa_background.png",
                mime="image/png"
            )
