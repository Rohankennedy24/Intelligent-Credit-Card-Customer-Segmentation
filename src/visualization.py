import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA


def feature_distribution(df):

    print("\nStarting Exploratory Data Analysis...")
    print("-" * 60)

    df.hist(figsize=(18,12), bins=30)

    plt.suptitle("Feature Distribution")

    plt.tight_layout()

    plt.savefig("images/feature_distribution.png")

    plt.show()

    print("Feature Distribution graph saved successfully.")


def correlation_heatmap(df):

    plt.figure(figsize=(15,10))

    sns.heatmap(df.corr(), cmap="coolwarm", annot=False)

    plt.title("Correlation Heatmap")

    plt.savefig("images/heatmap.png")

    plt.show()

    print("Correlation Heatmap saved successfully.")


def pca_visualization(scaled_df, clusters):

    print("\nApplying PCA...")
    print("-"*60)

    pca = PCA(n_components=2)

    pca_data = pca.fit_transform(scaled_df)

    pca_df = pd.DataFrame(
        pca_data,
        columns=["PCA1","PCA2"]
    )

    pca_df["Cluster"] = clusters

    print("PCA Completed Successfully!")

    plt.figure(figsize=(10,7))

    plt.scatter(
        pca_df["PCA1"],
        pca_df["PCA2"],
        c=pca_df["Cluster"],
        cmap="viridis",
        s=30
    )

    plt.title("Customer Segments using PCA")

    plt.xlabel("Principal Component 1")

    plt.ylabel("Principal Component 2")

    plt.colorbar(label="Cluster")

    plt.savefig("images/pca_clusters.png")

    plt.show()

    print("PCA Cluster graph saved successfully!")