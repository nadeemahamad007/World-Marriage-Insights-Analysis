# World Marriage Insights Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Academic%20Project-6f42c1?style=for-the-badge)

An MCA major project that explores global marriage trends using exploratory data analysis, machine learning, clustering, and a Streamlit dashboard built on the World Marriage Dataset.

## Why This Project Stands Out

- Large-scale dataset with `271,604+` records
- Coverage across `232` countries
- Historical trend range from `1970` to `2017`
- Combines EDA, ML, clustering, and dashboard storytelling
- Packaged as a GitHub-ready academic and portfolio project

## Project Snapshot

| Item | Details |
| --- | --- |
| Project Type | MCA Major Project |
| Domain | Data Analytics / Data Science |
| Dataset | World Marriage Dataset |
| Main Interface | Streamlit Dashboard |
| ML Models | Logistic Regression, Decision Tree, Random Forest |
| Clustering | K-Means, DBSCAN |
| Language | Python |

## Overview

This repository analyzes world marriage data to understand marital status patterns across countries, age groups, genders, and time periods. The project combines traditional exploratory analysis with machine learning and clustering techniques to produce both academic insights and an interactive dashboard experience.

The goal is not only to study the dataset statistically, but also to present the results in a form that is useful for project evaluation, portfolio display, and future extension.

## Features

- Exploratory data analysis on demographic and marital status attributes
- Country-wise marriage and divorce pattern exploration
- Time-based marital trend analysis
- Machine learning classification workflow
- K-Means and DBSCAN clustering workflow
- Interactive Streamlit dashboard with filters
- Cleaned project-relative file paths for easy reuse

## Dataset Information

| Attribute | Description |
| --- | --- |
| `Country` | Country name |
| `AgeGroup` | Age category |
| `Sex` | Gender category |
| `MaritalStatus` | Marital status label |
| `DataProcess` | Survey or census method |
| `Data Collection (Start Year)` | Starting year of collection |
| `Data Collection (End Year)` | Ending year of collection |
| `Data Source` | Source reference |

### Dataset Summary

- Total records: `271,604+`
- Countries covered: `232`
- Time span: `1970-2017`
- Missing values: `0`
- Duplicate rows: `0`

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Streamlit
- Joblib

## Repository Structure

