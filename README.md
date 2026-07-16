<p align="center">
  <img src="images/banner.png" alt="End-to-End Data Engineering Pipeline Banner" width="100%">
</p>

# End-to-End Crypto Data Engineering Pipeline

## Overview

This project demonstrates the design and implementation of an end-to-end ETL (Extract, Transform, Load) pipeline using Python, PostgreSQL, and SQL.

The pipeline extracts historical cryptocurrency market data from a Kaggle dataset, performs data cleaning and transformation using Pandas, loads the processed data into PostgreSQL, and executes SQL queries for validation and analysis.

The objective of this project is to demonstrate practical data engineering concepts including data ingestion, transformation, database loading, and analytical querying.

---

## Architecture

<p align="center">
  <img src="images/architecture.png" alt="Architecture Diagram" width="850">
</p>

---

## Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Database | PostgreSQL |
| Database Management | pgAdmin 4 |
| ORM | SQLAlchemy |
| Query Language | SQL |
| Version Control | Git |
| Repository Hosting | GitHub |
| Development Environment | VS Code |

---

## Project Structure

```text
Data Engineering Pipeline/
│
├── Dashboard/
│
├── Data/
│   ├── Raw_Data.csv
│   └── Clean_Data.csv
│
├── Scripts/
│   ├── 01_extract.py
│   ├── 02_transform.py
│   └── 03_load.py
│
├── SQL/
│   ├── create_tables.sql
│   └── analysis.sql
│
├── images/
│   ├── banner.png
│   └── architecture.png
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ETL Workflow

### Extract

- Load cryptocurrency historical market data from a CSV dataset.
- Validate dataset availability.
- Inspect the dataset structure.

### Transform

- Remove duplicate records.
- Handle missing values.
- Convert the `date` column to the appropriate data type.
- Save the cleaned dataset.

### Load

- Connect to PostgreSQL using SQLAlchemy.
- Load the cleaned dataset into PostgreSQL.
- Verify successful data ingestion.

---

## Database Schema

| Column | Data Type |
|----------|-----------|
| id | SERIAL PRIMARY KEY |
| date | DATE |
| price | DECIMAL(18,8) |
| total_volume | BIGINT |
| market_cap | BIGINT |
| coin_name | VARCHAR(100) |

---

## SQL Analysis

The following SQL queries were executed to validate and analyze the dataset:

- Count total records
- Retrieve the highest cryptocurrency price
- Retrieve the lowest cryptocurrency price
- Calculate the average price
- Display sample records

Example:

```sql
SELECT COUNT(*) FROM crypto_prices;

SELECT MAX(price) FROM crypto_prices;

SELECT AVG(price) FROM crypto_prices;
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/end-to-end-crypto-data-pipeline.git
```

Navigate into the project directory.

```bash
cd end-to-end-crypto-data-pipeline
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Pipeline

Execute the scripts in the following order.

```bash
python scripts/01_extract.py
python scripts/02_transform.py
python scripts/03_load.py
```

---

## Sample Output

After running the pipeline:

- Raw dataset successfully extracted.
- Data cleaned and transformed.
- Clean dataset generated.
- Data loaded into PostgreSQL.
- SQL validation completed successfully.

---

## Skills Demonstrated

- ETL Pipeline Development
- Data Cleaning and Transformation
- PostgreSQL Database Design
- SQL Querying
- Python Programming
- Data Validation
- Logging and Error Handling
- Git Version Control
- Project Documentation

---

## Future Improvements

- Automate the pipeline using Apache Airflow
- Containerize the application with Docker
- Integrate AWS S3 for data storage
- Schedule automated pipeline execution
- Develop an interactive dashboard using Streamlit or Power BI

---

## Author

**Patience Ramaboe**

Aspiring Data Engineer

LinkedIn: *(Add your LinkedIn URL)*

GitHub: *(Add your GitHub URL)*