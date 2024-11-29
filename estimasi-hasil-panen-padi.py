import pickle
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open('estimasi-hasil-panen-padi.sav', 'rb'))

# App Title
st.title('Estimasi Hasil Panen Padi di Sumatera')

# Deskripsi
st.subheader('Deskripsi')
st.write("""
Pulau Sumatera mempunyai lebih dari 50 persen lahan pertanian setiap provinsinya dengan komoditas utama padi. 
Hasil pertanian sangat rentan terhadap perubahan iklim yang memengaruhi pola tanam dan hasil produksi. 
Aplikasi ini memprediksi hasil panen padi berdasarkan data cuaca dan luas lahan.
""")

# Sumber Dataset
st.subheader('Sumber Dataset')
st.write('Dataset berasal dari Kaggle: [Dataset Tanaman Padi Sumatera](https://www.kaggle.com/datasets/ardikasatria/datasettanamanpadisumatera)')

# Display Static Dataset Table
st.write('Tabel Dataset:')
static_dataset_url = "https://www.kaggleusercontent.com/datasets/ardikasatria/datasettanamanpadisumatera/padi.csv"
try:
    dataset = pd.read_csv("Data_Tanaman_Padi_Sumatera_version_1.csv")
    st.dataframe(dataset.head(10))
except:
    st.error("Gagal memuat dataset. Silakan pastikan URL dataset valid.")

# Nama Pembuat
st.subheader('Nama Pembuat')
st.write('Ica Chintyasari')

# Input Data
st.subheader('Input Data')
Luas_Panen = st.number_input('Luas Pertanian (hektar)', min_value=0.0)
Curah_hujan = st.number_input('Jumlah rata-rata curah hujan dalam setahun (milimeter)', min_value=0.0)
Kelembapan = st.number_input('Tingkat kelembaban rata-rata dalam setahun (persentase)', min_value=0.0)
Suhu_rata_rata = st.number_input('Derajat suhu rata-rata dalam setahun (celsius)', min_value=0.0)

# Prediction
predict = ''
if st.button('Estimasi Hasil Panen'):
    predict = model.predict(
        [[Luas_Panen, Curah_hujan, Kelembapan, Suhu_rata_rata]]
    )
    st.write('Estimasi Hasil Panen Padi (ton): ', round(predict[0], 2))

# Visualisasi Data (Optional)
uploaded_file = st.file_uploader("Upload file dataset (.csv) untuk visualisasi tambahan", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Visualisasi Data
    st.subheader('Visualisasi Data')
    
    # Barplot Tahun vs Produksi
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='Tahun', y='Produksi', ax=ax)
    plt.title('Produksi Padi per Tahun')
    plt.xticks(rotation=90)
    st.pyplot(fig)
