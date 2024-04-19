import requests
import json

# Replace these with your FileMaker Server details
filemaker_host = ''
filemaker_file = ''
filemaker_layout = ''
filemaker_user = ''
filemaker_password = ''

# Base URL for the FileMaker Data API
base_url = f'https://{filemaker_host}/fmi/data/v1/databases/{filemaker_file}/layouts/{filemaker_layout}/records'

# Create a session and login to FileMaker
session = requests.Session()
login_url = f'https://{filemaker_host}/fmi/data/v1/databases/{filemaker_file}/sessions'
login_payload = {
    'fmDataSource': {'database': filemaker_file},
    'fmLayout': filemaker_layout,
    'fmScript': 'YourLoginScript',  # Optional: If you have a login script
    'fmUsername': filemaker_user,
    'fmPassword': filemaker_password
}
login_response = session.post(login_url, json=login_payload, verify=False)

# Check if login was successful
# Check if login was successful
# Check if login was successful
if login_response.status_code == 200:
    # Check if the session cookie is present
    if 'session' in session.cookies:
        # Retrieve records
        get_records_response = session.get(base_url, verify=False)

        if get_records_response.status_code == 200:
            records = get_records_response.json()
            print(json.dumps(records, indent=2))
        else:
            print(f"Error retrieving records: {get_records_response.status_code}")
    else:
        print("Session cookie not found. Login might have failed.")
else:
    print(f"Login failed: {login_response.status_code}")

# Logout from FileMaker
logout_url = f'https://{filemaker_host}/fmi/data/v1/databases/{filemaker_file}/sessions/{session.cookies["session"]}'
logout_response = session.delete(logout_url)

# Check if logout was successful
if logout_response.status_code == 200:
    print("Logged out successfully")
else:
    print(f"Logout failed: {logout_response.status_code}")
