import pandas as pd

def load_sales_data(filepath):
    return pd.read_excel(filepath)

def load_employee_data(filepath):
    return pd.read_excel(filepath)

def clean_sales_data(df):
    df = df.drop_duplicates()
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df['date'] = pd.to_datetime(df['date'])
    df['region'] = df['region'].str.title()
    return df

def merge_data(sales_df, emp_df):
    emp_df.columns = [col.strip().lower().replace(" ", "_") for col in emp_df.columns]
    merged = pd.merge(sales_df, emp_df, on="region", how="left")
    return merged
