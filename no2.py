import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


order_items = pd.read_csv('order_items_dataset.csv')
order_payments = pd.read_csv('order_payments_dataset.csv')
order_reviews = pd.read_csv('order_reviews_dataset.csv')
orders = pd.read_csv('orders_dataset.csv')
products = pd.read_csv('products_dataset.csv')
product_translation = pd.read_csv('product_category_name_translation.csv')
sellers = pd.read_csv('sellers_dataset.csv')
customers = pd.read_csv('customers_dataset.csv')
geolocation = pd.read_csv('geolocation_dataset.csv')

order_items_products = pd.merge(order_items, products, on='product_id')
order_items_products = pd.merge(order_items_products, product_translation, on='product_category_name', how='left')
print(order_items_products.head())
category_sales = order_items_products['product_category_name_english'].value_counts().reset_index()
category_sales.columns = ['product_category', 'order_count']
print(category_sales.head(10))
plt.figure(figsize=(10,6))
sns.barplot(x='order_count', y='product_category', data=category_sales.head(10), palette='viridis')
plt.title('10 Kategori Produk dengan Pesanan Terbanyak')
plt.xlabel('Jumlah Pesanan')
plt.ylabel('Kategori Produk')
plt.show()
st.title('Analisis Pola Pembelian Berdasarkan Kategori Produk')
st.header('Pola Pembelian Berdasarkan Kategori Produk')
st.dataframe(category_sales.head(10))

plt.figure(figsize=(10,6))
sns.barplot(x='order_count', y='product_category', data=category_sales.head(10), palette='viridis')
plt.title('10 Kategori Produk dengan Pesanan Terbanyak')
st.pyplot(plt)