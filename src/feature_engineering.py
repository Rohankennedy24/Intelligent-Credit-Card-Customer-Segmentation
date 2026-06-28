import pandas as pd
from sklearn.preprocessing import StandardScaler


def feature_scaling(df):

    print("\nStarting Feature Scaling...")
    print("-" * 60)

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(df)

    scaled_df = pd.DataFrame(
        scaled_data,
        columns=df.columns
    )

    print("Feature Scaling Completed Successfully!")

    print("\nFirst 5 Rows of Scaled Dataset")
    print("-" * 60)

    print(scaled_df.head())

    scaled_df.to_csv(
        "outputs/scaled_dataset.csv",
        index=False
    )

    print("\nScaled dataset saved successfully!")

    return scaled_df