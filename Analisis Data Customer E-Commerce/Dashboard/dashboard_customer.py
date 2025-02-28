import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Load data
df = pd.read_csv('all_dataset.csv', parse_dates=['order_purchase_timestamp', 'order_delivered_customer_date', 'order_estimated_delivery_date'])

# Convert date column
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

# Set page title
st.title("Dashboard Analisis Data Pelanggan")

# Sidebar navigation
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("3d_img.jpg")
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("Pilih Analisis:", ["Pendapatan Berdasarkan Lokasi", "Penjualan Berdasarkan Kategori", "Keterlambatan Pengiriman", "Analisis RFM"])

# Function untuk analisis

def sales_over_time(df):
    df['month'] = df['order_purchase_timestamp'].dt.to_period('M')
    sales_by_month = df.groupby('month')['order_id'].count().reset_index()
    sales_by_month['month'] = sales_by_month['month'].astype(str)
    return sales_by_month

def revenue_loc(df):
    revenue_by_location = df.groupby('customer_city')['price'].sum().reset_index().sort_values(by='price', ascending=False).head(10)
    return revenue_by_location

def revenue_state(df):
    revenue_by_state = df.groupby('customer_state')['price'].sum().reset_index().sort_values(by='price', ascending=False).head(10)
    return revenue_by_state

def sales_cat(df):
    sales_by_category = df.groupby('product_category_name')['price'].sum().reset_index().sort_values(by='price', ascending=False).head(10)
    return sales_by_category

def sales_month(df):
    df['month'] = df['order_purchase_timestamp'].dt.to_period('M')
    sales_by_month = df.groupby('month')['order_id'].count().reset_index()
    return sales_by_month

def late_deliver_time(df):
    df["actual_delivery_time"] = (df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]).dt.days
    late_deliver = df.groupby("customer_city")["actual_delivery_time"].mean().round(2).reset_index(name="avg_delay_days").head()
    return late_deliver

def create_rfm(df):
    data_rfm = df[df['order_status'] == 'delivered']
    rfm_df = data_rfm.groupby(by='customer_unique_id', as_index=False).agg({
        'order_purchase_timestamp': 'max',
        'order_id': 'count',
        'price': 'sum',
    })
    rfm_df.columns = ['customer_id', "max_order", "frequency", "monetary"]
    rfm_df['max_order'] = rfm_df['max_order'].dt.date
    recent_date = df['order_purchase_timestamp'].dropna().dt.date.max()
    rfm_df['recency'] = rfm_df['max_order'].apply(lambda x: (recent_date - x).days)
    rfm_df.drop('max_order', axis=1, inplace=True)
    return rfm_df


