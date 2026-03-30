import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("dataset/sales_data.csv")

# Create Revenue column
data["Revenue"] = data["Quantity"] * data["Price"]

# Convert date column
data["Date"] = pd.to_datetime(data["Date"])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Data")

region_filter = st.sidebar.multiselect(
    "Select Region",
    options=data["Region"].unique(),
    default=data["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "Select Product",
    options=data["Product"].unique(),
    default=data["Product"].unique()
)

filtered_data = data[
    (data["Region"].isin(region_filter)) &
    (data["Product"].isin(product_filter))
]

# -----------------------------
# Dashboard Title
# -----------------------------
st.title("Sales Data Analytics Dashboard")

st.write("Interactive dashboard for analyzing sales performance.")

# -----------------------------
# KPI - Total Revenue
# -----------------------------
total_revenue = filtered_data["Revenue"].sum()

st.metric("Total Revenue", f"${total_revenue}")

# -----------------------------
# Sales by Region
# -----------------------------
st.subheader("Sales by Region")

region_sales = filtered_data.groupby("Region")["Revenue"].sum()

fig1, ax1 = plt.subplots()
region_sales.plot(kind="bar", ax=ax1)
plt.ylabel("Revenue")

st.pyplot(fig1)

# -----------------------------
# Product Performance
# -----------------------------
st.subheader("Product Performance")

product_sales = filtered_data.groupby("Product")["Revenue"].sum()

fig2, ax2 = plt.subplots()
product_sales.plot(kind="pie", autopct='%1.1f%%', ax=ax2)

st.pyplot(fig2)

# -----------------------------
# Monthly Sales Trend
# -----------------------------
st.subheader("Monthly Sales Trend")

filtered_data["Month"] = filtered_data["Date"].dt.month

monthly_sales = filtered_data.groupby("Month")["Revenue"].sum()

fig3, ax3 = plt.subplots()
monthly_sales.plot(kind="line", marker="o", ax=ax3)

plt.ylabel("Revenue")

st.pyplot(fig3)

# -----------------------------
# Top Selling Products Table
# -----------------------------
st.subheader("Top Selling Products")

top_products = filtered_data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

st.dataframe(top_products)

# -----------------------------
# Revenue Heatmap
# -----------------------------
st.subheader("Revenue Heatmap")

heatmap_data = filtered_data.pivot_table(
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

fig4, ax4 = plt.subplots()
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", ax=ax4)

st.pyplot(fig4)

# -----------------------------
# Business Insights
# -----------------------------
st.subheader("Business Insights")

best_region = filtered_data.groupby("Region")["Revenue"].sum().idxmax()
best_product = filtered_data.groupby("Product")["Revenue"].sum().idxmax()

st.write(f"🏆 Best Performing Region: **{best_region}**")
st.write(f"📦 Top Selling Product: **{best_product}**")