import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2

# Your RDS connection details
DB_HOST = ""
DB_PORT = ""
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""

try:
    connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(connection_string)
    
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("Connection successful!")
        print(f"PostgreSQL version: {result.fetchone()[0]}")
        
except Exception as e:
    print(f"Connection failed: {e}")