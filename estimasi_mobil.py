import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Load the data
df = pd.read_csv('toyota.csv')

#st.title('Estimasi Harga Mobil Toyota Bekas di Wilayah Inggris')
 
# Menambahkan judul yang menarik
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🚗 Estimasi Harga Mobil Toyota Bekas di Wilayah Inggris</h1>", unsafe_allow_html=True)

# Filter by year

unique_years = sorted(df['year'].unique())
selected_year = st.selectbox('Pilih Tahun:', unique_years)

unique_mileage = sorted(df['mileage'].unique())
selected_mileage = st.selectbox('Pilih KM Mobil:', unique_mileage)

unique_tax = sorted(df['tax'].unique())
selected_tax = st.selectbox('Pilih Pajak Mobil:', unique_tax)

unique_mpg = sorted(df['mpg'].unique())
selected_mpg = st.selectbox('Pilih Konsumsi BBM:', unique_mpg)

unique_engine = sorted(df['engineSize'].unique())
selected_engine = st.selectbox('Pilih Konsumsi BBM:', unique_engine)


# Display filtered data
filtered_data = df[df['year']==selected_year]

# Additional option to filter by model
selected_model = st.sidebar.multiselect('Select Model(s)', sorted(df['model'].unique()), default=df['model'].unique())
filtered_data_by_model = filtered_data[filtered_data['model'].isin(selected_model)]

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[selected_year, selected_mileage, selected_tax, selected_mpg, selected_engine]]
    )
    st.write ('Estimasi Harga Mobil Bekas dalam Ponds :', predict)
    st.write ('Estimasi Harga Mobil Bekas dalam IDR :', predict*19000)
    st.write (f"Menampilkan Data Untuk Tahun  {selected_year}")
    st.dataframe(filtered_data)
    st.write(f"Menampilkan Data Untuk Tahun  {selected_year} and selected model(s)")
    st.dataframe(filtered_data_by_model)