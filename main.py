#E-Commerce Sales Analysis - 
import pandas as pd
#  Load Dataset
data = pd.read_csv("ecommerce_sales.csv")
# Convert Order_Date to datetime
data["Order_Date"] = pd.to_datetime(data["Order_Date"])
# 2. Create Revenue Column
data["Revenue"] = data["Quantity"] * data["Unit_Price"] * (1 - data["Discount"])
# 3. Total Revenue
total_revenue = data["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)
# 4. Category-wise Revenue
category_revenue = (
    data.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("Category-wise Revenue:")
print(category_revenue)
# 5. Monthly Sales Trend
monthly_sales = (
    data.groupby(data["Order_Date"].dt.to_period("M"))["Revenue"]
    .sum()
    .reset_index()
)
print("Monthly Sales Trend:")
print(monthly_sales)
# 6. Best Performing Region
region_revenue = (
    data.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
best_region = region_revenue.idxmax()
print("Region-wise Revenue:")
print(region_revenue)

print("\nBest Performing Region:", best_region)
# 7. Top 5 Products
top_products = (
    data.groupby("Product_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print("Top 5 Products:")
print(top_products)
# 8. Export Summary Report
summary_report = pd.DataFrame({
    "Total Revenue": [total_revenue],
    "Best Performing Region": [best_region]
})
summary_report.to_csv("summary_report.csv", index=False)
print("Summary report exported")