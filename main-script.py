import logging
from datetime import datetime
from pathlib import Path
from etl.processor import ETLProcessor
from validation.validator import DataValidator
from monitoring.monitor import DataMonitor
from config.settings import load_config

# Configure logging
logging.basicConfig(
    filename=f'logs/migration_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    """Main execution function for the benchmark data migration tool."""
    try:
        # Load configuration
        config = load_config()
        
        # Initialize components
        etl_processor = ETLProcessor(config)
        validator = DataValidator(config)
        monitor = DataMonitor(config)
        
        # Execute ETL pipeline
        logging.info("Starting ETL process...")
        processed_data = etl_processor.run()
        
        # Validate data
        logging.info("Validating migrated data...")
        validation_results = validator.validate(processed_data)
        
        # Monitor results
        logging.info("Monitoring data quality...")
        monitor.check_data_quality(validation_results)
        
        logging.info("Migration process completed successfully")
        
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()
