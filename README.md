# Intelligent Credit Card Customer Segmentation using Machine Learning

##  Project Overview

The **Intelligent Credit Card Customer Segmentation** project is a Machine Learning application that groups credit card customers based on their financial behavior using the **K-Means Clustering** algorithm.

Instead of treating every customer the same, this project identifies customers with similar spending habits, payment behavior, credit usage, and purchasing patterns. These customer segments help banks and financial institutions create personalized marketing strategies, improve customer retention, and offer suitable financial products.

This project follows a complete Machine Learning pipeline including data preprocessing, exploratory data analysis, feature engineering, clustering, visualization, and business insight generation.

---

#  Objectives

- Analyze customer financial behavior.
- Clean and preprocess the dataset.
- Perform Exploratory Data Analysis (EDA).
- Standardize numerical features.
- Determine the optimal number of customer groups.
- Segment customers using K-Means Clustering.
- Visualize customer clusters using PCA.
- Generate business insights for each customer segment.

---

#  Dataset

### Dataset Name

**CC GENERAL Dataset**

### Description

The dataset contains credit card customer information collected over a period of time.

It includes customer spending patterns, balance information, purchase frequency, payment history, credit limits, cash advances, and tenure.

### Dataset Information

| Property | Value |
|----------|--------|
| Records | 8,950 |
| Features | 18 |
| Missing Values | Yes |
| Duplicate Records | No |

---

## Dataset Features

- Customer ID
- Balance
- Balance Frequency
- Purchases
- One-off Purchases
- Installment Purchases
- Cash Advance
- Purchase Frequency
- One-off Purchase Frequency
- Installment Purchase Frequency
- Cash Advance Frequency
- Cash Advance Transactions
- Purchase Transactions
- Credit Limit
- Payments
- Minimum Payments
- Percentage of Full Payment
- Tenure

---

# 🛠 Technologies Used

## Programming Language

- Python

---

## Development Environment

- Visual Studio Code (VS Code)

---

## Libraries Used

### Data Manipulation

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn

---

# Machine Learning Algorithms

## 1. StandardScaler

### Purpose

Machine learning algorithms work better when all features have the same scale.

Since variables like **Balance** can range up to thousands while **Purchase Frequency** ranges between 0 and 1, scaling ensures fair contribution from every feature.

Output:

```
Mean = 0
Standard Deviation = 1
```

---

## 2. Elbow Method

### Purpose

The Elbow Method helps determine the optimal number of customer clusters.

It calculates the **Within Cluster Sum of Squares (WCSS)** for different values of K.

The point where the curve bends (the "elbow") is selected as the optimal number of clusters.

For this project,

```
Optimal K = 4
```

---

## 3. K-Means Clustering

### Purpose

K-Means is an **unsupervised machine learning algorithm**.

It groups customers with similar financial behavior into different clusters.

Customers inside the same cluster have similar characteristics.

Output:

- Cluster 0
- Cluster 1
- Cluster 2
- Cluster 3

---

## 4. Principal Component Analysis (PCA)

### Purpose

The dataset originally contains **17 numerical features**.

Since humans cannot visualize data in 17 dimensions, PCA reduces them into **2 principal components** while preserving most of the information.

This allows easy visualization of customer clusters.

---

# Exploratory Data Analysis (EDA)

The project performs EDA before training the clustering model.

EDA includes:

- Feature Distribution
- Correlation Heatmap
- Missing Value Analysis
- Dataset Statistics
- Data Type Analysis

---

# Module Description

## main.py

Acts as the main controller of the project.

Responsible for:

- Loading dataset
- Running preprocessing
- Calling visualization
- Scaling features
- Running clustering
- Performing PCA
- Generating business insights

---

## data_preprocessing.py

Responsible for:

- Removing Customer ID
- Handling missing values
- Saving cleaned dataset

Output:

```
cleaned_dataset.csv
```

---

## feature_engineering.py

Responsible for:

- Standardizing all numerical features
- Applying StandardScaler

Output:

```
scaled_dataset.csv
```

---

## clustering.py

Responsible for:

- Elbow Method
- K-Means Clustering
- Customer Segment Analysis

Outputs

```
clustered_customers.csv

customer_segments.csv
```

---

## visualization.py

Responsible for generating:

- Feature Distribution
- Correlation Heatmap
- Elbow Method Graph
- PCA Cluster Visualization

---

## utils.py

Contains helper functions used throughout the project to reduce code duplication.

---

# Generated Visualizations

### Feature Distribution

Shows how each feature is distributed across customers.

Helps identify:

- Outliers
- Skewness
- Data spread

---

### Correlation Heatmap

Shows relationships between variables.

Useful for understanding:

- Positive correlation
- Negative correlation
- Strong feature relationships

---

### Elbow Method

Used to determine the optimal number of clusters.

Result:

```
Optimal Number of Clusters = 4
```

---

### PCA Cluster Visualization

Displays customer clusters in a 2D space after dimensionality reduction.

Each color represents one customer segment.

---

#  Outputs

| File | Description |
|------|-------------|
| cleaned_dataset.csv | Dataset after preprocessing |
| scaled_dataset.csv | Standardized dataset |
| clustered_customers.csv | Dataset with cluster labels |
| customer_segments.csv | Average statistics for each customer segment |
| business_insights.txt | Business recommendations based on customer segments |

---

# Future Improvements

- Deploy the project using Streamlit or Flask.
- Add interactive dashboards.
- Compare K-Means with DBSCAN and Hierarchical Clustering.
- Perform automatic cluster profiling.
- Integrate real-time customer prediction.

---

# Project Results

The project successfully:

- Cleaned the dataset.
- Performed feature scaling.
- Identified the optimal number of clusters.
- Segmented customers into four meaningful groups.
- Generated business insights.
- Visualized customer clusters using PCA.

---

# Author

**Rohan Kennedy**

- B.Tech Artificial Intelligence & Machine Learning
- Machine Learning | Data Science | Full Stack Development



# ⭐ If you found this project useful, please consider giving it a Star!
