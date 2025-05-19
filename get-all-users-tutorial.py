import requests  # For making HTTP requests
from requests.auth import HTTPBasicAuth  # For basic API authentication
import json  # For handling JSON data
from dotenv import load_dotenv  # Loads environment variables from a .env file
import os  # Provides access to environment variables and operating system features

load_dotenv()  # Load environment variables from the .env file

# Jira Cloud API endpoint for creating issues
url = os.getenv("url_get_users")  

# Jira account credentials
api_token = os.getenv("api_token")  
email = os.getenv("email")

# Tell Jira we want the response data formatted as JSON
headers = {
  "Accept": "application/json"
}

# Sends an HTTP GET request to Jira to retrieve all users, with headers and authentication
response = requests.get(
    url,
    headers=headers,
    auth=(email, api_token)
)

users = response.json()  # Parse the JSON response into a Python dictionary

for i, user in enumerate(users):
    print(i, user["displayName"])