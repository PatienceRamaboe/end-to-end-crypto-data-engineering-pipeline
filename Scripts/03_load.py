import logging
import pandas as pd
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("Reading cleaned CSV file...")

    df = pd.read_csv("Data/Clean_Data.csv")

    logging.info("Connecting to PostgreSQL...")

    engine = create_engine(
        "postgresql://postgres:nosipho%4002@localhost:5432/data_pipeline_db"
    )

    logging.info("Loading data into PostgreSQL...")

    df.to_sql(
        "crypto_prices",
        engine,
        if_exists="replace",
        index=False
    )

    logging.info("Data loaded successfully!")

except Exception as e:
    logging.error(f"An error occurred: {e}")