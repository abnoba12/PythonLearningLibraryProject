from config import USE_DB

if USE_DB:
    from library.data_operations.db_operations import DbOperations as Operations
else:
    from library.data_operations.csv_operations import CsvOperations as Operations

operations = Operations()
