# E-Commerce Customer Data Analysis Dashboard

![E-Commerce Data Dashboard](dashboard.gif)

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)

## Overview

This project is a data analysis and visualization project focused on e-commerce customer data. It includes data wrangling, exploratory data analysis (EDA), and an interactive Streamlit dashboard to visualize insights. The main objective is to analyze customer behavior using RFM segmentation, sales trends, and delivery performance.

## Project Structure

```
├── dashboard.py          # Main Streamlit dashboard script
├── data/                 # Directory containing raw CSV data files
├── notebook.ipynb        # Jupyter Notebook for data analysis
├── requirements.txt      # Dependencies for the project
├── README.md             # Documentation file
```

## Installation

### Setup Environment - Anaconda

```sh
conda create --name ecom-analysis python=3.9
conda activate ecom-analysis
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal

```sh
mkdir ecom_analysis_project
cd ecom_analysis_project
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Usage

### Running the Streamlit Dashboard

```sh
streamlit run dashboard.py
```

Access the dashboard in your web browser at `http://localhost:8501`.

### Data Analysis

1. **Data Wrangling**: Use `notebook.ipynb` to clean and preprocess the data.
2. **Exploratory Data Analysis (EDA)**: Perform RFM segmentation, sales analysis, and delivery performance evaluation.
3. **Visualization**: Insights are presented interactively in the Streamlit dashboard.

## Data Sources

This project uses the E-Commerce Public Dataset from [Dicoding's Data Analysis Course](https://www.dicoding.com/).

---

📌 **Note:** Feel free to contribute and enhance this project by adding more features and insights!
