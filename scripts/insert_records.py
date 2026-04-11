# This module connects to a PostgreSQL database, creates a table if it doesn't exist and inserts weather data fetched from an API. 
# It uses the psycopg2 library for database operations and a custom fetch_data function to retrieve data from the API. 
# The script is designed to be run as a standalone program.

# Import needed libraries
import psycopg2
from api_request import  fetch_data

# Function to connect to the PostgreSQL database
def connect_to_db():
    print("Connecting to the PostgreSQL database...")
    try:
        # Establish a connection to the database using the provided credentials
        conn =psycopg2.connect(
            host="db",
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise

# Function to create the table if it doesn't exist
def create_table(conn):
    print("Creating table if it doesn't exist...")
    try:
        # Use a cursor to execute the SQL command to create the schema and table if they don't exist
        with conn.cursor() as cur:
            cur.execute("""
                CREATE SCHEMA IF NOT EXISTS dev;        
                    
                CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature FLOAT,
                    weather_description TEXT,
                    wind_speed FLOAT,
                    time TIMESTAMP,
                    inserted_at TIMESTAMP DEFAULT NOW(),
                    utc_offset TEXT
                );
            """)
            # Commit the transaction to save changes to the database
            conn.commit()
            # Print a success message if the table is created successfully
            print("Table created successfully")
    except Exception as e:
        print(f"Error creating table: {e}")
        raise

# Function to insert a record into the database
def insert_record(conn, data):
    print("Inserting weather data into the database...")
    try:
        # Extract relevant data from the API response to be inserted into the database
        weather = data["current"]
        location = data["location"]
        # Use a cursor to execute the SQL command to insert the weather data into the table
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO dev.raw_weather_data (city, temperature, weather_description, wind_speed, time, inserted_at, utc_offset)
                VALUES (%s, %s, %s, %s, %s, NOW(), %s);
            """, (
                location['name'],
                weather['temperature'],
                weather['weather_descriptions'][0],
                weather['wind_speed'],
                location['localtime'],
                location['utc_offset']
            ))
            # Commit the transaction to save changes to the database
            conn.commit()
            print("Data inserted successfully!")
    except psycopg2.Error as e:
        print(f"Error inserting data into the database: {e}")
        raise

# Main function to orchestrate the database connection, table creation, data fetching and record insertion
def main():
    # Define the API key and URL for fetching weather data for New York
    api_key = "92dda4cf802ed148c3b1b0165365c632"
    api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"
    try:
        conn = connect_to_db()      # Connect to the database
        create_table(conn)          # Create the table if it doesn't exist   
        data = fetch_data(api_url)  # Fetch weather data from the API
        insert_record(conn, data)   # Insert the fetched data into the database
    except Exception as e:
        print(f"An error occurred during execution: {e}")
    finally:
        # Ensure that the database connection is closed after all operations are completed, even if an error occurs
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")