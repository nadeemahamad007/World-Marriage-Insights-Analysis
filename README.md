# World Marriage Analysis Dashboard

## Overview

This project presents a comprehensive Exploratory Data Analysis (EDA), Machine Learning, and Interactive Dashboard solution developed on the World Marriage Dataset.

The dataset contains more than 271,000 records collected across 232 countries between 1970 and 2017. The project analyzes global marriage patterns, demographic trends, marital status distributions, and country-level variations using modern Data Science techniques.

The project was developed as an MCA Final Year Major Project.

Recommended GitHub repository name: `world-marriage-analysis-dashboard`

## Objectives

- Analyze global marriage trends from 1970-2017
- Perform detailed exploratory data analysis
- Discover hidden demographic patterns
- Build machine learning classification models
- Apply clustering techniques for country segmentation
- Develop an interactive Streamlit dashboard
- Generate actionable insights for researchers and policymakers

## Dataset Information

| Attribute | Description |
| --- | --- |
| Country | Country name |
| AgeGroup | Age category |
| Sex | Male/Female |
| MaritalStatus | Marriage status |
| DataProcess | Survey/Census method |
| Data Collection Start Year | Beginning year |
| Data Collection End Year | Ending year |
| Data Source | Source information |

### Dataset Statistics

- Total Records: 271,604+
- Countries Covered: 232
- Time Span: 1970-2017
- Missing Values: 0
- Duplicate Records: 0

## Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-Learn
- Streamlit
- Joblib

## Project Structure

```text
world-marriage-analysis-dashboard/
|-- app/
|   `-- app.py
|-- data/
|   `-- World_Marriage_Dataset.csv
|-- images/
|   `-- .gitkeep
|-- notebooks/
|   `-- World_Marriage_EDA.py
|-- reports/
|   |-- Major_Project_Report.pdf
|   |-- Dashboard-Code.pdf
|   |-- Dashboard-Screenshot.pdf
|   `-- World-Marriage-Code.pdf
|-- .gitignore
|-- LICENSE
|-- README.md
`-- requirements.txt
```

## Exploratory Data Analysis

The project includes analysis such as:

- Age group distribution
- Marital status distribution
- Gender-wise analysis
- Country-wise marriage trends
- Country-wise divorce trends
- Correlation analysis
- Time-series analysis
- Demographic insights

## Machine Learning Models

### Classification

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Clustering

- K-Means Clustering
- DBSCAN

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Dashboard Features

### Interactive Filters

- Country selection
- Gender selection
- Age group selection
- Marital status selection

### Visualizations

- Histograms
- Bar charts
- Box plots
- Correlation heatmaps
- Country comparison charts
- Cluster visualizations

### Key Insights

- Marriage trends
- Divorce trends
- Gender analysis
- Country rankings
- Population segmentation

## Project Workflow

1. Data collection
2. Data cleaning
3. Data transformation
4. Exploratory data analysis
5. Feature engineering
6. Machine learning
7. Clustering analysis
8. Dashboard development
9. Insight generation

## Results

- Identified global marriage patterns
- Discovered country-specific demographic trends
- Segmented countries using clustering algorithms
- Developed an interactive dashboard for dynamic analysis
- Generated insights useful for social researchers and policymakers

## Future Enhancements

- Deep learning models
- Real-time data integration
- Geographical visualizations
- Predictive trend forecasting
- Cloud deployment

## Included Reports And Supporting Files

The repository already includes:

- Major project final report PDF
- Dashboard code PDF
- Dashboard screenshot PDF
- EDA and project code PDF

You can still add PNG screenshots to `images/` later for a stronger GitHub presentation.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/world-marriage-analysis-dashboard.git
cd world-marriage-analysis-dashboard
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add the dataset

Place the dataset at:

```text
data/World_Marriage_Dataset.csv
```

### 4. Run the Streamlit app

```bash
streamlit run app/app.py
```

### 5. Run the EDA and ML script

```bash
python notebooks/World_Marriage_EDA.py
```

## Important Code Improvement

Avoid hardcoded local paths such as:

```python
pd.read_csv("D:\\MCA Life\\...")
```

Use project-relative paths instead:

```python
from pathlib import Path
import pandas as pd
import streamlit as st

data_path = Path(__file__).resolve().parents[1] / "data" / "World_Marriage_Dataset.csv"

try:
    df = pd.read_csv(data_path)
except FileNotFoundError:
    st.error("Dataset not found. Add data/World_Marriage_Dataset.csv")
    st.stop()
```

## Files Included For GitHub Upload

- `README.md`
- `app/app.py`
- `notebooks/World_Marriage_EDA.py`
- `data/World_Marriage_Dataset.csv`
- `requirements.txt`
- `reports/Major_Project_Report.pdf`
- `reports/Dashboard-Code.pdf`
- `reports/Dashboard-Screenshot.pdf`
- `reports/World-Marriage-Code.pdf`
- `LICENSE`
- `.gitignore`

## Git Commands

```bash
git init
git add .
git commit -m "Initial commit - World Marriage Analysis Dashboard"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/world-marriage-analysis-dashboard.git
git push -u origin main
```

## Author

Nadeem Ahamad  
Master of Computer Applications (MCA)  
Major Project 2025

## License

This project is licensed under the MIT License.
