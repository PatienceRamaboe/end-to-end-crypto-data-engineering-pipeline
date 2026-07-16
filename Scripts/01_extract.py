import os
import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

FILE_PATH = "Data/Raw_Data.csv"

try:
    logging.info("Checking if dataset exists...")

    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f"{FILE_PATH} was not found.")

    logging.info("Dataset found. Reading CSV file...")

    df = pd.read_csv(FILE_PATH)

    logging.info(f"Dataset loaded successfully.")
    logging.info(f"Number of rows: {df.shape[0]}")
    logging.info(f"Number of columns: {df.shape[1]}")

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nDataset Information")
    df.info()

except Exception as e:
    logging.error(f"Error during extraction: {e}")