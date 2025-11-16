import streamlit as st
import sys
import os
import nltk

@st.cache_resource
def download_nltk_packages():
    
    packages = ['stopwords', 'punkt', 'punkt_tab']
    for package in packages:
        try:
            nltk.data.find(f'corpora/{package}' if package == 'stopwords' else f'tokenizers/{package}')
        except LookupError:
            st.info(f"Mengunduh paket NLTK yang diperlukan: {package}...")
            nltk.download(package)

download_nltk_packages()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.search import SearchEngine

#Config Halaman
st.set_page_config(
    page_title="Mesin Pencari Hewan Langka",
    page_icon="🔎"
)

#Inisialisasi Engine
@st.cache_resource
def initialize_engine():
    engine = SearchEngine(data_path='data/')
    return engine

engine = initialize_engine()

#Tampilan Antarmuka (UI)
st.title("🔎 Hewan Langka Indonesia")
st.markdown(f"Dibangun berdasarkan model **Boolean** dan **Vector Space Model (VSM)**. Total **{len(engine.documents)}** dokumen dalam korpus.")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    model_choice = st.radio(
        "Pilih Model Pencarian:",
        ('Vector Space Model', 'Boolean Model'),
        horizontal=True,
        key='model_selection'
    )

with col2:
    if model_choice == 'Vector Space Model':
        k_options = list(range(1, len(engine.documents) + 1))
        top_k = st.selectbox(
            "Jumlah Hasil Teratas (Top-K):",
            options=k_options,
            index=2 
        )

query = st.text_input(
    "Masukkan query Anda di sini...",
    placeholder="Contoh VSM: hewan pemakan buah dari sumatra | Contoh Boolean: badak AND jawa"
)

if st.button("Cari Dokumen", type="primary"):
    if query:
        st.header("Hasil Pencarian")
        st.markdown("---")
        
        #VSM
        if model_choice == 'Vector Space Model':
            results = engine.search(query, model='vsm', k=top_k)
            if not results or results[0][1] == 0:
                st.warning("Tidak ada dokumen yang relevan ditemukan.")
            else:
                st.success(f"Menampilkan {len(results)} hasil teratas untuk '{query}'")
                for doc_name, score in results:
                    with st.container(border=True):
                        st.subheader(f"📄 {doc_name}")
                        st.markdown(f"**Skor Relevansi (Cosine Similarity):** `{score:.4f}`")
                        
                        full_text = engine.documents[doc_name]
                        snippet = full_text.replace('\n', ' ')[:250]
                        st.write(snippet + "...")
                        
                        with st.expander("Baca Selengkapnya..."):
                            st.write(full_text)

        #Boolean
        elif model_choice == 'Boolean Model':
            results = engine.search(query, model='boolean')
            if not results:
                st.warning("Tidak ada dokumen yang cocok dengan query Anda.")
            else:
                st.success(f"Ditemukan {len(results)} dokumen untuk '{query}'")
                for doc_name in results:
                    with st.container(border=True):
                        st.subheader(f"📄 {doc_name}")
                        
                        full_text = engine.documents[doc_name]
                        snippet = full_text.replace('\n', ' ')[:250]
                        st.write(snippet + "...")

                        with st.expander("Baca Selengkapnya..."):
                            st.write(full_text)
    else:
        st.warning("Mohon masukkan query untuk memulai pencarian.")