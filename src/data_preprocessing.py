import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df
def preprocess_data(df):

    print("\nStarting Data Preprocessing...")
    print("-" * 60)

    # Remove Customer ID
    df = df.drop("CUST_ID", axis=1)
    print("CUST_ID column removed successfully.")

    # Fill missing values
    df["CREDIT_LIMIT"] = df["CREDIT_LIMIT"].fillna(
        df["CREDIT_LIMIT"].median()
    )

    df["MINIMUM_PAYMENTS"] = df["MINIMUM_PAYMENTS"].fillna(
        df["MINIMUM_PAYMENTS"].median()
    )

    print("Missing values handled successfully.")

    print("\nChecking Missing Values After Cleaning")
    print("-" * 60)
    print(df.isnull().sum())

    print("\nDataset Shape After Cleaning")
    print("-" * 60)
    print(df.shape)

    df.to_csv("outputs/cleaned_dataset.csv", index=False)

    print("\nCleaned dataset saved successfully!")

    return df