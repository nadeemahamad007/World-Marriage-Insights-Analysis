from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "World_Marriage_Dataset.csv"


st.set_page_config(page_title="World Marriage Analysis Dashboard", layout="wide")


@st.cache_data
def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def add_styles() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(238, 199, 154, 0.45), transparent 30%),
                radial-gradient(circle at bottom right, rgba(93, 134, 197, 0.28), transparent 25%),
                linear-gradient(135deg, #f6efe7 0%, #eef4f8 100%);
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.78);
            border: 1px solid rgba(62, 84, 120, 0.12);
            padding: 1rem;
            border-radius: 18px;
            box-shadow: 0 12px 30px rgba(34, 54, 82, 0.08);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def extract_age_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.astype(str).str.extract(r"(\d+)")[0], errors="coerce")


add_styles()

st.title("World Marriage Analysis Dashboard")
st.caption("Interactive EDA, demographic insights, and clustering on the World Marriage Dataset (1970-2017)")

if not DATA_PATH.exists():
    st.error("Dataset not found. Add data/World_Marriage_Dataset.csv to run the dashboard.")
    st.stop()

try:
    df = load_data()
except Exception as exc:
    st.error(f"Unable to load dataset: {exc}")
    st.stop()

required_columns = [
    "Country",
    "AgeGroup",
    "Sex",
    "MaritalStatus",
    "Data Collection (Start Year)",
    "Data Collection (End Year)",
]

missing_columns = [column for column in required_columns if column not in df.columns]
if missing_columns:
    st.error(f"Dataset is missing required columns: {', '.join(missing_columns)}")
    st.stop()

df = df.copy()
df["AgeNumeric"] = extract_age_numeric(df["AgeGroup"])
df["Data Collection (Start Year)"] = pd.to_numeric(df["Data Collection (Start Year)"], errors="coerce")
df["Data Collection (End Year)"] = pd.to_numeric(df["Data Collection (End Year)"], errors="coerce")

st.sidebar.header("Explore Filters")
selected_countries = st.sidebar.multiselect(
    "Country",
    options=sorted(df["Country"].dropna().unique()),
    default=sorted(df["Country"].dropna().unique())[:10],
)
selected_age_groups = st.sidebar.multiselect(
    "Age Group",
    options=sorted(df["AgeGroup"].dropna().unique()),
    default=sorted(df["AgeGroup"].dropna().unique()),
)
selected_genders = st.sidebar.multiselect(
    "Gender",
    options=sorted(df["Sex"].dropna().unique()),
    default=sorted(df["Sex"].dropna().unique()),
)
selected_statuses = st.sidebar.multiselect(
    "Marital Status",
    options=sorted(df["MaritalStatus"].dropna().unique()),
    default=sorted(df["MaritalStatus"].dropna().unique()),
)

filtered_df = df[
    df["Country"].isin(selected_countries)
    & df["AgeGroup"].isin(selected_age_groups)
    & df["Sex"].isin(selected_genders)
    & df["MaritalStatus"].isin(selected_statuses)
].copy()

if filtered_df.empty:
    st.warning("No data matches the selected filters. Adjust the sidebar filters to continue.")
    st.stop()

married_count = int((filtered_df["MaritalStatus"] == "Married").sum())
divorced_count = int((filtered_df["MaritalStatus"] == "Divorced").sum())
most_common_status = filtered_df["MaritalStatus"].mode().iat[0]
top_country = filtered_df["Country"].mode().iat[0]

metric_cols = st.columns(4)
metric_cols[0].metric("Filtered Records", f"{len(filtered_df):,}")
metric_cols[1].metric("Married", f"{married_count:,}")
metric_cols[2].metric("Divorced", f"{divorced_count:,}")
metric_cols[3].metric("Top Status", most_common_status)

st.markdown(f"Top country in the current filtered view: **{top_country}**")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    status_by_gender = px.histogram(
        filtered_df,
        x="MaritalStatus",
        color="Sex",
        barmode="group",
        title="Marital Status Distribution by Gender",
        text_auto=True,
    )
    status_by_gender.update_layout(xaxis_title="", yaxis_title="Count")
    st.plotly_chart(status_by_gender, use_container_width=True)

with chart_col2:
    age_distribution = px.box(
        filtered_df.dropna(subset=["AgeNumeric"]),
        x="MaritalStatus",
        y="AgeNumeric",
        color="Sex",
        title="Age Group Distribution by Marital Status",
    )
    age_distribution.update_layout(xaxis_title="", yaxis_title="Approximate Age Group Start")
    st.plotly_chart(age_distribution, use_container_width=True)

country_stats = filtered_df.groupby("Country")["MaritalStatus"].value_counts().unstack(fill_value=0)

if "Married" in country_stats.columns:
    top_married = country_stats["Married"].nlargest(10).reset_index(name="Count")
    fig_married = px.bar(
        top_married,
        x="Country",
        y="Count",
        title="Top 10 Countries with Highest Married Count",
        text_auto=True,
    )
    st.plotly_chart(fig_married, use_container_width=True)

if "Divorced" in country_stats.columns:
    top_divorced = country_stats["Divorced"].nlargest(10).reset_index(name="Count")
    fig_divorced = px.bar(
        top_divorced,
        x="Country",
        y="Count",
        title="Top 10 Countries with Highest Divorced Count",
        text_auto=True,
        color_discrete_sequence=["#c75b5b"],
    )
    st.plotly_chart(fig_divorced, use_container_width=True)

timeline = (
    filtered_df.dropna(subset=["Data Collection (Start Year)"])
    .groupby(["Data Collection (Start Year)", "MaritalStatus"])
    .size()
    .reset_index(name="Count")
)

fig_timeline = px.line(
    timeline,
    x="Data Collection (Start Year)",
    y="Count",
    color="MaritalStatus",
    markers=True,
    title="Marital Status Trends Over Time",
)
st.plotly_chart(fig_timeline, use_container_width=True)

st.subheader("Clustering Snapshot")
cluster_df = filtered_df[["Country", "AgeGroup", "Sex", "MaritalStatus"]].astype(str).copy()
encoder = LabelEncoder()
for column in cluster_df.columns:
    cluster_df[column] = encoder.fit_transform(cluster_df[column])

if len(cluster_df) >= 10:
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_df["Cluster"] = kmeans.fit_predict(cluster_df)

    cluster_chart = px.scatter_3d(
        cluster_df,
        x="Country",
        y="AgeGroup",
        z="MaritalStatus",
        color=cluster_df["Cluster"].astype(str),
        title="K-Means Clustering on Encoded Features",
    )
    cluster_chart.update_layout(legend_title_text="Cluster")
    st.plotly_chart(cluster_chart, use_container_width=True)
else:
    st.info("At least 10 filtered rows are needed to display the clustering chart.")

with st.expander("View Filtered Data"):
    st.dataframe(filtered_df.head(100), use_container_width=True)

with st.expander("Dataset Summary"):
    summary = pd.DataFrame(
        {
            "Column": filtered_df.columns,
            "Non-Null Count": [filtered_df[column].notna().sum() for column in filtered_df.columns],
            "Unique Values": [filtered_df[column].nunique(dropna=True) for column in filtered_df.columns],
            "Data Type": [str(filtered_df[column].dtype) for column in filtered_df.columns],
        }
    )
    st.dataframe(summary, use_container_width=True)

st.markdown("---")
st.markdown(
    "This dashboard was developed for an MCA major project focused on exploratory data analysis, "
    "machine learning, clustering, and interactive reporting on global marriage trends."
)
