import pandas as pd

from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import feature_scaling
from src.visualization import (
    feature_distribution,
    correlation_heatmap,
    pca_visualization
)
from src.clustering import (
    elbow_method,
    kmeans_clustering
)
from src.utils import heading


heading("Intelligent Credit Card Customer Segmentation")

print("\nProject Started Successfully...")

# Load Dataset
df = load_data("dataset/CC GENERAL.csv")

print("\nDataset Loaded Successfully!\n")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Records")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)

# Data Preprocessing
df = preprocess_data(df)

# EDA
feature_distribution(df)
correlation_heatmap(df)

# Feature Scaling
scaled_df = feature_scaling(df)

# Elbow Method
elbow_method(scaled_df)

# Clustering
clusters = kmeans_clustering(df, scaled_df)

# PCA
pca_visualization(scaled_df, clusters)