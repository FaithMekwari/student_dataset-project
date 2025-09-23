import pandas as pd 
import numpy as np

def student_data():
    df= pd.read_csv('bi.csv',encoding='latin-1')

    print(f"loaded{len(df)}records")
    print (f"columns:{df.columns.tolist()}")

    
    
    print("missing values:")
    print(df.isnull().sum())
    print("in first  rows:")
    print(df.head())
    
    df =df.drop_duplicates()
    print("after duplicates: {len(df)}records")
    
    df = df.fillna(0)           # replace NaN with 0
  # replace NaN with text
    df["gender"] = df["gender"].str.upper()
    
    df["avg_score"] = (df["Python"] + df["DB"]) / 2

    print(df[["Python", "DB", "avg_score"]].head())
    
    # define active as hours >= 10 AND passed
    active_passed = df[(df["studyHOURS"] >= 10) & (df["avg_score"] >= 50.0)]

    print(f"Number of active & passed students: {len(active_passed)}")
    print(active_passed.head())

# save to new CSV
    active_passed.to_csv("active_passed_students.csv", index=False)
    print("✅ Saved to active_passed_students.csv")
    
    gender_type = df[(df["gender"]== "FEMALE" )]
    print(f"Number of females: {len(gender_type)}")
    gender_type.to_csv("gender_type.csv",index = False)
    print("✅ Saved to gender_type.csv")
    
    
    #binning using pd.cut()
    avg_bins =[0,30,50,70,100]
    avg_labels =["D","C","B","A"]
    
    df["Grades"]=pd.cut(df["avg_score"],bins= avg_bins,labels=avg_labels)
    df.to_csv("Grades.csv", index=False)
    print("✅ Saved to Grades.csv")
    
    return df
if __name__ == "__main__":
    student_data()
