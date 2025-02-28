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
├── Dashboard/
│   ├── 3d Novri.jpg                 # Image asset
│   ├── dashboard_customer.py        # Streamlit dashboard script
│
├── E-Commerce Dataset/
│   ├── customers_dataset.csv        # Customer data
│   ├── geolocation_dataset.csv      # Location data
│   ├── order_items_dataset.csv      # Order details
│   ├── order_payments_dataset.csv   # Payment details
│   ├── order_reviews_dataset.csv    # Customer reviews
│   ├── orders_dataset.csv           # Order information
│   ├── product_category_name.csv    # Product categories
│   ├── products_dataset.csv         # Product details
│   ├── sellers_dataset.csv          # Seller details
│
├── Analisis_data_eCommerce.ipynb     # Jupyter Notebook for data analysis
├── all_dataset.csv                   # Combined dataset
├── README.md                          # Project documentation
├── Requirements.txt                    # Dependencies for the project
```

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/NovrianPratama/personal-project.git
```

2. Go to the project directory

```
cd "Analisis Data Customer E-Commerce"
```

3. Install the required Python packages by running:

```
pip install -r requirements.txt
```

## Usage

### Running the Streamlit Dashboard

```sh
cd Dashboard
streamlit run dashboard_customer.py
```

Access the dashboard in your web browser at `http://localhost:8502`.

### Data Analysis

1. **Data Wrangling**: Use `Analisis_data_eCommerce.ipynb` to clean and preprocess the data.
2. **Exploratory Data Analysis (EDA)**: Perform RFM segmentation, sales analysis, and delivery performance evaluation.
3. **Visualization**: Insights are presented interactively in the Streamlit dashboard.

## Data Sources

This project uses the E-Commerce Public Dataset from [Dicoding's Data Analysis Course](https://www.dicoding.com/).

---

📌 **Note:** Feel free to contribute and enhance this project by adding more features and insights! 🚀
