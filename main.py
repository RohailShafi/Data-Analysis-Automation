from utils import load_sales_data, load_employee_data, clean_sales_data, merge_data
from report_generator import generate_visual_reports

def main():
    # Load data
    sales_df = load_sales_data("data/sales_data.xlsx")
    emp_df = load_employee_data("data/employee_info.xlsx")

    # Clean and merge
    cleaned_sales = clean_sales_data(sales_df)
    merged_df = merge_data(cleaned_sales, emp_df)

    # Generate visual reports
    generate_visual_reports(merged_df)

    # Save final output
    merged_df.to_excel("output/final_merged_report.xlsx", index=False)
    print("✅ Process completed successfully.")

if __name__ == "__main__":
    main()
