import pandas as pd 

def process_employee_data():
    # 1. Load dataset
    df = pd.read_csv('employee_data.csv')  
    print("✅ Data loaded successfully")
    
    # 2. Explore data
    print(df.info())
    print("\nMissing values before cleaning:")
    print(df.isnull().sum())

    # 3. Remove duplicates
    df = df.drop_duplicates()
    print(f"\nAfter removing duplicates: {len(df)} records")

    # 4. Handle missing values
    df['Salary'].fillna(df['Salary'].median(), inplace=True)
    df['Department'].fillna('Unknown', inplace=True)

    # 5. Clean text data
    df['Name'] = df['Name'].str.strip().str.title()
    df['Email'] = df['Email'].str.lower()

    # 6. Fix data types
    df['Hire_Date'] = pd.to_datetime(df['Hire_Date'])
    df['Employee_ID'] = df['Employee_ID'].astype(str)

    # 7. Create new column (Years of Service)
    df['Years_Service'] = (pd.Timestamp.now() - df['Hire_Date']).dt.days / 365.25
    df['Years_Service'] = df['Years_Service'].round(1)

    # 8. Save cleaned data
    df.to_csv('cleaned_employee_data.csv', index=False)
    print("✅ Saved: cleaned_employee_data.csv")

    return df


# ======================
# TESTING ENVIRONMENT
# ======================
if __name__ == "__main__":
    # Create sample data to test
    sample_data = {
        'Employee_ID': ['E001', 'E002', 'E003', 'E004', 'E005'],
        'Name': ['john doe', 'JANE SMITH', ' bob johnson ', 'alice brown', 'mike davis'],
        'Email': ['JOHN@COMPANY.COM', 'jane@company.com', 'bob@company.com', 'alice@company.com', 'mike@company.com'],
        'Department': ['Engineering', 'Marketing', 'Sales', None, 'Engineering'],
        'Salary': [75000, 65000, None, 60000, 80000],
        'Hire_Date': ['2020-01-15', '2019-06-20', '2021-03-10', '2018-11-05', '2022-09-01']
    }

    # Save sample CSV for testing
    pd.DataFrame(sample_data).to_csv('employee_data.csv', index=False)
    print("Created sample employee_data.csv")

    # Run the processing pipeline
    processed_df = process_employee_data()
    print("\n=== Cleaned Data Preview ===")
    print(processed_df.head())
