# ==========================================
# TITANIC DATA ENGINEERING PROJECT
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

# ------------------------------------------
# 1. Load Dataset
# ------------------------------------------
df = pd.read_csv("train.csv")

print("Shape:", df.shape)

print("\nINFO:")
print(df.info())

print("\nDESCRIBE:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------
# 2. Data Cleaning
# ------------------------------------------

# Drop Cabin column (>10% missing)
df.drop(columns="Cabin", inplace=True)

# Fill Age with median
df["Age"].fillna(df["Age"].median(), inplace=True)

# Fill Embarked with mode
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ------------------------------------------
# 3. Outlier Handling (Age)
# ------------------------------------------

Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["Age"] = np.where(df["Age"] < lower, lower, df["Age"])
df["Age"] = np.where(df["Age"] > upper, upper, df["Age"])

# ------------------------------------------
# 4. Outlier Handling (Fare)
# ------------------------------------------

Q1 = df["Fare"].quantile(0.25)
Q3 = df["Fare"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["Fare"] = np.where(df["Fare"] < lower, lower, df["Fare"])
df["Fare"] = np.where(df["Fare"] > upper, upper, df["Fare"])

# ------------------------------------------
# 5. Save to SQLite
# ------------------------------------------

conn = sqlite3.connect("titanic.db")

df.to_sql("passengers", conn, if_exists="replace", index=False)

print("Database Created Successfully")

# Box Plot
plt.boxplot(df["Age"])
plt.title("Age Box Plot")
plt.ylabel("Age")
plt.show()

# Histogram
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Bar Chart
df["Sex"].value_counts().plot(kind="bar")
plt.title("Gender Count")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Scatter Plot
plt.scatter(df["Age"], df["Fare"])
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()

# GroupBy Chart
group = df.groupby("Pclass")["Fare"].mean()

group.plot(kind="bar")
plt.title("Average Fare by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Fare")
plt.show()
