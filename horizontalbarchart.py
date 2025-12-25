import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

# JUDUL
st.title("Praktikum 7 Visualisasi Data")
st.subheader("Horizontal Bar Chart & Stacked Horizontal Bar Chart")

# DATASET (FIX)
brands = ['Samsung', 'Iphone', 'Vivo', 'Oppo']
sales_2023 = [500, 700, 300, 400]
sales_2024 = [550, 750, 350, 450]
sales_2025 = [600, 800, 400, 500]

y = np.arange(len(brands))

# PILIH KATEGORI
kategori = st.selectbox(
    "Pilih kategori visualisasi",
    ['Basic Chart', 'Kustomisasi Grafik', 'Multiple Chart']
)

# BASIC CHART
if kategori == "Basic Chart":
    st.subheader("Basic Chart")

    # Basic Horizontal
    fig1, ax1 = plt.subplots()
    ax1.barh(y, sales_2023)
    ax1.set_yticks(y)
    ax1.set_yticklabels(brands)
    ax1.set_title("Horizontal Bar Chart - 2023")
    st.pyplot(fig1)

    # Basic Stacked
    fig2, ax2 = plt.subplots()
    ax2.barh(y, sales_2023, label='2023')
    ax2.barh(y, sales_2024, left=sales_2023, label='2024')
    ax2.set_yticks(y)
    ax2.set_yticklabels(brands)
    ax2.set_title("Stacked Horizontal Bar Chart")
    ax2.legend()
    st.pyplot(fig2)

# KUSTOMISASI GRAFIK
elif kategori == "Kustomisasi Grafik":
    st.subheader("Kustomisasi Grafik")

    colors = ['blue', 'green', 'orange', 'red']

    # Custom Horizontal
    fig3, ax3 = plt.subplots()
    ax3.barh(y, sales_2023, color=colors)
    for i, v in enumerate(sales_2023):
        ax3.text(v + 10, i, str(v), va='center')
    ax3.set_yticks(y)
    ax3.set_yticklabels(brands)
    ax3.set_title("Customized Horizontal Bar Chart")
    st.pyplot(fig3)

    # Custom Stacked
    fig4, ax4 = plt.subplots()
    ax4.barh(y, sales_2023, label='2023')
    ax4.barh(y, sales_2024, left=sales_2023, label='2024')
    ax4.set_yticks(y)
    ax4.set_yticklabels(brands)
    ax4.set_title("Customized Stacked Horizontal Bar Chart")
    ax4.grid(axis='x', linestyle='--', alpha=0.5)
    ax4.legend()
    st.pyplot(fig4)

# MULTIPLE CHART (2023–2025)
elif kategori == "Multiple Chart":
    st.subheader("Multiple Chart (2023–2025)")

    bar_h = 0.25

    # Multiple Horizontal
    fig5, ax5 = plt.subplots()
    ax5.barh(y - bar_h, sales_2023, height=bar_h, label='2023')
    ax5.barh(y,         sales_2024, height=bar_h, label='2024')

    ax5.set_yticks(y)
    ax5.set_yticklabels(brands)
    ax5.set_title("Multiple Horizontal Bar Chart")
    ax5.legend()
    st.pyplot(fig5)

    # Stacked Horizontal
    fig6, ax6 = plt.subplots()
    ax6.barh(y, sales_2023, label='2023')
    ax6.barh(y, sales_2024, left=sales_2023, label='2024')
    ax6.barh(
        y,
        sales_2025,
        left=np.array(sales_2023) + np.array(sales_2024),
        label='2025'
    )

    ax6.set_yticks(y)
    ax6.set_yticklabels(brands)
    ax6.set_title("Stacked Horizontal Bar Chart (2023–2025)")
    ax6.legend()
    st.pyplot(fig6)
