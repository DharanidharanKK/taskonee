# Document360 API - Folder Management Application

A Python console application for interacting with the Document360 API. This application provides functions for performing REST operations (GET, POST, PATCH, DELETE) on Document360 folders with logging and error handling.

## Overview

The application is designed to:
- Interact with the Document360 API for folder management
- Provide simple functions for folder CRUD operations
- Handle API requests and responses efficiently
- Manage authentication using API tokens
- Log all operations for debugging

### Key Features

✅ **GET Operation** - Fetch all folders from Document360 API  
✅ **POST Operation** - Create new folders with custom names  
✅ **PATCH Operation** - Rename existing folders  
✅ **DELETE Operation** - Remove folders  
✅ **Logging** - Logs to both console and `api_requests.log` file  
✅ **Error Handling** - Clear status codes and response messages  
✅ **Interactive Menu** - User-friendly command-line interface  

---

## Setup & Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Navigate to the project directory:**
   ```bash
   cd c:\Users\Dharanidharan\Desktop\Migration_task
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   pip list | findstr requests
   ```

---

## How to Run

Execute the main script:
```bash
python task_app.py
```

### Interactive Workflow

The application guides you through:

1. **Enter API Token** - Prompts for your Document360 API token at startup
2. **GET Folders** - Automatically fetches and displays all existing folders
3. **Create Folder** - Prompts you to enter a folder name to create
4. **Rename Folder** - Prompts you to enter a new name for the created folder (if creation was successful)
5. **Delete Folder** - Asks for confirmation before deleting the folder

### Example Session

```
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
```

---

## Task Implementation

### Task-1: GET - Fetch All Folders

**Function:** `get_folders()`

Retrieves all folders from Document360 API.

```python
def get_folders():
    print("\n--- GET: Fetch All Folders ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    r = requests.get(BASE_URL, headers=headers)
    print("Status Code:", r.status_code)
    print(r.text)
    return r.json()
```

---

### Task-2: POST - Create Folder

**Function:** `create_folder(name)`

Creates a new folder with the specified name.

```python
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
```

---

### Task-3: PATCH - Rename Folder

**Function:** `rename_folder(folder_id, new_name)`

Renames an existing folder to the new name.

```python
def rename_folder(folder_id, new_name):
    print("\n--- PATCH: Rename Folder ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    body = {"title": new_name, "userId": USER_ID}
    r = requests.patch(f"{BASE_URL}/{folder_id}", headers=headers, json=body)
    print("Status Code:", r.status_code)
    print(r.text)
```

---

### Task-4: DELETE - Remove Folder

**Function:** `delete_folder(folder_id)`

Deletes the specified folder.

```python
def delete_folder(folder_id):
    print("\n--- DELETE: Remove Folder ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    r = requests.delete(f"{BASE_URL}/{folder_id}", headers=headers)
    print("Status Code:", r.status_code)
    print(r.text)
```

---

## Project Files

| File | Purpose |
|------|---------|
| `task_app.py` | Main application with GET, POST, PATCH, DELETE functions |
| `config.py` | API configuration (base URL, headers) |
| `requirements.txt` | Python dependencies |
| `README.md` | This documentation |
| `api_requests.log` | Auto-generated request/response log |

---

## Configuration

### API Token

The application prompts you to enter your Document360 API token at runtime:
```
Enter API Token: <paste_your_token_here>
```

The token is used in headers for all API requests:
```python
headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
```

### Base URL

Configured for Document360 API v2:
```
https://apihub.document360.io/v2/Drive/Folders
```

---

## Error Handling

The application handles various response scenarios:

| Status Code | Meaning |
|-------------|---------|
| 200 | Success - Operation completed |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid parameters |
| 403 | Forbidden - Permission denied |
| 404 | Not Found - Resource doesn't exist |
| 500 | Server Error - API server error |

All responses are printed to console with full details for troubleshooting.

---

## Logging

### Console Output
All operations display:
- Operation name (GET, POST, PATCH, DELETE)
- HTTP status code
- Full response text

### Log File
All requests and responses are also logged to `api_requests.log` with timestamps:
```
2026-01-13 10:30:45,123 - INFO - REQUEST: GET ...
2026-01-13 10:30:45,456 - INFO - RESPONSE: 200
```

---

## Troubleshooting

### Issue: "Module not found: requests"
**Solution:** Run `pip install -r requirements.txt`

### Issue: Invalid API Token
**Solution:** Verify your Document360 API token and paste it correctly when prompted

