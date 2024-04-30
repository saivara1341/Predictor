import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Read the CSV file
file_path = 'Sleep_Efficiency.csv'
data = pd.read_csv(file_path)

# Drop rows with NaN values
data.dropna(inplace=True)

# Display available attributes
print("Available attributes:")
for idx, col in enumerate(data.columns):
    print(f"{idx+1}. {col}")

# Ask user to select attributes for clustering
selected_attributes = []
while True:
    try:
        choice = int(input("Enter the number of the attribute to select (0 to finish): "))
        if choice == 0:
            break
        elif choice > len(data.columns) or choice < 0:
            print("Invalid choice. Please enter a valid number.")
        else:
            selected_attributes.append(data.columns[choice - 1])
    except ValueError:
        print("Invalid input. Please enter a number.")

# Prepare data for clustering
X = data[selected_attributes]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform clustering using KMeans
kmeans = KMeans(n_clusters=3)  # You can adjust the number of clusters as per your requirement
kmeans.fit(X_scaled)
data['Cluster'] = kmeans.labels_

# Plot the clusters
for cluster in data['Cluster'].unique():
    plt.scatter(data[data['Cluster'] == cluster][selected_attributes[0]], 
                data[data['Cluster'] == cluster][selected_attributes[1]],
                label=f'Cluster {cluster}')

plt.xlabel(selected_attributes[0])
plt.ylabel(selected_attributes[1])
plt.title('Cluster Plot')
plt.legend()
plt.show()
