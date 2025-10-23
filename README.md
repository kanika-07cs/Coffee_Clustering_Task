# Global-coffee-health Clustering Project

## Project Overview
This project analyzes a global coffee and health dataset to identify clusters of people with similar lifestyle patterns using clustering techniques like **K-Means** and **DBSCAN**.

## Dataset
- Source: https://www.kaggle.com/datasets/uom190346a/global-coffee-health-dataset/data
- Features include: `Age`, `Gender`, `Country`, `Coffee_Intake`, `Caffeine_mg`, `Sleep_Hours`, `Sleep_Quality`, `BMI`, `Heart_Rate`, `Stress_Level`, `Physical_Activity_Hours`, `Health_Issues`, `Occupation`, `Smoking`, `Alcohol_Consumption`.

## Preprocessing
- Handled missing values and outliers.  
- Scaled numeric features using `StandardScaler`.  
- Label-encoded categorical features (`Sleep_Quality`, `Stress_Level`, `Smoking`, `Alcohol_Consumption`).  
- Combined numeric and categorical features for clustering.  

## Clustering
- Applied **PCA** for dimensionality reduction to reduce noise and highlight variance.  
- **K-Means** with silhouette analysis to determine the optimal number of clusters.  
- Applied **DBSCAN** to identify density-based clusters and noise.  
- Silhouette scores indicated moderate clustering, reflecting overlapping lifestyle patterns.  

## Visualization
- PCA 2D scatter plots to visualize cluster separation and centroids.  
- DBSCAN k-distance graphs used to select optimal eps parameter.  

## Conclusion
The project successfully identifies broad lifestyle clusters in the dataset, providing insights into sleep, coffee consumption, stress, and physical activity patterns across individuals.
