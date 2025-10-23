# Lifestyle Clustering Project

## Project Overview
This project analyzes a global coffee and health dataset to identify clusters of people with similar lifestyle patterns using clustering techniques like **K-Means** and **DBSCAN**.

## Dataset
- Source: [Kaggle - Global Coffee Health Dataset](https://www.kaggle.com/datasets/uom190346a/global-coffee-health-dataset/data)  
- Features include: `Age`, `Gender`, `Country`, `Coffee_Intake`, `Caffeine_mg`, `Sleep_Hours`, `Sleep_Quality`, `BMI`, `Heart_Rate`, `Stress_Level`, `Physical_Activity_Hours`, `Health_Issues`, `Occupation`, `Smoking`, `Alcohol_Consumption`.

## Preprocessing
- Handled missing values and outliers.  
- Scaled numeric features using `StandardScaler`.  
- Label-encoded categorical features (`Sleep_Quality`, `Stress_Level`, `Smoking`, `Alcohol_Consumption`).  
- Combined numeric and categorical features for clustering.  

## Clustering
- Applied **PCA** for dimensionality reduction to reduce noise and highlight variance.  
- Ran **K-Means** with silhouette analysis to determine the optimal number of clusters.  
- Applied **DBSCAN** to identify density-based clusters and noise.  
- Silhouette scores indicated moderate clustering, reflecting overlapping lifestyle patterns.  

## Cluster Interpretation
- Generated cluster-wise averages of numeric and categorical features.  
- Example interpretations:
  - Cluster 0: High stress, low physical activity  
  - Cluster 1: Healthy lifestyle, moderate coffee intake  
  - Cluster 2: High coffee intake, moderate sleep quality  

## Visualization
- PCA 2D scatter plots to visualize cluster separation and centroids.  
- DBSCAN k-distance graphs used to select optimal `eps` parameter.  

## How to Run
1. Install dependencies: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`.  
2. Load the dataset and define numeric & categorical columns.  
3. Run preprocessing, PCA, and clustering scripts.  
4. View cluster summary and visualizations.

## Conclusion
The project successfully identifies broad lifestyle clusters in the dataset, providing insights into sleep, coffee consumption, stress, and physical activity patterns across individuals.
