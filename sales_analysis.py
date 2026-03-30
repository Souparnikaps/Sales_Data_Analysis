import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("../dataset/sales_data.csv")

# Create revenue column
data["Revenue"] = data["Quantity"] * data["Price"]

print("Dataset Preview:")
print(data.head())

# Total Revenue
total_revenue = data["Revenue"].sum()
print("Total Revenue:", total_revenue)

# Sales by Region
region_sales = data.groupby("Region")["Revenue"].sum()
print(region_sales)

# Sales by Product
product_sales = data.groupby("Product")["Revenue"].sum()
print(product_sales)

region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Revenue")
plt.show()

product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.ylabel("Revenue")
plt.show()

data["Date"] = pd.to_datetime(data["Date"])
data["Month"] = data["Date"].dt.month

monthly_sales = data.groupby("Month")["Revenue"].sum()

monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Revenue")
plt.show()

sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Sales Data Correlation")
plt.show()