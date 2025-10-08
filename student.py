import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 

def student_data():
    df = pd.read_csv('bi.csv', encoding='latin-1')

    print(f"Loaded {len(df)} records")
    print(f"Columns: {df.columns.tolist()}")

    # Check for missing values
    print("Missing values:")
    print(df.isnull().sum())
    print("First rows:")
    print(df.head())
    
    # Clean duplicates and missing values
    df = df.drop_duplicates()
    print(f"After duplicates: {len(df)} records")
    
    df = df.fillna(0)           
    df["gender"] = df["gender"].str.upper()
    
    # Compute average score
    df["avg_score"] = (df["Python"] + df["DB"]) / 2
    print(df[["Python", "DB", "avg_score"]].head())
    
    # Active students filter
    active_passed = df[(df["studyHOURS"] >= 10) & (df["avg_score"] >= 50.0)]
    print(f"Number of active & passed students: {len(active_passed)}")
    print(active_passed.head())
    active_passed.to_csv("active_passed_students.csv", index=False)
    print("✅ Saved to active_passed_students.csv")
    
    # Gender filter
    gender_type = df[df["gender"] == "FEMALE"]
    print(f"Number of females: {len(gender_type)}")
    gender_type.to_csv("gender_type.csv", index=False)
    print("✅ Saved to gender_type.csv")
    
    # Binning
    avg_bins = [0, 30, 50, 70, 100]
    avg_labels = ["D", "C", "B", "A"]
    df["Grades"] = pd.cut(df["avg_score"], bins=avg_bins, labels=avg_labels)
    df.to_csv("Grades.csv", index=False)
    print("✅ Saved to Grades.csv")
    
    # --- PLOT using your cleaned data ---
    plt.figure(figsize=(8,6))
    plt.scatter(df['studyHOURS'], df['avg_score'], color='blue', label="Data points")

    # Regression line
    m, b = np.polyfit(df['studyHOURS'], df['avg_score'], 1)
    plt.plot(df['studyHOURS'], m*df['studyHOURS'] + b, color='red', label="Regression line")

    plt.xlabel("Study Hours")
    plt.ylabel("Average Score")
    plt.title("Average Score vs Study Hours")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    #using plotly to create a scatter and hisogram
    fig = px.scatter(df, x="studyHOURS", y="Python", title="Study Hours vs Python Score",
                 labels={"studyHOURS": "Study Hours", "Python": "Python Grade"},
                 color="gender")   # color by gender (optional)
    fig.show()
    fig.write_image("scatter.png")
    
    fig = px.histogram(df, x="avg_score", nbins=20, title="Distribution of Average Scores")
    fig.show()
    fig.write_image("histogram.png")

    #pie charts
    fig = px.pie(df, names='avg_score', title='Grade Distribution')
    fig.show()
    fig.write_image("pie.png")
    
    #box plots
    fig = px.box(df, x='avg_score', y='StudyHours', title='Study Hours by Grade')
    fig.show()
    fig.write_image("box.png")
    
    # Pearson correlation
    corr = df[['studyHOURS', 'avg_score']].corr(method='pearson')
    print("Pearson correlation:")
    print(corr)

    return df



if __name__ == "__main__":
    student_data()
