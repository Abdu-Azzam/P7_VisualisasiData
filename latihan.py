import  matplotlib as st
import streamlit as st
import numpy as np 

#judul
st.title("Praktikum 7 Viusalisasi Data")
st.subheader("Horizontal Bar Chart & Stacked Horizontal Bar Chart")

st.markdown("""
-Abdu Azzam Alariz
-Nurul Aeman
""")

#dataset
brand = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300,280]
sales_2024 = [380, 450, 320, 300]

#atur posisi Y
y = np.arange(len(brands))
bar_width = 0.4

#filter kategori
kategori = set.selectbox(
    "Pilih kategori visualisasi"
    ['Basic Chart', 'Kustomisasi Grafik', 'Multiple Chart']
)

if kategori == "Basic Chart":
    st.subheader("Horizontal Bar Chart Sederhana")
    fig1, ax1, = plt.subplots()

ax1.set_yticks(y)
ax1.set_yticklabels(y)
ax1.set_title('Horizontal Bar Chart - 2023')
ax1.set_xlabel('Jumlah Penjualan')
ax1.set_ylabel('Merk')
ax1.barh(y, sales_2023, color='skyblue')
st.pyplot(fig1)

st.subheader("Stacked Horizontal Bar Chart Sederhana")
fig2, ax2, = plt.subplots()
ax2.set_yticks(y)
ax2.set_yticklabels(y)
ax2.set_title('Stacked Horizontal Bar Chart - 2023')
ax2.set_xlabel('Jumlah Penjualan')
ax2.set_ylabel('Merk')
ax2.barh(y, sales_2023, color='skyblue', label='2023')
ax2.legend()
st.pyplot(fig2)


#Kustomisasi
elif kategori == "Kustomisasi Grafik" :
    st.subheader('Kustomisasi Horizontal Bar Chart')
    fig3, ax3, = plt.subplots()
    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_title('Kustomisasi Horizontal Bar Chart - 2023')
    ax3.set_xlabel('Jumlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.barh(y, sales_2023, color='lightblue', edgecolor='black')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)

#label nilai
for i, v in enumerate(sales_2023):

