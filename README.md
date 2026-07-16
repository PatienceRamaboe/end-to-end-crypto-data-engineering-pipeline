<div align="center">

# End-to-End Crypto Data Engineering Pipeline

An end-to-end ETL pipeline that extracts, transforms, and loads cryptocurrency market data into PostgreSQL using Python.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

</div>

---

## Overview

This project demonstrates the implementation of an end-to-end **ETL (Extract, Transform, Load)** pipeline using Python, PostgreSQL, and SQL.

The pipeline reads historical cryptocurrency market data from a Kaggle dataset, performs data cleaning and transformation with Pandas, loads the processed data into PostgreSQL, and validates the results using SQL queries.

The goal of this project is to demonstrate practical data engineering skills including data ingestion, transformation, relational database loading, and SQL analysis.

---

## Features

- Extract cryptocurrency data from a CSV dataset
- Validate dataset availability
- Clean and transform raw data
- Remove duplicate records
- Handle missing values
- Convert data types
- Load processed data into PostgreSQL
- Execute SQL queries for validation and analysis
- Logging and basic error handling
- Modular ETL architecture

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Data Processing | Pandas |
| Database | PostgreSQL |
| Database Administration | pgAdmin 4 |
| ORM | SQLAlchemy |
| Query Language | SQL |
| Version Control | Git |
| Repository Hosting | GitHub |
| IDE | Visual Studio Code |

---

## Project Structure

```text
end-to-end-crypto-data-engineering-pipeline/
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
├── Dashboard/
│
├── README.md
├── Requirements.txt
└── .gitignore
```

---

## ETL Workflow

```text
Kaggle Dataset
       │
       ▼
Raw_Data.csv
       │
       ▼
01_extract.py
       │
       ▼
02_transform.py
       │
       ▼
Clean_Data.csv
       │
       ▼
03_load.py
       │
       ▼
PostgreSQL
       │
       ▼
SQL Analysis
```

---

## Database Schema

| Column | Data Type |
|---------|-----------|
| id | SERIAL PRIMARY KEY |
| date | DATE |
| price | DECIMAL(18,8) |
| total_volume | BIGINT |
| market_cap | BIGINT |
| coin_name | VARCHAR(100) |

---

## SQL Validation

The following SQL queries were used to validate and analyze the loaded dataset.

### Count Total Records

```sql
SELECT COUNT(*)
FROM crypto_prices;
```

### Highest Cryptocurrency Price

```sql
SELECT MAX(price)
FROM crypto_prices;
```

### Lowest Cryptocurrency Price

```sql
SELECT MIN(price)
FROM crypto_prices;
```

### Average Cryptocurrency Price

```sql
SELECT AVG(price)
FROM crypto_prices;
```

### Preview Data

```sql
SELECT *
FROM crypto_prices
LIMIT 10;
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/PatienceRamaboe/end-to-end-crypto-data-engineering-pipeline.git
```

Navigate to the project directory.

```bash
cd end-to-end-crypto-data-engineering-pipeline
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

Install the required packages.

```bash
pip install -r Requirements.txt
```

---

## Running the Pipeline

Execute the ETL pipeline in the following order.

```bash
python Scripts/01_extract.py
python Scripts/02_transform.py
python Scripts/03_load.py
```

---

## Project Outcomes

This project demonstrates the ability to:

- Build an end-to-end ETL pipeline
- Extract data from external sources
- Transform and clean datasets using Pandas
- Design and populate PostgreSQL tables
- Perform SQL-based validation and analysis
- Organize a Python project using modular scripts
- Use Git and GitHub for version control

---

## Future Improvements

Planned enhancements include:

- Apache Airflow orchestration
- Docker containerization
- AWS S3 integration
- Automated pipeline scheduling
- Streamlit dashboard
- Power BI dashboard
- Unit testing
- CI/CD with GitHub Actions

---

## Author

**Patience Ramaboe**

Aspiring Data Engineer

**GitHub**  
https://github.com/PatienceRamaboe

**LinkedIn**  
_Add your LinkedIn profile URL_

---

## License

This project is available under the MIT License.