# Display selected analysis
if menu == "Pendapatan Berdasarkan Lokasi":
    st.header("Pendapatan Berdasarkan Kota dan Provinsi")
    col1, col2 = st.columns(2)
    with col1:
        revenue_city = revenue_loc(df)
        fig, ax = plt.subplots(figsize=(18, 12))
        sns.barplot(y=revenue_city['customer_city'], x=revenue_city['price'], ax=ax, palette='coolwarm')
        plt.xlabel('Total Revenue ($)', fontsize=30)
        plt.ylabel('City', fontsize=30)
        plt.title('Top 10 Cities by Revenue', loc="center", fontsize=50)
        plt.tick_params(axis='x', labelsize=35)
        plt.tick_params(axis='y', labelsize=35)
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        st.pyplot(fig)
    with col2:
        revenue_province = revenue_state(df)
        fig, ax = plt.subplots(figsize=(20, 10))
        sns.barplot(y=revenue_province['price'], x=revenue_province['customer_state'], ax=ax, palette='coolwarm')
        plt.xlabel('State', fontsize=30)
        plt.ylabel('Frequency', fontsize=30)
        plt.title('Top 10 States by Revenue', loc="center", fontsize=50)
        plt.tick_params(axis='x', labelsize=35)
        plt.tick_params(axis='y', labelsize=35)
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        st.pyplot(fig)
    
    # Visualisasi Sales Over Time
    sales_data = sales_over_time(df)
    st.header("Sales Trend Over Time")
    fig, ax = plt.subplots(figsize=(18, 12))
    ax.plot(sales_data['month'], sales_data['order_id'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Month', fontsize=30)
    ax.set_ylabel('Number of Orders', fontsize=30)
    ax.set_title('Monthly Sales Trend', loc="center", fontsize=50)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xticks(rotation=45)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    st.pyplot(fig)

elif menu == "Penjualan Berdasarkan Kategori":
    st.header("Total Penjualan per Kategori Produk")
    sales_category = sales_cat(df)
    # Visualisasi Best and Worst Performing Product
    st.header("Best and Worst Performing Products")
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))

    colors = ["#72BCD4"] * 3 + ["#D3D3D3"] * 7  # Warna untuk membedakan top 3 terbaik
    
    sns.barplot(x='price', y='product_category_name', data=sales_category.head(10), orient='h', palette=colors, ax=ax[0])
    ax[0].set_title("Best Performing Products", loc="center", fontsize=18)
    ax[0].set_ylabel(None)
    ax[0].set_xlabel("Total Sales (AUD)", fontsize=14)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.barplot(x='price', y='product_category_name', data=sales_category.sort_values(by='price', ascending=True).head(10), orient='h', palette=colors, ax=ax[1])
    ax[1].set_title("Worst Performing Products", loc="center", fontsize=18)
    ax[1].set_ylabel(None)
    ax[1].set_xlabel("Total Sales (AUD)", fontsize=14)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position('right')
    ax[1].yaxis.tick_right()
    ax[1].tick_params(axis='y', labelsize=12)

    plt.suptitle("Best and Worst Performing Products", fontsize=22)
    st.pyplot(fig)
    
    # Visualisasi Tren Penjualan dari Waktu ke Waktu
    st.header("Tren Penjualan dari Waktu ke Waktu")

    sales_by_month = sales_over_time(df)
    fig, ax = plt.subplots(figsize=(18, 10))
    ax.plot(sales_by_month['month'], sales_by_month['order_id'], marker='o', linestyle='-', color='b')
    ax.set_xlabel("Bulan", fontsize=20)
    ax.set_ylabel("Total Penjualan", fontsize=20)
    ax.set_title("Tren Penjualan dari Waktu ke Waktu", fontsize=25)
    plt.xticks(rotation=45, fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig)

elif menu == "Keterlambatan Pengiriman":
    st.header("Rata-rata Keterlambatan Pengiriman")
    delay_data = late_deliver_time(df)
    fig, ax = plt.subplots()
    sns.barplot(y=delay_data['customer_city'], x=delay_data['avg_delay_days'], ax=ax)
    ax.set_xlabel("Days", fontsize=15)
    ax.set_ylabel("City", fontsize=15)
    st.pyplot(fig)
    
    st.header("Distribusi Skor Ulasan Pelanggan")

    # Hitung frekuensi skor ulasan
    review_score_counts = df['review_score'].value_counts().sort_index()

    # Buat pie chart
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    ax.pie(review_score_counts, labels=review_score_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title('Distribusi Skor Ulasan Pelanggan', fontsize=16)
    plt.axis('equal')  # Agar pie chart berbentuk lingkaran sempurna

    # Tampilkan plot di Streamlit
    st.pyplot(fig)

elif menu == "Analisis RFM":
    st.header("Analisis RFM")
    rfm_df = create_rfm(df)
    
    # Menampilkan Rata-Rata RFM
    col1, col2, col3 = st.columns(3)

    with col1:
        avg_recency = round(rfm_df['recency'].mean(), 1)
        st.metric("Average Recency (days)", value=avg_recency)

    with col2:
        avg_frequency = round(rfm_df['frequency'].mean(), 2)
        st.metric("Average Frequency", value=avg_frequency)

    with col3:
        avg_monetary = format_currency(rfm_df['monetary'].mean(), "AUD", locale='es_CO') 
        st.metric("Average Monetary", value=avg_monetary)
    
    fig, axes = plt.subplots(1, 3, figsize=(20, 10))
    sns.histplot(rfm_df['recency'], bins=20, kde=True, ax=axes[0], color='b')
    axes[0].set_title("Recency Distribution")
    sns.histplot(rfm_df['frequency'], bins=20, kde=True, ax=axes[1], color='g')
    axes[1].set_title("Frequency Distribution")
    sns.histplot(rfm_df['monetary'], bins=20, kde=True, ax=axes[2], color='r')
    axes[2].set_title("Monetary Distribution")
    st.pyplot(fig)

    

st.caption('Copyright (C) Novrian Pratama 2025')

