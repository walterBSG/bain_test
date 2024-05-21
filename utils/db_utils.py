import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv(dotenv_path="/app/api_keys.env")

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def read_data_from_db(query):
    conn = get_db_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def write_data_to_db(df, table_name):
    conn = get_db_connection()
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
