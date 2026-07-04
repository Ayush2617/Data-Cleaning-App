# Data Cleaning App

A Python-based data preprocessing tool powered by the **Data Clean Master** engine that automates dataset cleaning by handling duplicate records and missing values. The application helps transform raw datasets into analysis-ready data within seconds, making it useful for data analysis, machine learning, and business intelligence workflows.

---

## Project Overview

Data Cleaning App is designed to simplify one of the most important stages of the data analytics pipeline: **data preprocessing**.

The application accepts CSV and Excel datasets, validates file paths, identifies duplicate records, handles missing values intelligently, and exports a cleaned dataset ready for further analysis.

The core cleaning functionality is implemented through the **Data Clean Master** function, which performs all cleaning operations automatically. The script supports large datasets and provides a simple command-line interface for easy usage.

---

## Features

✅ Supports CSV and Excel datasets

✅ File path validation before processing

✅ Duplicate record detection and removal

✅ Backup generation for duplicate records

✅ Missing value analysis and reporting

✅ Mean imputation for numeric columns

✅ Automatic removal of rows containing missing values in non-numeric columns

✅ Export of cleaned datasets

✅ Interactive command-line workflow

✅ Fast processing for large datasets

---

## Tech Stack

* Python
* Pandas
* NumPy
* OpenPyXL
* xlrd
* OS Module
* Time Module

---

## How It Works

### 1. Dataset Validation

* Accepts dataset path and dataset name from the user.
* Verifies whether the specified file exists.
* Validates supported file formats (CSV and Excel).

### 2. Data Loading

* Loads CSV files using Pandas.
* Loads Excel files using Pandas Excel Reader.

### 3. Duplicate Detection

* Identifies duplicate records.
* Saves duplicate entries separately.
* Removes duplicate rows from the main dataset.

### 4. Missing Value Handling

* Numeric columns:

  * Missing values are replaced using the column mean.
* Non-numeric columns:

  * Rows containing missing values are removed.

### 5. Data Export

* Generates a cleaned dataset.
* Saves the cleaned file automatically.
* Displays completion messages and dataset statistics.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Ayush2617/Data-Cleaning-App.git
```

Move to the project directory:

```bash
cd Data-Cleaning-App
```

Install required dependencies:

```bash
pip install pandas numpy openpyxl xlrd
```

---

## Usage

Run the application:

```bash
python app.py
```

Example:

```text
Welcome to Data Cleaning Master!

Please enter dataset path:
C:/Users/Ayush/Desktop/sales_data.csv

Please enter dataset name:
sales_data
```

Output:

```text
Dataset is csv !
Dataset has total duplicates record: 25
Dataset has total missing values: 18

Congratulations!
Your Dataset is clean now.

Your Dataset is Saved.
```

---

## Project Structure

```text
Data-Cleaning-App
│
├── app.py
├── sample_dataset.csv
├── cleaned_dataset.csv
├── duplicate_records.csv
├── README.md
└── requirements.txt
```

---


## Learning Outcomes

Through this project, I gained practical experience in:

* Data Cleaning and Preprocessing
* Pandas Data Manipulation
* File Handling in Python
* Data Quality Assessment
* Automation of Data Preparation Tasks
* Building Real-World Python Applications

---

## Future Improvements

* Streamlit-based GUI
* Data Profiling Dashboard
* Outlier Detection
* Automated Data Quality Reports
* Additional File Format Support
* Logging and Error Reporting

---

## Author

### Ayush Pratap Singh

B.Tech Graduate | Aspiring Data Analyst

#### Connect With Me

* GitHub: https://github.com/Ayush2617
* LinkedIn: https://www.linkedin.com/in/ayushpratapsingh2612/

#### Skills

Python • SQL • Excel • Power BI • Pandas • Data Analysis • Data Cleaning • Data Visualization

---

If you found this project useful, consider giving it a ⭐ on GitHub.
