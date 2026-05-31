# World Marriage Insights Analysis

## Overview

World Marriage Insights Analysis is an MCA major project focused on exploratory data analysis, machine learning, clustering, and dashboard-based insight generation using the World Marriage Dataset.

The project studies global marriage patterns across more than 271,000 records collected from 232 countries between 1970 and 2017. It combines Python-based EDA, classification models, clustering techniques, and a Streamlit dashboard to explore demographic behavior, marital status trends, and country-level differences.

This repository is designed as a complete GitHub-ready academic project showcase with source code, dataset, report files, and dashboard assets in one place.

## Key Highlights

- 271,604+ records analyzed
- 232 countries covered
- Time range from 1970 to 2017
- Exploratory Data Analysis with statistical and visual insights
- Machine learning models for marital status classification
- K-Means and DBSCAN clustering for pattern discovery
- Interactive Streamlit dashboard for dynamic exploration

## Objectives

- Analyze global marriage and divorce trends across countries
- Study marital status variation by age group and gender
- Identify country-level demographic patterns
- Build classification models using scikit-learn
- Apply clustering algorithms for segmentation analysis
- Present findings through an interactive dashboard

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

## Project Structure

```text
World-Marriage-Insights-Analysis/
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

The EDA portion of the project includes:

- Age group distribution analysis
- Marital status distribution
- Gender-based comparison
- Country-wise marriage patterns
- Country-wise divorce patterns
- Correlation heatmap analysis
- Time-based trend analysis
- Dataset diagnostics and summary statistics

## Machine Learning And Clustering

### Classification Models

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Clustering Models

- K-Means
- DBSCAN

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report

## Streamlit Dashboard Features

- Country filter
- Gender filter
- Age group filter
- Marital status filter
- Marital status distribution chart
- Country-level marriage and divorce comparison
- Trend analysis over time
- Clustering visualization
- Filtered data preview

## Reports Included

This repository already includes the following academic and supporting files:

- `reports/Major_Project_Report.pdf`
- `reports/Dashboard-Code.pdf`
- `reports/Dashboard-Screenshot.pdf`
- `reports/World-Marriage-Code.pdf`

Screenshots for the GitHub project gallery can be added later in the `images/` folder.

## How To Run

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

### 4. Run the EDA and ML script

```bash
python notebooks/World_Marriage_EDA.py
```

## Portability Improvement

The original project used machine-specific local file paths. This repository version has been cleaned so the code reads the dataset using a project-relative path:

```python
from pathlib import Path

data_path = Path(__file__).resolve().parents[1] / "data" / "World_Marriage_Dataset.csv"
```

This makes the project easier to run after cloning from GitHub.

## Results

- Identified broad global marriage trends over multiple decades
- Highlighted country-specific marital status differences
- Built machine learning models for predictive analysis
- Applied clustering methods to reveal hidden groupings
- Delivered an interactive dashboard for practical exploration

## Future Improvements

- Add more dashboard screenshots in `images/`
- Include deployment instructions for Streamlit Cloud
- Add deeper model comparison and tuning
- Add geographical visualizations
- Add forecast-based analysis for future trend prediction

## Author

**Nadeem Ahamad**  
Master of Computer Applications (MCA)  
Major Project 2025

## License

This project is licensed under the MIT License.
