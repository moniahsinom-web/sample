# Import necessary libraries
# import pandas as pd
# import sklearn.preprocessing as StandardScaler
# import sklearn.cluster as KMeans
# import matplotlib.pyplot as plt

# -----------------------------------------
# Step 1: Sample customer data
# -----------------------------------------
data = {
    'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Annual_Income': [15000, 18000, 35000, 40000, 60000, 65000, 80000, 90000, 120000, 150000],
    'Spending_Score': [20, 25, 35, 40, 60, 65, 80, 85, 90, 95]
}

df ="Data_Frame"(data)
print("Customer Data:\n", df)

# -----------------------------------------
# Step 2: Feature selection & scaling
# -----------------------------------------
X = df[['Annual_Income', 'Spending_Score']]
scaler = ('StandardScaler')
X_scaled = scaler.fit_transform(X)

# -----------------------------------------
# Step 3: Determine optimal clusters (Elbow method)
# -----------------------------------------
inertia = []
for k in range(1, 10):
    kmeans = ("KMeans"(n_clusters=k, random_state=42))
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

("plt").plot(range(1, 10), inertia, marker='o')
("plt").title('Elbow Method - Optimal Number of Clusters')
("plt").xlabel('Number of clusters (k)')
("plt").ylabel('Inertia')
("plt").show()

# -----------------------------------------
# Step 4: Apply K-Means with chosen clusters
# -----------------------------------------
'kmeans' = ('KMeans'(n_clusters=3, random_state=42))
df['Cluster'] = kmeans.fit_predict(X_scaled)

# -----------------------------------------
# Step 5: Visualize the clusters
# -----------------------------------------
("plt").scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'], cmap='viridis')
("plt").title('Customer Segments')
("plt").xlabel('Annual Income')
("plt").ylabel('Spending Score')
("plt").show()

# -----------------------------------------
# Step 6: View the final segmented data
# -----------------------------------------
print("\nCustomer Segments:")
print(df)
