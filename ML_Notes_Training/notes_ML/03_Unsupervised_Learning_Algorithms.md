# Module 3: Unsupervised Learning Algorithms

In Unsupervised Learning, there are no labels. We feed the algorithm raw data (`X`), but we do not give it the answers (`y`). The algorithm is forced to explore the data and discover hidden structures, patterns, or groupings entirely on its own.

## The Two Main Branches

### 1. Clustering
Grouping similar data points together based on their features. The algorithm tries to ensure that items in the same group (cluster) are highly similar, while items in different groups are highly dissimilar.
*   *Examples:* Customer market segmentation (finding types of shoppers), grouping news articles by topic, grouping pixels in an image by color.

### 2. Dimensionality Reduction
Taking a dataset with many features (columns/dimensions) and reducing it to a much smaller number of features while retaining as much of the original, important information as possible.
*   *Examples:* Compressing an image, speeding up training for an overly complex dataset, or visualizing data on a 2D graph that originally had 100 dimensions.

---

## Core Algorithms

### 1. K-Means Clustering
*   **Concept:** Grouping data into `K` distinct physical clusters.
*   **Type:** Clustering.
*   **How it works:** 
    1. You tell the algorithm how many clusters (`K`) you want it to find.
    2. It drops `K` random center points (centroids) onto the data graph.
    3. Every data point assigns itself to the closest centroid.
    4. The centroid calculates the center of its new group and moves to that new center.
    5. Steps 3 and 4 repeat until the centroids stop moving.
*   **Best for:** Segmenting datasets into known numbers of groups. Very fast.
*   **Weakness:** You must manually choose the number of clusters (`K`) beforehand. It also struggles with non-circular cluster shapes.

### 2. Hierarchical Clustering
*   **Concept:** Building a tree of nested clusters.
*   **Type:** Clustering.
*   **How it works:** It starts by treating every single data point as its own cluster. Then, it finds the two clusters that are closest together and merges them into one. It repeats this process over and over until all points are merged into a single giant cluster. This creates a diagram called a "Dendrogram," which allows the human to slice the tree wherever they want to determine the final number of clusters.
*   **Best for:** When you don't know how many clusters exist and want a visual representation of relationships (e.g., evolutionary biology, taxonomy).

### 3. Principal Component Analysis (PCA)
*   **Concept:** Finding the specific "angles/directions" (Principal Components) in the data that contain the most variation (information), and throwing away the rest.
*   **Type:** Dimensionality Reduction.
*   **How it works:** Imagine a 3D cloud of points that actually looks a lot like a flat pancake. PCA figures out that the 3rd dimension (thickness) barely varies, so it flattens the 3D cloud into a 2D shadow of the pancake without losing the overall shape. It rotates the axes to line up with the directions where the data spreads out the most.
*   **Best for:** Compressing data before feeding it into slow supervised algorithms, avoiding the "Curse of Dimensionality", and plotting high-dimensional data (like Word Embeddings) onto a 2D screen so humans can look at it.

### 4. Association Rules (Apriori Algorithm)
*   **Concept:** "People who bought X also bought Y."
*   **Type:** Rule Discovery.
*   **How it works:** It scans huge lists of transactions to find items that frequently occur together. 
*   **Best for:** Market basket analysis in retail (e.g., discovering that customers who buy diapers on Friday nights frequently also buy beer), and recommendation engines (e.g., Netflix "Because you watched...").

---
> **Next Step:** Proceed to `04_Model_Evaluation_and_Validation.md` to learn how we measure the success of ML models.
