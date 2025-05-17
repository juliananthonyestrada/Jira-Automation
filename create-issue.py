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

# HTTP headers for request/response formatting
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Creates a Jira issue with the given project key, summary, description, and issue type
def create_issue(project_key, summary, description_text, issue_type):
    # Converts Python dictionary to a JSON-formatted string, which is required by the API
    payload = json.dumps({
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": description_text,
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": issue_type
            }
        }
    })

    # Sends an HTTP POST request to Jira to create the issue, with headers, payload, and authentication
    response = requests.post(
        url,
        headers=headers,
        data=payload,
        auth=(email, api_token)
    )

    if response.status_code == 201:
        print(f"Issue created successfully! Key: {response.json()['key']}")
        print(f"Status code: {response.status_code}") 
        print(f"Response text: {response.text}") 
    else:
        print(f"Failed to create issue. Status code: {response.status_code}")
        print(f"Response text: {response.text}")

# Example usage
if __name__ == "__main__":
    create_issue("LRN", "Run", "We need to run a 5k today", "Task")
