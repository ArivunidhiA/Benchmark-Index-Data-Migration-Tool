# Benchmark Index Data Migration Tool

## Overview
This project implements a simplified financial benchmark index data migration and reconciliation system. It demonstrates ETL processes, data validation, and monitoring capabilities using Python and SQL, making it suitable for learning and portfolio presentation.

## Features
- Data migration between CSV files and SQLite database
- Automated ETL pipeline
- Data validation and reconciliation
- Real-time monitoring and alerts
- Basic dashboard for data visualization
- Error logging and reporting

## Project Structure
```
benchmark-migration-tool/
├── data/
│   ├── raw/                  # Raw benchmark data files
│   ├── processed/            # Cleaned and transformed data
│   └── validated/            # Final validated data
├── src/
│   ├── etl/                  # ETL processing scripts
│   ├── validation/           # Data validation scripts
│   ├── monitoring/           # Monitoring and alert scripts
│   └── visualization/        # Dashboard and reporting scripts
├── tests/                    # Unit tests
├── logs/                     # Application logs
├── config/                   # Configuration files
└── notebooks/               # Jupyter notebooks for analysis
```

## Prerequisites
- Python 3.8+
- SQLite3
- Required Python packages:
  - pandas
  - numpy
  - sqlite3
  - plotly
  - dash
  - pytest

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/benchmark-migration-tool.git
cd benchmark-migration-tool
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Place your source data files in the `data/raw` directory
2. Run the ETL pipeline:
```bash
python src/main.py
```

3. Access the dashboard:
```bash
python src/visualization/dashboard.py
```
The dashboard will be available at `http://localhost:8050`

## Testing
Run the test suite:
```bash
pytest tests/
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Sample data structure inspired by standard financial benchmark indices
- Dashboard design based on common industry practices
