# This module contains the function to fetch data from the weatherstack API.

# Import needed libraries
import requests

# Function to fetch data from the weatherstack API
def fetch_data(url):
    print("Fetching data from weatherstack API")  # Print the URL being accessed
    try:
        response = requests.get(url)        # Make the GET request to the API
        response.raise_for_status()         # Check if the request was successful
        print("API Request Successful")     # Print a success message
        return response.json()              # Return the JSON data
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
