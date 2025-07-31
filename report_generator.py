import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

def generate_visual_reports(df):
    os.makedirs("reports", exist_ok=True)

    # Sales over time
    plt.figure(figsize=(10,6))
    df_grouped = df.groupby('date')['total_sale'].sum().reset_index()
    sns.lineplot(data=df_grouped, x='date', y='total_sale')
    plt.title("Total Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Sale")
    plt.tight_layout()
    plt.savefig("reports/sales_over_time.png")
    plt.close()

    # Region-wise total sale
    plt.figure(figsize=(8,6))
    region_sales = df.groupby('region')['total_sale'].sum().reset_index()
    sns.barplot(data=region_sales, x='region', y='total_sale', palette='Set2')
    plt.title("Region-wise Total Sales")
    plt.tight_layout()
    plt.savefig("reports/region_sales.png")
    plt.close()

    # Correlation heatmap
    plt.figure(figsize=(6,4))
    sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("reports/correlation_heatmap.png")
    plt.close()
