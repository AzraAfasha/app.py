import streamlit as st
import pandas as pd
import seaborn as sns

# Load cleaned data
df_day = pd.read_csv('cleaned_day.csv')
df_hour = pd.read_csv('cleaned_hour.csv')

# Visualisasi Jumlah Peminjaman Sepeda Harian berdasarkan musim
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_day, x='season', y='cnt', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda Harian berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Visualisasi Jumlah Peminjaman Sepeda per Jam berdasarkan waktu (pagi, siang, malam)
df_hour['time_label'] = pd.cut(df_hour['hr'], bins=[0, 6, 12, 18, 24], labels=['Malam', 'Pagi', 'Siang', 'Malam'], ordered=False)
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df_hour, x='time_label', y='cnt', ax=ax)
ax.set_title('Jumlah Peminjaman Sepeda per Jam berdasarkan Waktu')
ax.set_xlabel('Waktu')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Distribusi Jumlah Peminjaman Sepeda per Jam
fig, ax = plt.subplots(figsize=(12, 6))
sns.histplot(df_hour['cnt'], bins=30, alpha=0.7, ax=ax)
ax.set_title('Distribusi Jumlah Peminjaman Sepeda per Jam')
ax.set_xlabel('Jumlah Peminjaman')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)
