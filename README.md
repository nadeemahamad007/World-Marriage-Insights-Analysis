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

You can upload screenshots later to the `images/` folder for a stronger repository presentation and social preview.

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
