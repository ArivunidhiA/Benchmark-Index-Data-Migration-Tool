import pandas as pd
import sqlite3
from pathlib import Path
import logging

class ETLProcessor:
    def __init__(self, config):
        self.config = config
        self.raw_data_path = Path(config['paths']['raw_data'])
        self.processed_data_path = Path(config['paths']['processed_data'])
        self.db_path = Path(config['paths']['database'])

    def extract(self):
        """Extract data from CSV files."""
        try:
            dfs = []
            for file in self.raw_data_path.glob('*.csv'):
                df = pd.read_csv(file)
                df['source_file'] = file.name
                dfs.append(df)
            
            return pd.concat(dfs, ignore_index=True)
        except Exception as e:
            logging.error(f"Error in data extraction: {str(e)}")
            raise

    def transform(self, data):
        """Transform the extracted data."""
        try:
            # Standardize column names
            data.columns = data.columns.str.lower().str.replace(' ', '_')
            
            # Convert date columns
            if 'date' in data.columns:
                data['date'] = pd.to_datetime(data['date'])
            
            # Handle missing values
            data = data.fillna({
                'value': data['value'].mean() if 'value' in data.columns else 0,
                'index_name': 'Unknown'
            })
            
            return data
        except Exception as e:
            logging.error(f"Error in data transformation: {str(e)}")
            raise

    def load(self, data):
        """Load data into SQLite database."""
        try:
            conn = sqlite3.connect(self.db_path)
            data.to_sql('benchmark_indices', conn, if_exists='replace', index=False)
            conn.close()
            
            # Also save as CSV for backup
            data.to_csv(self.processed_data_path / 'processed_data.csv', index=False)
            
            return data
        except Exception as e:
            logging.error(f"Error in data loading: {str(e)}")
            raise

    def run(self):
        """Execute the complete ETL pipeline."""
        logging.info("Starting ETL process")
        raw_data = self.extract()
        transformed_data = self.transform(raw_data)
        processed_data = self.load(transformed_data)
        logging.info("ETL process completed successfully")
        return processed_data