```text
World-Marriage-Insights-Analysis/
|-- .github/
|   |-- workflows/
|   |   `-- python-check.yml
|   `-- PULL_REQUEST_TEMPLATE.md
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
|-- CITATION.cff
|-- CONTRIBUTING.md
|-- LICENSE
|-- README.md
`-- requirements.txt
```

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/nadeemahamad007/World-Marriage-Insights-Analysis.git
cd World-Marriage-Insights-Analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit dashboard

```bash
streamlit run app/app.py
```

### 4. Run the EDA and ML workflow

```bash
python notebooks/World_Marriage_EDA.py
```

## Analytical Scope

### Exploratory Data Analysis

- Age group distribution
- Marital status distribution
- Gender comparison
- Country-wise patterns
- Divorce trend analysis
- Correlation heatmap
- Time trend analysis
- Data quality diagnostics

### Machine Learning

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Clustering

- K-Means
- DBSCAN

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report

## Dashboard Highlights

- Country filter
- Gender filter
- Age group filter
- Marital status filter
- Marital status distribution chart
- Country-level marriage and divorce comparison
- Trend analysis over time
- Clustering visualization
- Filtered data preview

## Included Files

This repository already includes:

- Source code for the Streamlit dashboard
- Source code for EDA, ML, and clustering analysis
- Dataset CSV file
- Final project report PDF
- Dashboard code PDF
- Dashboard screenshot PDF
- Additional project code PDF

## Screenshots

The dashboard is designed to move from dataset overview to filtering, country-level comparisons, trend analysis, and clustering-based insights.

### 1. Dashboard Overview

Main landing view of the Streamlit dashboard with project branding and core layout.

<img width="567" height="275" alt="Dashboard Overview" src="https://github.com/user-attachments/assets/1cdc94e1-9275-4ca5-9c73-a7b7862f5444" />

### 2. Sidebar Filters And User Controls

Interactive controls for country, age group, gender, and marital status selection.

<img width="535" height="427" alt="Sidebar Filters" src="https://github.com/user-attachments/assets/c6bd6516-d5d0-4060-84f2-e6d86ce004a9" />

<img width="519" height="714" alt="Extended Sidebar Filters" src="https://github.com/user-attachments/assets/ae1ede96-3bfc-4eac-bf96-74815d79457d" />

### 3. Dashboard Metrics And Key Insights

High-level summary cards and filtered insights for quick interpretation of the selected data.

<img width="805" height="767" alt="Dashboard Metrics and Insights" src="https://github.com/user-attachments/assets/9888e5f6-9e2c-48a4-8be6-8c7fdfa090f6" />

### 4. Distribution And Comparison Analysis

Visual analysis of marital status distribution, demographic patterns, and country-level comparisons.

<img width="802" height="348" alt="Marital Status Distribution" src="https://github.com/user-attachments/assets/91447669-c8ea-4ea9-9058-92c705def898" />

<img width="802" height="417" alt="Country-wise Marriage Comparison" src="https://github.com/user-attachments/assets/e6d1a10d-853a-4f8f-b761-c25d6c5cf6bc" />

<img width="804" height="457" alt="Country-wise Divorce Comparison" src="https://github.com/user-attachments/assets/c7deab2e-0fb1-4b4a-8988-b17e04be2baf" />

<img width="802" height="449" alt="Age Group and Status Comparison" src="https://github.com/user-attachments/assets/cb30eb4f-78ed-4412-bd37-7fc97d60a673" />

### 5. Trend Analysis Over Time

Time-based views used to study how marital status patterns change across the historical range of the dataset.

<img width="751" height="463" alt="Trend Analysis 1" src="https://github.com/user-attachments/assets/0d115428-7062-43c1-8efd-c981955a7daa" />

<img width="751" height="471" alt="Trend Analysis 2" src="https://github.com/user-attachments/assets/1ca11610-0844-44fe-ac6f-41efe4c7536b" />

<img width="751" height="451" alt="Trend Analysis 3" src="https://github.com/user-attachments/assets/6c56998a-876c-49a5-95e3-a1f6d9cd81a7" />

### 6. Clustering And Pattern Discovery

Clustering outputs showing hidden groupings and encoded pattern discovery using K-Means and DBSCAN-style analysis.

<img width="799" height="480" alt="Clustering Visualization 1" src="https://github.com/user-attachments/assets/2226dd06-498f-4a8c-91ee-742c8e83fc44" />

<img width="751" height="365" alt="Clustering Visualization 2" src="https://github.com/user-attachments/assets/e33eb16e-cd8b-4987-8db7-2ef0ba94658c" />

<img width="751" height="480" alt="Clustering Visualization 3" src="https://github.com/user-attachments/assets/dea2ce5e-f9b9-48ba-8a9c-22bf5457e591" />

## Portability Improvement

The original project used machine-specific local file paths. This repository version uses a project-relative dataset path:

```python
from pathlib import Path

data_path = Path(__file__).resolve().parents[1] / "data" / "World_Marriage_Dataset.csv"
```

That makes the project easier to clone, run, review, and share on GitHub.

## Results

- Identified broad global marriage trends over multiple decades
- Highlighted country-specific marital status differences
- Built machine learning models for predictive analysis
- Applied clustering methods to reveal hidden groupings
- Delivered an interactive dashboard for practical exploration

## Future Improvements

- Add dashboard screenshots in `images/`
- Add a social preview image for better sharing on GitHub
- Deploy the dashboard online
- Tune and compare more ML models
- Add geographical and map-based insights
- Add forecasting or predictive trend analysis

## Author

**Nadeem Ahamad**  
Master of Computer Applications (MCA)  
Major Project 2025

## License

This project is licensed under the MIT License.
