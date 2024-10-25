import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_config():
    """Load configuration settings for the application."""
    base_dir = Path(__file__).parent.parent

    return {
        'paths': {
            'raw_data': base_dir / 'data' / 'raw',
            'processed_data': base_dir / 'data' / 'processed',
            'validated_data': base_dir / 'data' / 'validated',
            'database': base_dir / 'data' / 'benchmark.db'
        },
        'validation': {
            'required_columns': [
                'date', 'index_name', 'value', 'volume', 
                'currency', 'region'
            ],
            'value_ranges': {
                'value': (0, 1000000),
                'volume': (0, 1000000000)
            }
        },
        'monitoring': {
            'alert_thresholds': {
                'missing_data_pct': 5.0,
                'value_change_pct': 10.0
            }
        },
        'database': {
            'connection_string': os.getenv('DB_CONNECTION_STRING', 'sqlite:///data/benchmark.db')
        }
    }
