import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


def elbow_method(scaled_df):

    print("\nFinding Optimal Number of Clusters...")
    print("-"*60)

    wcss=[]

    for i in range(1,11):

        kmeans=KMeans(
            n_clusters=i,
            init="k-means++",
            random_state=42,
            n_init=10
        )

        kmeans.fit(scaled_df)

        wcss.append(kmeans.inertia_)

    print("WCSS Values:")

    print(wcss)

    plt.figure(figsize=(8,6))

    plt.plot(range(1,11),wcss,marker="o")

    plt.title("Elbow Method")

    plt.xlabel("Number of Clusters (K)")

    plt.ylabel("WCSS")

    plt.grid(True)

    plt.savefig("images/elbow_method.png")

    plt.show()

    print("Elbow Method graph saved successfully.")


def kmeans_clustering(df,scaled_df):

    print("\nApplying K-Means Clustering...")
    print("-"*60)

    kmeans=KMeans(
        n_clusters=4,
        init="k-means++",
        random_state=42,
        n_init=10
    )

    clusters=kmeans.fit_predict(scaled_df)

    df["Cluster"]=clusters

    print("K-Means Clustering Completed Successfully!")

    print("\nCluster Counts")
    print("-"*60)

    print(df["Cluster"].value_counts().sort_index())

    df.to_csv(
        "outputs/clustered_customers.csv",
        index=False
    )

    print("\nClustered dataset saved successfully!")

    print("\nCluster Centers")
    print("-"*60)

    centers=pd.DataFrame(
        kmeans.cluster_centers_,
        columns=scaled_df.columns
    )

    print(centers)

    print("\nCustomer Segment Analysis")
    print("-"*60)

    summary=df.groupby("Cluster").mean(numeric_only=True)

    print(summary)

    summary.to_csv(
        "outputs/customer_segments.csv"
    )

    print("\nCustomer Segment Summary saved successfully!")

    return clusters