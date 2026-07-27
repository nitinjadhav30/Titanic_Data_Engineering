# Titanic Data Engineering, SQL & Exploratory Data Analysis

## Project Overview

This project performs Data Engineering, Data Cleaning, SQL Querying and Exploratory Data Analysis on the Titanic dataset using Python, Pandas, SQLite and Matplotlib.

---

## Dataset

- Dataset Name: Titanic - Machine Learning from Disaster
- File Used: train.csv
- Rows: 891
- Columns: 12

---

# Libraries Used

- Pandas
- NumPy
- Matplotlib
- SQLite3

---

# Dataset Exploration

The dataset was loaded using Pandas.

The following functions were used:

- shape
- info()
- describe()
- isnull()

---

# Missing Values

| Column | Missing Values | Strategy | Reason |
|---------|---------------|----------|--------|
| Age | 177 | Filled with Median | Numeric column |
| Cabin | 687 | Dropped | More than 10% values missing |
| Embarked | 2 | Filled with Mode | Categorical column |

---

# Incorrect Data Types

No incorrect data types were found in the dataset.

---

# Duplicate Rows

Duplicate rows were removed using

```python
drop_duplicates()
```

---

# Outlier Detection

Outliers were detected using the IQR Method.

Numeric Columns

- Age
- Fare

Outliers were capped using lower and upper IQR limits.

---

# SQLite Database

Database Name

```
titanic.db
```

Table Name

```
passengers
```

---

# SQL Queries

The following SQL concepts were implemented.

1. WHERE
2. GROUP BY
3. HAVING
4. ORDER BY
5. LIMIT
6. BETWEEN
7. AND Condition

---

# Visualizations

The following visualizations were created.

- Box Plot
- Histogram
- Bar Chart
- Scatter Plot
- GroupBy Bar Chart

Each visualization contains:

- Title
- X-axis Label
- Y-axis Label

---

# Insights

- Cabin column had more than 75% missing values and was removed.
- Missing values in Age were filled using the median.
- Missing values in Embarked were filled using the mode.
- Most passengers belonged to Passenger Class 3.
- Female passengers had a higher survival rate than male passengers.
- Passenger fares contained outliers which were capped using the IQR method.
- First-class passengers paid the highest average fare.
- The majority of passengers were between 20 and 40 years old.

---

# Files Included

```
Titanic_Project.ipynb

train.csv

clean_titanic.csv

titanic.db

queries.sql

README.md

requirements.txt
```

---

# Requirements

```
pandas
numpy
matplotlib
sqlite3
```

---

# Author

Your Name 
