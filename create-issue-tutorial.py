import requests  # For making HTTP requests
from requests.auth import HTTPBasicAuth  # For basic API authentication
import json  # For handling JSON data
from dotenv import load_dotenv  # Loads environment variables from a .env file
import os  # Provides access to environment variables and operating system features

load_dotenv()  # Load environment variables from the .env file

# Jira Cloud API endpoint for creating issues
url = os.getenv("url")  

# Jira account credentials
api_token = os.getenv("api_token")  
email = os.getenv("email")

# Holds HTTP header fields that the script sends along with the API request
# Header fields are pieces of information sent along with an HTTP request or response. 
# They act like labels or instructions that describe details about the message being sent.

# The headers tell Jira what kind of data we want to receive and what kind of data we are sending
headers = {
  "Accept": "application/json",       # Tell Jira we want the response data formatted as JSON
  "Content-Type": "application/json"  # Tell Jira the data we send in the request is JSON formatted
}

# To create a Jira issue, we need to provide some information about it. A payload is the 
# actual data that we send to the server in the body of the request.
    # ex: project key, summary, description, and issue type

# json.dumps() converts a Python object (e.g., dictionary) into a JSON-formatted string 
# because APIs require data to be sent as JSON text, not as Python objects.
payload = json.dumps(
    {
    "fields": {
       "project":
       {
          "key": "LRN" # Unique identifier for the project where the issue will be created
       },
       "summary": "Run",
       "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": "We need to run a 5k today",
                            "type": "text"
                        }
                    ]
                }
            ]
        },
       "issuetype": {
          "name": "Task"
       }
   }
}
)

# Sends data to a server to create or update a resource via an HTTP POST request; 
# takes parameters like URL, data (payload), headers, and authentication info
response = requests.post(url, headers=headers, data=payload, auth=(email, api_token))

print(f"Status code: {response.status_code}") # Print the status code of the response (e.g., 200 for success)
print(f"Response text: {response.text}") # Print the response text (the content returned by the server)


def create_issue(project_keu, summary, description, issue_type):
    pass