### Issue: Connection Error
**Solution:** Check internet connection and verify API endpoint is accessible

### Issue: 403 Forbidden on PATCH/DELETE
**Solution:** Check your Document360 account role and permissions

---

## Version

**Version:** 1.0.0  
**Last Updated:** January 13, 2026  
**Task Type:** REST API CRUD Operations on Document360 Folders

### 1. GET Folders (Retrieve all folders)

**Function:** `get_folders(api_token)`

**Steps:**
1. Run the application: `python task_app.py`
2. Select option [0] or enter your API token when prompted
3. The application sends a GET request to `https://apihub.document360.io/v2/Drive/Folders`
4. Response displays all available folders with their details

**Example:**
```python
api_token = "your_api_token_here"
folders = get_folders(api_token)
if folders and not folders.get("error"):
    print("Folders retrieved successfully!")
    print(folders)
```

---

### 2. CREATE Folder (Create a new folder)

**Function:** `create_folder(api_token, folder_name)`

**Steps:**
1. Run the application and provide your API token
2. At option [0.5], enter the folder name you want to create
3. The application sends a POST request with JSON body: `{ "name": "folder_name" }`
4. On success, the newly created folder_id is returned

**Example:**
```python
api_token = "your_api_token_here"
folder_name = "My New Folder"
folder_id = create_folder(api_token, folder_name)
if folder_id:
    print(f"Folder created with ID: {folder_id}")
```

---

### 3. UPDATE Folder (Rename a folder)

**Function:** `update_folder(api_token, folder_id, new_name)`

**Steps:**
1. Run the application and provide your API token
2. At option [0.75], enter the folder ID to rename
3. Enter the new folder name
4. The application sends a PUT request to update the folder
5. Success/failure message is displayed

**Example:**
```python
api_token = "your_api_token_here"
folder_id = "12345"
new_name = "Renamed Folder"
success = update_folder(api_token, folder_id, new_name)
if success:
    print(f"Folder renamed successfully!")
```

---

### 4. DELETE Folder (Remove a folder)

**Function:** `delete_folder(api_token, folder_id)`

**Steps:**
1. Run the application and provide your API token
2. At option [1.0], enter the folder ID to delete
3. Confirm deletion when prompted (safety feature)
4. The application sends a DELETE request
5. Confirmation message is displayed

**Example:**
```python
api_token = "your_api_token_here"
folder_id = "12345"
success = delete_folder(api_token, folder_id)
if success:
    print(f"Folder deleted successfully!")
```

---

## Sample Output Explanation

### Console Output Example

```
============================================================
REST API Console Application
============================================================

[0] GET Folders - Fetching folders from Document360 API
Enter your API token (or press Enter to skip): your_api_token_here

============================================================
REQUEST: GET https://apihub.document360.io/v2/Drive/Folders
Headers: {'api_token': 'your_api_token_here', 'Content-Type': 'application/json'}
============================================================
RESPONSE: 200
Response Headers: {...}
Response Body: {
  "folders": [
    {"folder_id": "1", "name": "My Documents"},
    {"folder_id": "2", "name": "Archives"}
  ]
}
============================================================

Folders fetched successfully!
```

### Log File Output

All requests and responses are logged to `api_requests.log`:

```
2026-01-13 10:30:45,123 - INFO - APIClient initialized with base URL: https://jsonplaceholder.typicode.com
2026-01-13 10:30:45,456 - INFO - REQUEST: GET https://apihub.document360.io/v2/Drive/Folders
2026-01-13 10:30:45,457 - INFO - Headers: {'api_token': 'token', 'Content-Type': 'application/json'}
2026-01-13 10:30:45,789 - INFO - RESPONSE: 200
2026-01-13 10:30:45,790 - INFO - Response Body: {"folders": [...]}
2026-01-13 10:30:45,791 - INFO - GET Folders request successful
```

---

## Error Handling

The application implements comprehensive error handling for various failure scenarios:

### HTTP Status Code Errors

| Status Code | Error Type | Action Taken |
|------------|-----------|--------------|
| 400 | Bad Request | Invalid parameters logged; request rejected |
| 401 | Unauthorized | Invalid/missing API token detected; request fails |
| 403 | Forbidden | Permission denied; user lacks required access |
| 404 | Not Found | Resource (e.g., folder) doesn't exist; returns None |
| 409 | Conflict | Resource conflict (e.g., folder not empty); operation fails |
| 429 | Rate Limited | Too many requests; user should wait before retrying |
| 500-503 | Server Errors | API service error; request fails with appropriate message |

### Network Exceptions

