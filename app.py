import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df_day = pd.read_csv("day.csv")

# Memilih fitur-fitur yang relevan untuk prediksi
features = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed']

# Memisahkan fitur dan target variable
X = df_day[features]
y = df_day['cnt']

# Memisahkan data menjadi data pelatihan dan data pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat transformer untuk kolom kategorikal
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first'), ['season', 'mnth', 'weekday', 'weathersit'])
    ],
    remainder='passthrough'
)

# Melakukan transformasi pada data pelatihan dan pengujian
X_train_encoded = preprocessor.fit_transform(X_train)
X_test_encoded = preprocessor.transform(X_test)

# Membuat model regresi linier
model_encoded = LinearRegression()

# Melatih model pada data pelatihan yang telah diencode
model_encoded.fit(X_train_encoded, y_train)

# Melakukan prediksi pada data pengujian yang telah diencode
y_pred_encoded = model_encoded.predict(X_test_encoded)

# Evaluasi kinerja model
mse_encoded = mean_squared_error(y_test, y_pred_encoded)
r2_encoded = r2_score(y_test, y_pred_encoded)

# Menampilkan visualisasi
st.title("Aplikasi Prediksi Jumlah Peminjaman Sepeda")

# Visualisasi hasil regresi
st.subheader("Visualisasi Hasil Regresi")
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred_encoded)
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=3)
ax.set_xlabel('Aktual')
ax.set_ylabel('Prediksi')
st.pyplot(fig)

# Menampilkan metrik evaluasi
st.subheader("Metrik Evaluasi")
st.write(f'Mean Squared Error (Encoded): {mse_encoded}')
st.write(f'R-squared (Encoded): {r2_encoded}')

# Menampilkan dataset
st.subheader("Dataset")
st.write(df_day)

# Menampilkan ringkasan statistik dataset
st.subheader("Ringkasan Statistik Dataset")
st.write(df_day.describe())

# Menjalankan aplikasi
if __name__ == '__main__':
    st.run_app()
