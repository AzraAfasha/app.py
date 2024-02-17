import streamlit as st
import pandas as pd
import seaborn as sns

# Load cleaned data
df_day = pd.read_csv('cleaned_day.csv')
df_hour = pd.read_csv('cleaned_hour.csv')

# Visualisasi Jumlah Peminjaman Sepeda Harian berdasarkan musim
plt.figure(figsize=(10, 6))
df_day.boxplot(column='cnt', by='season')
plt.title('Jumlah Peminjaman Sepeda Harian berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Peminjaman')
st.pyplot(plt)

# Visualisasi Jumlah Peminjaman Sepeda per Jam berdasarkan waktu (pagi, siang, malam)
df_hour['time_label'] = pd.cut(df_hour['hr'], bins=[0, 6, 12, 18, 24], labels=['Malam', 'Pagi', 'Siang', 'Malam'], ordered=False)
plt.figure(figsize=(10, 6))
df_hour.boxplot(column='cnt', by='time_label')
plt.title('Jumlah Peminjaman Sepeda per Jam berdasarkan Waktu')
plt.xlabel('Waktu')
plt.ylabel('Jumlah Peminjaman')
st.pyplot(plt)

# Distribusi Jumlah Peminjaman Sepeda per Jam
plt.figure(figsize=(12, 6))
plt.hist(df_hour['cnt'], bins=30, alpha=0.7)
plt.title('Distribusi Jumlah Peminjaman Sepeda per Jam')
plt.xlabel('Jumlah Peminjaman')
plt.ylabel('Frekuensi')
st.pyplot(plt)
