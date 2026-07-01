# internship_project
# Olist E-Commerce Data Warehouse

##  Project Overview

This project implements an end-to-end Data Warehouse for the Olist E-Commerce dataset using the **Medallion Architecture (Bronze, Silver, and Gold)**. The pipeline was built using **Snowflake SQL**,and visualized using **Tableau** to generate business insights.

---

## Tools & Technologies

- Snowflake
- SQL (Snowflake SQL )
- Tableau
- GitHub
- Kaggle (Dataset)

---

## Architecture

The project follows the **Medallion Architecture**:

```
Raw Data
    │
    ▼
 Bronze Layer
    │
    ▼
 Silver Layer
    │
    ▼
 Gold Layer
    │
    ▼
Tableau Dashboards


---

Bronze Layer

The Bronze layer stores raw data from the Olist dataset without modifications.

Activities:
- Data ingestion
- Null value checks
- Duplicate checks
- Data quality validation

---

Silver Layer

The Silver layer cleans and transforms the raw data.

Activities:
- Handle missing values using `COALESCE()`
- Standardize data
- Create cleaned tables
- Improve data quality

---

Gold Layer

The Gold layer is designed for analytics using a Star Schema.

Tables Created:
- DIM_CUSTOMER
- DIM_PRODUCT
- DIM_SELLER
- DIM_REVIEW
- FACT_SALES
- PROFIT_ANALYSIS (View)

---

Tableau Dashboards

1.Sales Dashboard
- Total Sales
- Total Orders
- Monthly Sales Trend
- Product Performance
- Payment Type Analysis

2. Customer Insights

3.Profit Dashboard
- Total Revenue
- Estimated Cost
- Estimated Profit
- Profit Margin
- Revenue vs Profit
- Monthly Profit Trend


---

SQL Concepts Used:

- SELECT
- JOIN & LEFT JOIN
- GROUP BY
- COALESCE
- CASE
- SUM, COUNT, AVG
- ROW_NUMBER()
- CREATE TABLE
- CREATE VIEW

---

Key Learning Outcomes:

- Data Warehousing
- Medallion Architecture
- ETL Pipeline Development
- Star Schema Modeling
- SQL Data Transformation
- Tableau Dashboard Development


---

Author

ABITHASHRI PS


