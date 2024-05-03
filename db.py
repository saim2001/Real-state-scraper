import os
import psycopg2 
from psycopg2 import sql
from psycopg2.errors import UniqueViolation,InFailedSqlTransaction
import pandas as pd
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

conn = psycopg2.connect('postgresql://saim:DSkl7vw-AjHK2LJIguIlSw@redear-giraffe-8487.8nk.gcp-asia-southeast1.cockroachlabs.cloud:26257/postgres?sslmode=verify-full')


def convert_to_date(date_str):
    try:
        return pd.to_datetime(date_str)
    except ValueError:
        return date_str  
def convert_to_star(data):
    try:
        return str(data)
    except ValueError:
        return data  
def replace_not_found_addrs(data):
    if data.replace('/n','') == 'Address not available':
        return None
    else :
        return data

def process_data(sheet):

    # Read all sheets into a dictionary of DataFrames
    xls = pd.ExcelFile(sheet)
    sheets_dict = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}

    # Concatenate all DataFrames into one
    combined_df = pd.concat(sheets_dict.values(), ignore_index=True)
    combined_df['date'] = combined_df['date'].apply(convert_to_date)
    combined_df['longitude'] = combined_df['longitude'].apply(convert_to_star)
    combined_df['latitude'] = combined_df['latitude'].apply(convert_to_star)
    combined_df['address'] = combined_df['address'].apply(replace_not_found_addrs)
    insert_properties(combined_df)

def insert_single_prop(tup):
    with conn.cursor() as cur:
                
        query = sql.SQL("""
                    INSERT INTO properties (
                        date_scraped,
                        address,
                        city,
                        state,
                        postal_code,
                        agent,
                        broker,
                        price_CAD,
                        longitude,
                        latitude
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )
                    """)
        try:
            cur.execute(query,tup)
        except  (InFailedSqlTransaction,UniqueViolation):
            print(f'duplicate found {tup}')
            return 1
        conn.commit()
        return 0
        
    

def insert_properties(df):
    with conn.cursor() as cur:
        data = [tuple(row) for row in df.values]
                
        query = sql.SQL("""
                    INSERT INTO properties (
                        date_scraped,
                        address,
                        city,
                        state,
                        postal_code,
                        agent,
                        broker,
                        price_CAD,
                        longitude,
                        latitude
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )
                    """)
        for i in data:
            try:
                cur.execute(query,i)
                conn.commit()
            except:
                pass
        
        cur.close()
        conn.close()

# process_data(r'data_3.xlsx')