```
Timeout Error
- Occurs when API takes more than 10 seconds to respond
- Message: "Request timeout - API server took too long to respond"
- User should check network or try again later

Connection Error
- Occurs when unable to reach the API server
- Message: "Connection error - Unable to reach the API server"
- Typically due to network issues or incorrect base URL

Request Exception
- General request failures (SSL errors, etc.)
- Logged with specific error details
```

### Validation Errors

```
Empty API Token
- Error: "Invalid api_token: API token cannot be empty"
- Action: Function returns None or False without making request

Empty Folder ID
- Error: "Invalid folder_id: folder_id cannot be empty"
- Action: Function returns None or False without making request

Empty Folder Name
- Error: "Invalid new_name: New folder name cannot be empty"
- Action: Function returns False without making request

Missing Response Fields
- Error: "Response missing expected fields: [field_names]"
- Action: Logged; application attempts to continue gracefully
```

### JSON Parsing Errors

```
Invalid JSON Response
- Error: "Failed to parse response as JSON"
- Action: Response logged as raw text; application continues if status code is success
```

### Error Logging Example

```
2026-01-13 10:35:22,100 - ERROR - Authentication failed: Invalid API token
2026-01-13 10:35:22,101 - ERROR - Non-success response received: 401
2026-01-13 10:35:22,102 - ERROR - Error details: {"message": "Invalid token"}
```

---

## File Structure

```
Migration_task/
├── task_app.py           # Main application file with all functions
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── README.md            # This documentation file
└── api_requests.log     # Auto-generated request/response log (created on first run)
```

---

## Code Structure

### Main Components

1. **Utility Functions**
   - `validate_response_json()` - Safely parses JSON responses
   - `validate_response_fields()` - Validates response structure
   - `handle_http_error()` - Generates meaningful error messages

2. **Document360 Specific Functions**
   - `get_folders()` - Fetch all folders
   - `create_folder()` - Create new folder
   - `update_folder()` - Rename folder
   - `delete_folder()` - Delete folder

3. **Generic API Client Class**
   - `APIClient` - Reusable client for any REST API
   - Methods: `get()`, `post()`, `put()`, `delete()`

4. **Main Entry Point**
   - `main()` - Interactive menu and demonstrations

---

## Troubleshooting

### Issue: "Module not found: requests"
**Solution:** Install dependencies with `pip install -r requirements.txt`

### Issue: "Authentication failed: Invalid API token"
**Solution:** Verify your API token is correct and hasn't expired

### Issue: "Connection error - Unable to reach the API server"
**Solution:** Check internet connection and ensure the API server is accessible

### Issue: "Request timeout"
**Solution:** The API is slow to respond; increase timeout value or try again later

### Issue: "Folder not found: Invalid folder_id"
**Solution:** Verify the folder ID exists; run GET Folders to see valid IDs

### Issue: Logs not being created
**Solution:** Ensure write permissions in the application directory; check `api_requests.log`

---

## Best Practices

1. **Store API tokens securely** - Never hardcode tokens; use environment variables
2. **Check logs regularly** - Review `api_requests.log` for troubleshooting
3. **Validate inputs** - Always verify user inputs before passing to functions
4. **Handle responses gracefully** - Always check return values (None, False, dict with error flag)
5. **Retry on timeout** - Network timeouts are temporary; implement retry logic if needed
6. **Use confirmation prompts** - Dangerous operations (delete) should require confirmation

---

## Example Workflow

```
1. Start Application
   → python task_app.py

2. Provide API Token
   → Paste your Document360 API token

3. Get Folders
   → Retrieve list of all folders

4. Create Folder
   → Enter "Projects" as folder name
   → Receive folder_id (e.g., "123")

5. Update Folder
   → Enter folder_id "123"
   → Enter new name "Active Projects"
   → Confirmation message displayed

6. Generic API Test
   → Use JSONPlaceholder test API
   → Demonstrates GET, POST, PUT, DELETE

7. Review Logs
   → Check api_requests.log for all operations
```

---

## Support & Debugging

- **Enable detailed logging** - All operations logged to console and `api_requests.log`
- **Check response structure** - Use logging output to understand API response format
- **Validate inputs** - Ensure API token and IDs are correct before operations
- **Review HTTP status codes** - Consult the error handling section for status code meanings

---

## License

This project is provided as-is for educational and integration purposes.

---

## Version

**Version:** 1.0.0  
**Last Updated:** January 13, 2026  
**Python:** 3.7+  
**Dependencies:** requests 2.31.0+
