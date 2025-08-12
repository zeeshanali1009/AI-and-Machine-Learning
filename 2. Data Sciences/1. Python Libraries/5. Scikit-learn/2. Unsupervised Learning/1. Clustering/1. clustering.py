from sklearn.cluster import KMeans
import numpy as np

# Fake data: [Spending Score, Income]
X = np.array([
    [15, 20000],
    [16, 22000],
    [17, 21000],
    [80, 90000],
    [85, 88000],
    [78, 92000]
])

# Apply KMeans (let’s assume we want 2 clusters)
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

print("Cluster Labels:", kmeans.labels_)
print("Centroids:", kmeans.cluster_centers_)
