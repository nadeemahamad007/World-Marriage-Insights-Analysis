from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import DBSCAN, KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "World_Marriage_Dataset.csv"


def load_dataset() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def prepare_dataset(df: pd.DataFrame) -> pd.DataFrame:
    prepared = df.copy()
    prepared["AgeGroup"] = prepared["AgeGroup"].astype(str)
    prepared["AgeNumeric"] = pd.to_numeric(
        prepared["AgeGroup"].str.extract(r"(\d+)")[0],
        errors="coerce",
    )
    prepared["Data Collection (Start Year)"] = pd.to_numeric(
        prepared["Data Collection (Start Year)"],
        errors="coerce",
    )
    prepared["Data Collection (End Year)"] = pd.to_numeric(
        prepared["Data Collection (End Year)"],
        errors="coerce",
    )
    return prepared


def print_basic_diagnostics(df: pd.DataFrame) -> None:
    print("Dataset Overview")
    print(df.info())
    print("\nFirst 5 Rows")
    print(df.head())
    print("\nMissing Values")
    print(df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())
    print("\nSummary Statistics")
    print(df.describe(include="all"))


def run_eda(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 5))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values Heatmap")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(14, 6))
    sns.countplot(data=df, x="AgeGroup", order=df["AgeGroup"].value_counts().index, color="#4c78a8")
    plt.title("Age Group Distribution")
    plt.xlabel("Age Group")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=df,
        x="MaritalStatus",
        order=df["MaritalStatus"].value_counts().index,
        palette="Set2",
    )
    plt.title("Distribution of Marital Status")
    plt.xlabel("Marital Status")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df.dropna(subset=["AgeNumeric"]), x="MaritalStatus", y="AgeNumeric", palette="coolwarm")
    plt.title("Age Group by Marital Status")
    plt.xlabel("Marital Status")
    plt.ylabel("Approximate Age Group Start")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

    numeric_df = df[["AgeNumeric", "Data Collection (Start Year)", "Data Collection (End Year)"]].dropna()
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.show()

    trend_df = (
        df.dropna(subset=["Data Collection (Start Year)"])
        .groupby(["Data Collection (Start Year)", "MaritalStatus"])
        .size()
        .unstack(fill_value=0)
    )
    trend_df.plot(kind="line", figsize=(14, 7))
    plt.title("Marital Status Trends Over Time")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    country_stats = df.groupby("Country")["MaritalStatus"].value_counts().unstack(fill_value=0)
    if "Married" in country_stats.columns:
        top_10_married = country_stats.sort_values(by="Married", ascending=False).head(10)
        print("\nTop 10 Countries with Highest Marriage Count")
        print(top_10_married[["Married"]])

        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_10_married.index, y=top_10_married["Married"], palette="Blues_r")
        plt.title("Top 10 Countries with Highest Marriage Count")
        plt.xlabel("Country")
        plt.ylabel("Number of Married Individuals")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()

    if "Divorced" in country_stats.columns:
        top_10_divorced = country_stats.sort_values(by="Divorced", ascending=False).head(10)
        print("\nTop 10 Countries with Highest Divorce Count")
        print(top_10_divorced[["Divorced"]])

        plt.figure(figsize=(12, 6))
        sns.barplot(x=top_10_divorced.index, y=top_10_divorced["Divorced"], palette="Reds_r")
        plt.title("Top 10 Countries with Highest Divorce Count")
        plt.xlabel("Country")
        plt.ylabel("Number of Divorced Individuals")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()


def encode_for_modeling(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    model_df = df.drop(
        columns=[
            "Sr.No.",
            "DataProcess",
            "Data Collection (Start Year)",
            "Data Collection (End Year)",
            "Data Source",
            "AgeNumeric",
        ],
        errors="ignore",
    ).copy()

    encoder = LabelEncoder()
    for column in ["MaritalStatus", "Sex", "Country", "AgeGroup"]:
        model_df[column] = encoder.fit_transform(model_df[column].astype(str))

    X = model_df.drop(columns=["MaritalStatus"])
    y = model_df["MaritalStatus"]
    return X, y


def run_classification_models(X: pd.DataFrame, y: pd.Series) -> None:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print(f"\n{name}")
        print("Accuracy:", accuracy_score(y_test, predictions))
        print(classification_report(y_test, predictions))


def run_clustering(df: pd.DataFrame) -> None:
    cluster_df = df.drop(
        columns=[
            "Sr.No.",
            "DataProcess",
            "Data Collection (Start Year)",
            "Data Collection (End Year)",
            "Data Source",
            "AgeNumeric",
        ],
        errors="ignore",
    ).copy()

    encoder = LabelEncoder()
    cluster_df["MaritalStatus_encoded"] = encoder.fit_transform(cluster_df["MaritalStatus"].astype(str))
    cluster_df["Sex"] = encoder.fit_transform(cluster_df["Sex"].astype(str))
    cluster_df["Country"] = encoder.fit_transform(cluster_df["Country"].astype(str))
    cluster_df["AgeGroup"] = encoder.fit_transform(cluster_df["AgeGroup"].astype(str))

    X = cluster_df[["AgeGroup", "Sex", "Country", "MaritalStatus_encoded"]]
    X_scaled = StandardScaler().fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_df["KMeans_Cluster"] = kmeans.fit_predict(X_scaled)

    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=cluster_df, x="AgeGroup", y="Country", hue="KMeans_Cluster", palette="coolwarm")
    plt.title("K-Means Clustering")
    plt.xlabel("Encoded Age Group")
    plt.ylabel("Encoded Country")
    plt.tight_layout()
    plt.show()

    dbscan = DBSCAN(eps=0.5, min_samples=5)
    cluster_df["DBSCAN_Cluster"] = dbscan.fit_predict(X_scaled)

    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=cluster_df,
        x="AgeGroup",
        y="MaritalStatus_encoded",
        hue="DBSCAN_Cluster",
        palette="Set2",
    )
    plt.title("DBSCAN Clustering of Marital Status")
    plt.xlabel("Encoded Age Group")
    plt.ylabel("Encoded Marital Status")
    plt.tight_layout()
    plt.show()


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    raw_df = load_dataset()
    df = prepare_dataset(raw_df)

    print_basic_diagnostics(df)
    run_eda(df)

    X, y = encode_for_modeling(df)
    run_classification_models(X, y)
    run_clustering(df)

    print("\nProject analysis completed - By Nadeem Ahamad")


if __name__ == "__main__":
    main()
