Document360 API - Folder Management Application
A Python console application for interacting with the Document360 API. This application provides functions for performing REST operations (GET, POST, PATCH, DELETE) on Document360 folders with logging and error handling.

Overview
The application is designed to:

Interact with the Document360 API for folder management
Provide simple functions for folder CRUD operations
Handle API requests and responses efficiently
Manage authentication using API tokens
Log all operations for debugging
Key Features
✅ GET Operation - Fetch all folders from Document360 API
✅ POST Operation - Create new folders with custom names
✅ PATCH Operation - Rename existing folders
✅ DELETE Operation - Remove folders
✅ Logging - Logs to both console and api_requests.log file
✅ Error Handling - Clear status codes and response messages
✅ Interactive Menu - User-friendly command-line interface

Setup & Installation
Prerequisites
Python 3.7 or higher
pip (Python package manager)
Installation Steps
Navigate to the project directory:

cd c:\Users\Dharanidharan\Desktop\Migration_task
Install required dependencies:

pip install -r requirements.txt
Verify installation:

pip list | findstr requests
How to Run
Execute the main script:

python task_app.py
Interactive Workflow
The application guides you through:

Enter API Token - Prompts for your Document360 API token at startup
GET Folders - Automatically fetches and displays all existing folders
Create Folder - Prompts you to enter a folder name to create
Rename Folder - Prompts you to enter a new name for the created folder (if creation was successful)
Delete Folder - Asks for confirmation before deleting the folder
Example Session
Enter API Token: <your_token_here>

--- GET: Fetch All Folders ---
Status Code: 200
{response data...}

Enter folder name to create: My Test Folder

--- POST: Create Folder ---
Status Code: 200
{response data...}
Folder Created ID: <folder_id>

Enter new name for folder: My Updated Folder

--- PATCH: Rename Folder ---
Status Code: 200
{response data...}

Delete this folder? (yes/no): yes

--- DELETE: Remove Folder ---
Status Code: 200
{response data...}
Task Implementation
Task-1: GET - Fetch All Folders
Function: get_folders()

Retrieves all folders from Document360 API.

def get_folders():
    print("\n--- GET: Fetch All Folders ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    r = requests.get(BASE_URL, headers=headers)
    print("Status Code:", r.status_code)
    print(r.text)
    return r.json()
Task-2: POST - Create Folder
Function: create_folder(name)

Creates a new folder with the specified name.

def create_folder(name):
    print("\n--- POST: Create Folder ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    body = {"title": name, "userId": USER_ID}
    r = requests.post(BASE_URL, headers=headers, json=body)
    print("Status Code:", r.status_code)
    print(r.text)
    if r.status_code == 200:
        return r.json()["data"]["media_folder_id"]
    return None
Task-3: PATCH - Rename Folder
Function: rename_folder(folder_id, new_name)

Renames an existing folder to the new name.

def rename_folder(folder_id, new_name):
    print("\n--- PATCH: Rename Folder ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    body = {"title": new_name, "userId": USER_ID}
    r = requests.patch(f"{BASE_URL}/{folder_id}", headers=headers, json=body)
    print("Status Code:", r.status_code)
    print(r.text)
Task-4: DELETE - Remove Folder
Function: delete_folder(folder_id)

Deletes the specified folder.

def delete_folder(folder_id):
    print("\n--- DELETE: Remove Folder ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    r = requests.delete(f"{BASE_URL}/{folder_id}", headers=headers)
    print("Status Code:", r.status_code)
    print(r.text)
Project Files
File	Purpose
task_app.py	Main application with GET, POST, PATCH, DELETE functions
config.py	API configuration (base URL, headers)
requirements.txt	Python dependencies
README.md	This documentation
api_requests.log	Auto-generated request/response log
Configuration
API Token
The application prompts you to enter your Document360 API token at runtime:

Enter API Token: <paste_your_token_here>
The token is used in headers for all API requests:

headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
Base URL
Configured for Document360 API v2:

https://apihub.document360.io/v2/Drive/Folders
Error Handling
The application handles various response scenarios:

Status Code	Meaning
200	Success - Operation completed
201	Created - Resource created successfully
400	Bad Request - Invalid parameters
403	Forbidden - Permission denied
404	Not Found - Resource doesn't exist
500	Server Error - API server error
All responses are printed to console with full details for troubleshooting.

Logging
Console Output
All operations display:

Operation name (GET, POST, PATCH, DELETE)
HTTP status code
Full response text
Log File
All requests and responses are also logged to api_requests.log with timestamps:

2026-01-13 10:30:45,123 - INFO - REQUEST: GET ...
2026-01-13 10:30:45,456 - INFO - RESPONSE: 200
Troubleshooting
Issue: "Module not found: requests"
Solution: Run pip install -r requirements.txt

Issue: Invalid API Token
Solution: Verify your Document360 API token and paste it correctly when prompted

Issue: Connection Error
Solution: Check internet connection and verify API endpoint is accessible

Issue: 403 Forbidden on PATCH/DELETE
Solution: Check your Document360 account role and permissions

Version
Version: 1.0.0
Last Updated: January 13, 2026
Task Type: REST API CRUD Operations on Document360 Folders
