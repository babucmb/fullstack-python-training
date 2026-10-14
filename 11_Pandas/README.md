# 🐼 Pandas — Complete Learning Guide

A practical guide to learning **Pandas in Python**, covering important concepts, commonly used functions, data manipulation, data cleaning, exploratory data analysis (EDA), related libraries, coding examples, and interview questions.

## 📚 Table of Contents

1. [Introduction to Pandas](#-1-introduction-to-pandas)
2. [Why Do We Use Pandas?](#-2-why-do-we-use-pandas)
3. [Installation and Import](#-3-installation-and-import)
4. [Important Python Data Science Libraries](#-4-important-python-data-science-libraries)
5. [Pandas Data Structures](#-5-pandas-data-structures)
6. [Creating DataFrames](#-6-creating-dataframes)
7. [Understanding a Dataset](#-7-understanding-a-dataset)
8. [Reading and Writing Files](#-8-reading-and-writing-files)
9. [Selecting Rows and Columns](#-9-selecting-rows-and-columns)
10. [Filtering Data](#-10-filtering-data)
11. [Adding, Updating and Removing Columns](#-11-adding-updating-and-removing-columns)
12. [Sorting Data](#-12-sorting-data)
13. [Handling Missing Values](#-13-handling-missing-values)
14. [Handling Duplicate Data](#-14-handling-duplicate-data)
15. [Data Type Conversion](#-15-data-type-conversion)
16. [String Operations](#-16-string-operations)
17. [Statistical Operations](#-17-statistical-operations)
18. [GroupBy and Aggregation](#-18-groupby-and-aggregation)
19. [Combining Datasets](#-19-combining-datasets)
20. [Reshaping Data](#-20-reshaping-data)
21. [Date and Time Operations](#-21-date-and-time-operations)
22. [Apply, Map and Lambda](#-22-apply-map-and-lambda)
23. [Exploratory Data Analysis](#-23-exploratory-data-analysis)
24. [Data Visualization](#-24-data-visualization)
25. [Pandas with NumPy and SQL](#-25-pandas-with-numpy-and-sql)
26. [Pandas with Machine Learning](#-26-pandas-with-machine-learning)
27. [Performance and Best Practices](#-27-performance-and-best-practices)
28. [Common Errors](#-28-common-errors)
29. [Interview Questions and Answers](#-29-interview-questions-and-answers)
30. [Coding Practice Questions](#-30-coding-practice-questions)
31. [Mini Projects](#-31-mini-projects)
32. [Learning Roadmap](#-32-learning-roadmap)
33. [Quick Revision Cheat Sheet](#-33-quick-revision-cheat-sheet)
34. [Official Learning Resources](#-34-official-learning-resources)

---

## 🔹 1. Introduction to Pandas

**Pandas** is an open-source Python library used for working with structured and tabular data.

It helps us read, organize, clean, transform, analyze, and export data.

Examples of data that Pandas can handle:

- Student marks
- Employee records
- Sales transactions
- Customer information
- Stock prices
- Survey results
- Machine learning datasets

### Real-world example

Suppose we have this student dataset:

| Name | Age | Marks |
|---|---:|---:|
| Mahesh | 22 | 85 |
| Rahul | 21 | 72 |
| Priya | 22 | 91 |

Using Pandas, we can quickly calculate the average marks, find the highest score, filter students scoring above 80, and export the results to a CSV file.

**In simple words:** Pandas helps us work with data in a table-like structure using Python.

---

## 🔹 2. Why Do We Use Pandas?

Without Pandas, processing a large table using only basic Python lists and dictionaries can become difficult.

Pandas provides convenient functions for:

- Reading CSV and Excel files.
- Selecting specific columns and rows.
- Filtering records using conditions.
- Finding missing values.
- Removing duplicates.
- Calculating statistics.
- Grouping and summarizing data.
- Combining multiple datasets.
- Preparing data for machine learning.

### Typical data-analysis workflow

```text
Raw Data
   ↓
Load Dataset
   ↓
Inspect Data
   ↓
Clean Data
   ↓
Transform Data
   ↓
Analyze Data
   ↓
Visualize Results
   ↓
Export Results
```

---

## 🔹 3. Installation and Import

Install Pandas:

```bash
pip install pandas
```

For common data-analysis tasks, install additional libraries:

```bash
pip install numpy matplotlib seaborn openpyxl jupyter scikit-learn
```

Import Pandas:

```python
import pandas as pd
```

The alias `pd` is the widely used convention for Pandas.

Check the installed version:

```python
print(pd.__version__)
```

---

## 🔹 4. Important Python Data Science Libraries

Pandas is one part of the Python data-analysis ecosystem. Different libraries solve different problems.

| Library | Main purpose | Common use |
|---|---|---|
| **Pandas** | Tabular data manipulation | Clean CSV and Excel data |
| **NumPy** | Numerical computing and arrays | Mathematical operations |
| **Matplotlib** | Data visualization | Basic charts and plots |
| **Seaborn** | Statistical visualization | Heatmaps and statistical charts |
| **Plotly** | Interactive visualization | Interactive dashboards |
| **SciPy** | Scientific computing | Optimization and scientific statistics |
| **Statsmodels** | Statistical modeling | Regression and statistical tests |
| **Scikit-learn** | Machine learning | Training and evaluating ML models |
| **OpenPyXL** | Excel `.xlsx` file handling | Read and modify Excel workbooks |
| **Requests** | HTTP communication | Retrieve data from web APIs |
| **Beautiful Soup** | HTML/XML parsing | Extract information from web pages |
| **Polars** | Tabular data processing | Alternative DataFrame workflows |
| **Dask** | Parallel and larger-than-memory computing | Scale certain data-processing workloads |

### How the libraries work together

```text
Data Source
    ↓
Pandas / Requests
    ↓
NumPy + Pandas
    ↓
Data Cleaning and Analysis
    ↓
Matplotlib / Seaborn / Plotly
    ↓
Scikit-learn / Statsmodels
    ↓
Insights or Predictions
```

### 1. Pandas vs NumPy

**Pandas** works especially well with labeled rows and columns. **NumPy** focuses on efficient numerical arrays and mathematical operations.

```python
import numpy as np
import pandas as pd

numbers = np.array([10, 20, 30])
print(numbers.mean())

marks = pd.Series([10, 20, 30])
print(marks.mean())
```

Both can calculate the mean, but their data structures and broader purposes differ.

### 2. Matplotlib vs Seaborn

Matplotlib is a general plotting library. Seaborn builds on Matplotlib and offers convenient statistical visualizations.

```python
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [70, 85, 92]
})

df.plot(x="Name", y="Marks", kind="bar")
plt.show()
```

### 3. Pandas vs Scikit-learn

Pandas prepares and explores datasets. Scikit-learn provides tools for machine learning, such as preprocessing, model training, and evaluation.

```python
from sklearn.model_selection import train_test_split

X = df[["Marks"]]
y = df["Marks"] > 80

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)
```

This is only a small illustration of the integration. Real machine learning requires suitable features, targets, and evaluation.

### 4. Pandas vs SQL

SQL is used to query databases. Pandas performs data manipulation in Python.

| SQL | Pandas equivalent |
|---|---|
| `SELECT` | `df[["Name", "Marks"]]` |
| `WHERE` | Boolean filtering |
| `ORDER BY` | `sort_values()` |
| `GROUP BY` | `groupby()` |
| `JOIN` | `merge()` |
| `COUNT()` | `count()` or `size()` depending on the requirement |

These are conceptual equivalents, not exact one-to-one replacements in every situation.

---

## 🔹 5. Pandas Data Structures

Pandas has two fundamental data structures: **Series** and **DataFrame**.

### Series

A Series is a one-dimensional labeled collection of values.

```python
import pandas as pd

marks = pd.Series([85, 72, 91])

print(marks)
```

Output:

```text
0    85
1    72
2    91
dtype: int64
```

Each value has an index.

Create a Series with custom labels:

```python
marks = pd.Series(
    [85, 72, 91],
    index=["Mahesh", "Rahul", "Priya"]
)

print(marks["Mahesh"])
```

Output:

```text
85
```

### DataFrame

A DataFrame is a two-dimensional tabular structure containing rows and columns.

```python
data = {
    "Name": ["Mahesh", "Rahul", "Priya"],
    "Age": [22, 21, 22],
    "Marks": [85, 72, 91]
}

df = pd.DataFrame(data)

print(df)
```

### Series vs DataFrame

| Series | DataFrame |
|---|---|
| One-dimensional | Two-dimensional |
| One labeled sequence | Rows and columns |
| Similar to a single column | Similar to a complete table |

---

## 🔹 6. Creating DataFrames

### From a dictionary

```python
df = pd.DataFrame({
    "Name": ["Mahesh", "Rahul", "Priya"],
    "Age": [22, 21, 22],
    "Marks": [85, 72, 91]
})
```

### From a list of dictionaries

```python
students = [
    {"Name": "Mahesh", "Marks": 85},
    {"Name": "Rahul", "Marks": 72},
    {"Name": "Priya", "Marks": 91}
]

df = pd.DataFrame(students)
```

### From a NumPy array

```python
import numpy as np
import pandas as pd

arr = np.array([
    [1, 80],
    [2, 90],
    [3, 75]
])

df = pd.DataFrame(
    arr,
    columns=["Student_ID", "Marks"]
)
```

---

## 🔹 7. Understanding a Dataset

Create a sample dataset for practice:

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Mahesh", "Rahul", "Priya", "Anu", "Kiran"],
    "Age": [22, 21, 22, np.nan, 23],
    "Department": ["AIML", "CSE", "AIML", "ECE", "CSE"],
    "Marks": [85, 72, 91, 68, 85],
    "City": ["Hyderabad", "Chennai", "Hyderabad", "Pune", "Chennai"]
})
```

### Important inspection methods

| Method | Purpose |
|---|---|
| `df.head()` | First five rows by default |
| `df.tail()` | Last five rows by default |
| `df.sample(3)` | Three randomly sampled rows |
| `df.shape` | Number of rows and columns |
| `df.columns` | Column labels |
| `df.index` | Row index |
| `df.dtypes` | Data type of each column |
| `df.info()` | Structure, data types and non-null counts |
| `df.describe()` | Descriptive statistics for eligible columns |
| `df.nunique()` | Number of distinct values per column |
| `df["Department"].value_counts()` | Frequency of department values |

Examples:

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
print(df.describe())
```

Remember: `shape`, `columns`, `index`, and `dtypes` are attributes, so they are used without parentheses.

---

## 🔹 8. Reading and Writing Files

Pandas supports many formats, including CSV, Excel, JSON, and SQL data sources. <Cite refs={["turn419916search0","turn419916search4"]}/>

### CSV

Read:

```python
df = pd.read_csv("students.csv")
```

Write:

```python
df.to_csv("output.csv", index=False)
```

### Excel

```python
df = pd.read_excel("students.xlsx")
df.to_excel("output.xlsx", index=False)
```

Excel support may require installing `openpyxl` or another compatible Excel engine.

### JSON

```python
df = pd.read_json("students.json")
df.to_json("output.json", orient="records", indent=2)
```

### SQL

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///college.db")

df = pd.read_sql("SELECT * FROM students", engine)
```

This example uses SQLite. Other databases need a suitable SQLAlchemy dialect and database driver.

### Read only specific columns

```python
df = pd.read_csv(
    "students.csv",
    usecols=["Name", "Marks"]
)
```

### Read a limited number of rows

```python
df = pd.read_csv("students.csv", nrows=100)
```

---

## 🔹 9. Selecting Rows and Columns

### Select one column

```python
df["Name"]
```

Returns a Series.

### Select multiple columns

```python
df[["Name", "Marks"]]
```

Returns a DataFrame.

### Using `loc`

`loc` selects using row and column labels.

```python
print(df.loc[0, "Name"])
print(df.loc[0:2, ["Name", "Marks"]])
```

The label slice `0:2` includes label `2`.

### Using `iloc`

`iloc` selects using integer positions.

```python
print(df.iloc[0, 0])
print(df.iloc[0:3, 0:2])
```

The positional slice `0:3` excludes position `3`.

### `loc` vs `iloc`

| `loc` | `iloc` |
|---|---|
| Label-based | Position-based |
| `df.loc[0, "Name"]` | `df.iloc[0, 0]` |
| Label slice includes the end label | Positional slice excludes the end position |

### Select the first three rows

```python
df.head(3)
```

---

## 🔹 10. Filtering Data

Filtering selects rows that satisfy a condition.

### Marks greater than 80

```python
df[df["Marks"] > 80]
```

### Multiple conditions using AND

```python
df[
    (df["Marks"] > 80) &
    (df["Age"] >= 22)
]
```

### Multiple conditions using OR

```python
df[
    (df["City"] == "Chennai") |
    (df["City"] == "Hyderabad")
]
```

### Exclude a condition

```python
df[df["Department"] != "CSE"]
```

### Filter using `isin()`

```python
df[df["Department"].isin(["AIML", "CSE"])]
```

### Filter using `between()`

```python
df[df["Marks"].between(70, 90)]
```

### Filter text using `str.contains()`

```python
df[df["Name"].str.contains("a", case=False, na=False)]
```

### Use `query()`

```python
df.query("Marks > 80")
```

**Important:** Use parentheses around each condition when combining conditions with `&` or `|`. Use `&` and `|`, not Python's `and` and `or`, for element-wise Pandas filtering.

---

## 🔹 11. Adding, Updating and Removing Columns

### Add a column

```python
df["Passed"] = df["Marks"] >= 40
```

### Create a calculated column

```python
df["Bonus_Marks"] = df["Marks"] + 5
```

### Update existing values

```python
df.loc[df["Marks"] < 40, "Marks"] = 40
```

### Rename columns

```python
df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Final_Marks"
})
```

### Remove a column

```python
df = df.drop(columns=["City"])
```

### Remove rows

```python
df = df.drop(index=[0, 1])
```

### Change column order

```python
df = df[["Name", "Department", "Marks", "Age"]]
```

---

## 🔹 12. Sorting Data

### Sort ascending

```python
df.sort_values("Marks")
```

### Sort descending

```python
df.sort_values("Marks", ascending=False)
```

### Sort using multiple columns

```python
df.sort_values(
    ["Department", "Marks"],
    ascending=[True, False]
)
```

### Sort by index

```python
df.sort_index()
```

`sort_values()` sorts by values. `sort_index()` sorts by index labels.

---

## 🔹 13. Handling Missing Values

Missing values can occur because of incomplete forms, failed data collection, or unavailable information.

Pandas commonly represents missing data with values such as `NaN` or `pd.NA`, depending on the data type.

### Detect missing values

```python
df.isna()
```

### Count missing values per column

```python
df.isna().sum()
```

### Count all missing cells

```python
df.isna().sum().sum()
```

### Remove rows with missing values

```python
df.dropna()
```

### Remove columns with missing values

```python
df.dropna(axis=1)
```

### Fill missing values with a fixed value

```python
df["Age"] = df["Age"].fillna(22)
```

### Fill missing numerical values with the mean

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

### Fill missing values with the median

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

### Fill missing categorical values

```python
df["Department"] = df["Department"].fillna("Unknown")
```

### Forward-fill values

```python
df = df.ffill()
```

### Backward-fill values

```python
df = df.bfill()
```

**Interview point:** Mean is sensitive to outliers; median is often more robust. The correct strategy depends on the data and the reason values are missing. For machine learning, calculate imputation values from training data rather than using information from the test set.

---

## 🔹 14. Handling Duplicate Data

### Check duplicate rows

```python
df.duplicated()
```

### Count duplicate rows

```python
df.duplicated().sum()
```

### Remove duplicate rows

```python
df = df.drop_duplicates()
```

### Check duplicates based on one column

```python
df.duplicated(subset=["Name"])
```

### Keep the last occurrence

```python
df = df.drop_duplicates(
    subset=["Name"],
    keep="last"
)
```

Possible `keep` values:

- `"first"` — keep the first occurrence.
- `"last"` — keep the last occurrence.
- `False` — remove all rows that are duplicates within the selected subset.

---

## 🔹 15. Data Type Conversion

Data types determine how values are stored and which operations are available.

### Check types

```python
print(df.dtypes)
```

### Convert to integer

```python
df["Age"] = df["Age"].astype("Int64")
```

`Int64` is Pandas' nullable integer type, which can represent missing values.

### Convert to string

```python
df["Name"] = df["Name"].astype("string")
```

### Convert to numeric safely

```python
df["Marks"] = pd.to_numeric(
    df["Marks"],
    errors="coerce"
)
```

Invalid values become missing values when `errors="coerce"` is used.

### Convert to datetime

```python
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)
```

### Convert to category

```python
df["Department"] = df["Department"].astype("category")
```

Categorical data can be useful for columns containing a limited set of repeated labels.

---

## 🔹 16. String Operations

Pandas provides the `.str` accessor for vectorized string operations.

### Convert text to lowercase

```python
df["Name"] = df["Name"].str.lower()
```

### Convert text to uppercase

```python
df["Name"] = df["Name"].str.upper()
```

### Remove leading and trailing spaces

```python
df["Name"] = df["Name"].str.strip()
```

### Replace text

```python
df["Name"] = df["Name"].str.replace(
    "Mahesh",
    "Mahesh Babu",
    regex=False
)
```

### Find string length

```python
df["Name_Length"] = df["Name"].str.len()
```

### Check whether a value contains text

```python
df["Name"].str.contains(
    "mah",
    case=False,
    na=False
)
```

### Split text

```python
df["Full_Name"] = df["Name"].str.split()
```

---

## 🔹 17. Statistical Operations

Pandas makes it easy to calculate descriptive statistics.

| Function | Purpose |
|---|---|
| `sum()` | Sum |
| `mean()` | Average |
| `median()` | Middle value |
| `mode()` | Most frequent value(s) |
| `min()` | Minimum |
| `max()` | Maximum |
| `count()` | Count of non-missing values |
| `size` | Number of elements in a group |
| `std()` | Standard deviation |
| `var()` | Variance |
| `quantile()` | Quantiles |
| `nunique()` | Number of unique values |

Examples:

```python
print(df["Marks"].sum())
print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].min())
print(df["Marks"].max())
print(df["Marks"].std())
```

### Find the highest-scoring row

```python
df.loc[df["Marks"].idxmax()]
```

### Find the lowest-scoring row

```python
df.loc[df["Marks"].idxmin()]
```

### Count each department

```python
df["Department"].value_counts()
```

**Important:** `count()` excludes missing values. `size` counts rows regardless of missing values in the selected column.

---

## 🔹 18. GroupBy and Aggregation

`groupby()` divides data into groups so that calculations can be performed for each group.

This is commonly called **split–apply–combine**. <Cite refs={["turn419916search8"]}/>

### Average marks by department

```python
df.groupby("Department")["Marks"].mean()
```

### Multiple statistics

```python
df.groupby("Department")["Marks"].agg(
    ["mean", "min", "max", "count"]
)
```

### Group by multiple columns

```python
df.groupby(
    ["Department", "City"]
)["Marks"].mean()
```

### Named aggregation

```python
summary = df.groupby("Department").agg(
    Average_Marks=("Marks", "mean"),
    Highest_Marks=("Marks", "max"),
    Student_Count=("Name", "count")
)
```

### Keep groups as ordinary columns

```python
df.groupby(
    "Department",
    as_index=False
)["Marks"].mean()
```

### Difference between `count()` and `size()`

```python
df.groupby("Department").size()
```

- `count()` counts non-missing values in a column.
- `size()` counts rows in each group.

**SQL connection:**

```sql
SELECT Department, AVG(Marks)
FROM Students
GROUP BY Department;
```

Equivalent Pandas concept:

```python
df.groupby("Department")["Marks"].mean()
```

---

## 🔹 19. Combining Datasets

Pandas offers `concat()`, `merge()`, and `join()` for combining data.

### `concat()`

Stacks or combines DataFrames along an axis.

```python
df1 = pd.DataFrame({
    "Name": ["Mahesh", "Rahul"]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Anu"]
})

combined = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

### `merge()`

Combines tables using matching key columns.

```python
students = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Mahesh", "Rahul", "Priya"]
})

scores = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [85, 72, 91]
})

result = pd.merge(
    students,
    scores,
    on="Student_ID",
    how="inner"
)
```

### Types of joins

| Join | Meaning |
|---|---|
| `inner` | Keep matching keys in both tables |
| `left` | Keep all left-table keys |
| `right` | Keep all right-table keys |
| `outer` | Keep keys from both tables |

Example:

```python
result = pd.merge(
    students,
    scores,
    on="Student_ID",
    how="left"
)
```

### `join()`

Useful for combining DataFrames using their indexes by default.

```python
left = students.set_index("Student_ID")
right = scores.set_index("Student_ID")

result = left.join(
    right[["Marks"]],
    how="left"
)
```

### `concat()` vs `merge()` vs `join()`

- `concat()` combines objects along rows or columns.
- `merge()` combines based on matching key columns or indexes.
- `join()` is a convenient DataFrame method, especially for index-based joins.

---

## 🔹 20. Reshaping Data

Reshaping changes how data is organized.

### `pivot()`

Changes long-format data to wide format when each index/column combination uniquely identifies a value.

```python
df.pivot(
    index="Name",
    columns="Subject",
    values="Marks"
)
```

### `pivot_table()`

Similar to `pivot()`, but can aggregate duplicate combinations.

```python
df.pivot_table(
    index="Department",
    values="Marks",
    aggfunc="mean"
)
```

### `melt()`

Converts wide-format data into long-format data.

```python
wide = pd.DataFrame({
    "Name": ["Mahesh", "Rahul"],
    "Maths": [80, 70],
    "Science": [90, 85]
})

long = wide.melt(
    id_vars="Name",
    var_name="Subject",
    value_name="Marks"
)
```

### `transpose()`

Switches rows and columns.

```python
df.T
```

### `reset_index()`

Moves index information back into columns and creates a default index.

```python
df = df.reset_index()
```

### `set_index()`

Sets one or more columns as the index.

```python
df = df.set_index("Name")
```

---

## 🔹 21. Date and Time Operations

### Convert a column to datetime

```python
df["Date"] = pd.to_datetime(df["Date"])
```

### Extract year, month and day

```python
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
```

### Filter records after a date

```python
df[df["Date"] >= "2026-01-01"]
```

### Sort by date

```python
df = df.sort_values("Date")
```

### Calculate time differences

```python
df["Duration"] = df["End_Date"] - df["Start_Date"]
```

### Resample time-series data

For a DataFrame with a datetime index:

```python
monthly_sales = df["Sales"].resample("MS").sum()
```

Here, `"MS"` means month start. Resampling requires an appropriate datetime-like index or a datetime column selected through the relevant time-series options.

---

## 🔹 22. Apply, Map and Lambda

These tools help transform values or apply functions.

### `map()` on a Series

```python
df["Department_Code"] = df["Department"].map({
    "AIML": 1,
    "CSE": 2,
    "ECE": 3
})
```

Values absent from the mapping become missing.

### `apply()` on a Series

```python
df["Marks_Double"] = df["Marks"].apply(
    lambda x: x * 2
)
```

### `apply()` on a DataFrame

```python
df[["Age", "Marks"]].apply(
    lambda column: column.max()
)
```

### Vectorized alternative

Instead of:

```python
df["Marks_Double"] = df["Marks"].apply(
    lambda x: x * 2
)
```

Prefer:

```python
df["Marks_Double"] = df["Marks"] * 2
```

For common numerical operations, vectorized expressions are usually simpler and often faster.

---

## 🔹 23. Exploratory Data Analysis (EDA)

**EDA** stands for **Exploratory Data Analysis**.

It means examining a dataset to understand its structure, quality, patterns, and relationships before drawing conclusions or building a model.

### Basic EDA checklist

```python
# 1. Inspect the first rows
print(df.head())

# 2. Check the dataset size
print(df.shape)

# 3. Inspect column types and non-null values
df.info()

# 4. Calculate descriptive statistics
print(df.describe(include="all"))

# 5. Check missing values
print(df.isna().sum())

# 6. Check duplicate rows
print(df.duplicated().sum())

# 7. Check distinct values
print(df.nunique())

# 8. Check category frequencies
print(df["Department"].value_counts())

# 9. Check numerical correlations
print(df.select_dtypes(include="number").corr())
```

### Questions EDA should answer

- How many rows and columns exist?
- Which columns contain missing values?
- Are there duplicate records?
- What are the data types?
- Which categories occur most often?
- What are the average, minimum and maximum values?
- Are there unusual values or possible outliers?
- Which numerical variables may be related?

EDA helps identify issues; it does not automatically prove causation or determine whether a result is statistically significant.

---

## 🔹 24. Data Visualization

Pandas includes basic plotting methods that use Matplotlib.

### Line chart

```python
df.plot(x="Date", y="Sales", kind="line")
```

### Bar chart

```python
df.plot(x="Name", y="Marks", kind="bar")
```

### Histogram

```python
df["Marks"].plot(kind="hist", bins=10)
```

### Box plot

```python
df[["Marks"]].plot(kind="box")
```

### Seaborn example

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(
    data=df,
    x="Age",
    y="Marks",
    hue="Department"
)

plt.show()
```

Visualizations can help reveal distributions, trends, group differences, and potential outliers.

---

## 🔹 25. Pandas with NumPy and SQL

### Pandas with NumPy

Convert a Series to a NumPy array:

```python
import numpy as np

values = df["Marks"].to_numpy()
```

Calculate a numerical operation:

```python
print(np.mean(values))
```

Create a column using a NumPy condition:

```python
df["Result"] = np.where(
    df["Marks"] >= 40,
    "Pass",
    "Fail"
)
```

### Pandas with SQL

Read query results:

```python
df = pd.read_sql(
    "SELECT * FROM Students",
    engine
)
```

Write data to a database table:

```python
df.to_sql(
    "Student_Results",
    engine,
    if_exists="replace",
    index=False
)
```

**Important:** `if_exists="replace"` replaces the existing table. Use it carefully when the table contains important data.

---

## 🔹 26. Pandas with Machine Learning

Pandas is often used to load and prepare data before training a machine learning model.

Typical workflow:

```text
CSV Dataset
    ↓
Pandas
    ↓
Inspect and Clean Data
    ↓
Select Features and Target
    ↓
Train/Test Split
    ↓
Scikit-learn Model
    ↓
Evaluate Results
```

Example:

```python
from sklearn.model_selection import train_test_split

X = df[["Age", "Marks"]]
y = df["Marks"] >= 40

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

This is a demonstration of how to split features and labels, not a meaningful predictive model because the example target is derived from `Marks`, which is also included as a feature.

For real ML projects, choose the correct target, prevent data leakage, preprocess features appropriately, and evaluate the model using suitable metrics.

### Common Pandas operations in ML projects

- `read_csv()` — load data.
- `dropna()` / `fillna()` — handle missing values.
- `drop_duplicates()` — remove duplicate rows.
- `get_dummies()` — one-hot encode categorical values.
- `select_dtypes()` — select columns by data type.
- `to_numpy()` — convert to a NumPy array.
- `merge()` — combine features from multiple sources.

---

## 🔹 27. Performance and Best Practices

### 1. Avoid unnecessary row-by-row loops

Prefer:

```python
df["Total"] = df["Price"] * df["Quantity"]
```

over manually iterating through every row for this simple calculation.

### 2. Select only the required columns

```python
df = pd.read_csv(
    "large_dataset.csv",
    usecols=["Name", "Marks"]
)
```

### 3. Inspect data before cleaning

```python
df.info()
print(df.isna().sum())
print(df.duplicated().sum())
```

### 4. Avoid chained assignment

Prefer:

```python
df.loc[df["Marks"] < 40, "Marks"] = 40
```

rather than trying to modify a filtered temporary DataFrame.

### 5. Preserve the original data when needed

```python
clean_df = df.copy()
```

### 6. Validate merge results

```python
result = pd.merge(
    students,
    scores,
    on="Student_ID",
    how="left",
    validate="one_to_one"
)
```

Use the validation mode that matches the actual relationship between your keys.

### 7. Be careful with missing data

Do not automatically fill every missing numerical value with zero. Decide based on what the missing value represents.

### 8. Be careful with large datasets

Read only required columns, choose appropriate data types, and consider tools such as Polars or Dask when their execution model fits the workload.

---

## 🔹 28. Common Errors

### `KeyError`

Example:

```python
df["Mark"]
```

when the actual column is named `"Marks"`.

**Fix:**

```python
print(df.columns)
```

### `FileNotFoundError`

The requested file cannot be found at the specified path.

**Fix:** Check the working directory and file path.

### `ValueError` during type conversion

A column contains values that cannot be converted to the requested type.

**Fix:**

```python
df["Marks"] = pd.to_numeric(
    df["Marks"],
    errors="coerce"
)
```

Then inspect the resulting missing values.

### Incorrect filtering

Incorrect:

```python
df[df["Marks"] > 80 and df["Age"] >= 22]
```

Correct:

```python
df[
    (df["Marks"] > 80) &
    (df["Age"] >= 22)
]
```

### Merge creates more rows than expected

This can happen when a join key occurs multiple times in one or both tables.

**Fix:** Check key uniqueness, understand the relationship between tables, and use `validate=` when appropriate.

---

## 🔹 29. Interview Questions and Answers

### Beginner Questions

**1. What is Pandas?**

Pandas is an open-source Python library used for data manipulation and analysis. It provides data structures such as Series and DataFrame and makes it easy to clean, filter, group, and analyze structured data.

**2. Why is Pandas used in data science?**

Pandas helps load datasets, inspect their quality, handle missing values, calculate statistics, and prepare data for visualization and machine learning.

**3. What is a Series?**

A Series is a one-dimensional labeled data structure that stores values with an associated index.

**4. What is a DataFrame?**

A DataFrame is a two-dimensional labeled table consisting of rows and columns. Its columns can have different data types.

**5. What is the difference between a Series and a DataFrame?**

A Series is one-dimensional, while a DataFrame is two-dimensional and can contain multiple columns.

**6. How do you read a CSV file?**

```python
df = pd.read_csv("data.csv")
```

**7. How do you display the first five rows?**

```python
df.head()
```

**8. How do you check the number of rows and columns?**

```python
df.shape
```

**9. How do you inspect column data types?**

```python
df.dtypes
```

**10. What is the difference between `loc` and `iloc`?**

`loc` selects by labels, while `iloc` selects by integer positions.

### Intermediate Questions

**11. How do you handle missing values?**

Use `isna()` to detect them, `dropna()` to remove rows or columns, and `fillna()` to replace missing values using a suitable strategy.

**12. What is the difference between `dropna()` and `fillna()`?**

`dropna()` removes selected rows or columns containing missing values. `fillna()` replaces missing values.

**13. How do you remove duplicate rows?**

```python
df.drop_duplicates()
```

**14. What is `groupby()`?**

`groupby()` divides records into groups so that we can calculate statistics or apply transformations for each group.

**15. What is the difference between `merge()` and `concat()`?**

`merge()` combines data based on matching keys or indexes. `concat()` combines objects along rows or columns.

**16. What is the difference between `count()` and `size()`?**

`count()` counts non-missing values in a column. `size()` counts the number of rows in a group.

**17. What is the difference between `sort_values()` and `sort_index()`?**

`sort_values()` sorts by data values, while `sort_index()` sorts by index labels.

**18. How do you select rows using multiple conditions?**

```python
df[
    (df["Marks"] > 80) &
    (df["Age"] >= 22)
]
```

**19. What is `apply()`?**

`apply()` applies a function along a Series or along an axis of a DataFrame.

**20. What is `value_counts()`?**

It counts occurrences of distinct values in a Series.

### Advanced Questions

**21. What is vectorization?**

Vectorization means applying operations to entire arrays or columns rather than manually iterating through individual elements. It often produces clearer and faster numerical code.

**22. What is the difference between `pivot()` and `pivot_table()`?**

`pivot()` requires unique combinations of the selected index and column keys. `pivot_table()` can aggregate duplicate combinations using functions such as `mean` or `sum`.

**23. What is `melt()` used for?**

`melt()` converts wide-format data into long-format data by turning selected columns into rows.

**24. How do you detect outliers?**

You can inspect distributions, use box plots, or calculate interquartile ranges. A statistical rule flags potential outliers; domain knowledge is needed to decide whether they are errors.

**25. How do you optimize Pandas code?**

Select only required columns, use vectorized operations, choose appropriate data types, avoid unnecessary loops, and process large files in chunks where appropriate.

**26. How do you prevent data leakage during machine learning preprocessing?**

Split the dataset first, fit preprocessing steps using training data only, and then apply the fitted transformations to validation or test data.

**27. What is the difference between Pandas and NumPy?**

Pandas focuses on labeled tabular data and provides operations for rows, columns, missing values, and grouping. NumPy focuses on efficient numerical arrays and mathematical computing.

**28. Can Pandas read data from SQL?**

Yes. Functions such as `read_sql()` can read query results using a supported database connection.

**29. What is `reset_index()`?**

It resets the DataFrame index, normally creating a default integer index and optionally placing the previous index into a column.

**30. What is the difference between `map()` and `apply()`?**

`map()` is commonly used to transform values in a Series, including dictionary-based mapping. `apply()` is more general and can apply a function to a Series or along a DataFrame axis.

---

## 🔹 30. Coding Practice Questions

Try solving these using Pandas.

### Beginner

1. Create a DataFrame containing five students and their marks.
2. Display the first three rows.
3. Select only the `Name` and `Marks` columns.
4. Filter students who scored more than 80.
5. Sort students by marks in descending order.
6. Calculate the average marks.
7. Count students in each department.
8. Find the maximum and minimum marks.
9. Add a `Result` column based on a passing score.
10. Rename a column.

### Intermediate

11. Find and count missing values.
12. Fill missing marks using the median.
13. Remove duplicate student records.
14. Find the top three students by marks.
15. Group students by department and calculate average marks.
16. Merge student details with a separate marks table.
17. Convert a date column to datetime.
18. Extract the year and month from a date column.
19. Find names containing a specified character.
20. Convert a DataFrame from wide format to long format.

### Advanced

21. Analyze monthly sales and find the highest-sales month.
22. Calculate each department's percentage of total sales.
23. Compare inner, left, right, and outer joins on sample tables.
24. Find potential outliers using the IQR method.
25. Create a pivot table summarizing sales by region and product.
26. Read a large CSV file in chunks.
27. Import data from SQL and summarize it with Pandas.
28. Prepare a dataset for a Scikit-learn model while avoiding data leakage.
29. Create a reusable data-cleaning function.
30. Perform a complete EDA workflow on a real dataset.

---

## 🔹 31. Mini Projects

### Project 1: Student Performance Analysis

**Tasks:**

- Load student records.
- Handle missing values.
- Calculate average marks.
- Find the top-performing students.
- Compare departments.
- Export the summary to CSV.

### Project 2: Sales Data Analysis

**Tasks:**

- Load sales data.
- Convert date columns.
- Calculate total revenue.
- Find best-selling products.
- Group revenue by region.
- Visualize monthly trends.

### Project 3: Employee Data Analysis

**Tasks:**

- Clean employee records.
- Identify duplicate rows.
- Analyze department-wise salaries.
- Calculate average salary.
- Examine missing values.
- Export a cleaned dataset.

### Project 4: E-Commerce Analysis

**Tasks:**

- Analyze orders and products.
- Merge multiple tables.
- Calculate total order values.
- Identify repeat customers.
- Find top products.
- Build charts for business insights.

### Project 5: Machine Learning Data Preparation

**Tasks:**

- Load a public dataset.
- Inspect data types and missing values.
- Identify numerical and categorical features.
- Split training and test data.
- Build preprocessing pipelines.
- Train a basic Scikit-learn model.
- Evaluate the model using appropriate metrics.

---

## 🔹 32. Learning Roadmap

### Level 1 — Fundamentals

- Series and DataFrame
- Creating DataFrames
- Reading CSV and Excel
- `head()`, `tail()`, `shape`, `info()`
- Selecting columns
- `loc` and `iloc`

### Level 2 — Data Manipulation

- Filtering
- Sorting
- Adding and removing columns
- Renaming
- Type conversion
- String operations

### Level 3 — Data Cleaning

- Missing values
- Duplicate records
- Invalid data
- Outlier investigation
- Data validation

### Level 4 — Data Analysis

- Descriptive statistics
- `groupby()`
- Aggregation
- `merge()`
- `concat()`
- `pivot_table()`
- Date/time operations

### Level 5 — Data Science Integration

- NumPy
- Matplotlib
- Seaborn
- SQL
- Scikit-learn
- EDA
- Machine learning preprocessing

### Level 6 — Projects and Interview Preparation

- Solve coding questions
- Analyze real datasets
- Build mini projects
- Explain why you chose each operation
- Practice interview answers aloud
- Document your projects on GitHub

---

## 🔹 33. Quick Revision Cheat Sheet

| Task | Pandas operation |
|---|---|
| Import Pandas | `import pandas as pd` |
| Read CSV | `pd.read_csv("file.csv")` |
| Read Excel | `pd.read_excel("file.xlsx")` |
| First five rows | `df.head()` |
| Last five rows | `df.tail()` |
| Dataset dimensions | `df.shape` |
| Column types | `df.dtypes` |
| Dataset overview | `df.info()` |
| Summary statistics | `df.describe()` |
| Select one column | `df["Name"]` |
| Select multiple columns | `df[["Name", "Marks"]]` |
| Select by label | `df.loc[...]` |
| Select by position | `df.iloc[...]` |
| Filter records | `df[df["Marks"] > 80]` |
| Sort values | `df.sort_values("Marks")` |
| Missing values | `df.isna()` |
| Fill missing values | `df.fillna(...)` |
| Remove missing values | `df.dropna()` |
| Remove duplicates | `df.drop_duplicates()` |
| Count categories | `df["Department"].value_counts()` |
| Group records | `df.groupby("Department")` |
| Combine tables by key | `pd.merge(...)` |
| Stack DataFrames | `pd.concat(...)` |
| Reshape wide to long | `df.melt(...)` |
| Save CSV | `df.to_csv("out.csv", index=False)` |
| Convert to datetime | `pd.to_datetime(...)` |
| Export to Excel | `df.to_excel("out.xlsx", index=False)` |

---

## 🔹 34. Official Learning Resources

Use the official documentation when you need the complete explanation of a function or more examples.

- [Pandas — Getting Started](https://pandas.pydata.org/docs/getting_started/)
- [Pandas — User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Pandas — 10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas — API Reference](https://pandas.pydata.org/docs/reference/index.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---

## 📌 Final Takeaways

- **Pandas** is primarily for tabular data manipulation and analysis.
- **NumPy** is primarily for numerical arrays and mathematical operations.
- **Matplotlib, Seaborn, and Plotly** are used for visualization.
- **Scikit-learn** is used for machine learning.
- **SQL** is useful for querying databases, and Pandas can process the returned data.
- **EDA** helps you understand data before modeling.
- Learn the important functions by using them on real datasets rather than memorizing their names alone.

**Recommended goal:** Complete one student-analysis project, one sales-analysis project, and one EDA project before moving to advanced Pandas and machine learning workflows.