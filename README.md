# 📁 Document360 API - Folder Management Application 

A Python console application for interacting with the Document360 API.  
It performs REST operations (**GET, POST, PATCH, DELETE**) on Document360 folders with full logging and error handling.
find the ReadMe Inside the file to get more informations

---

## 🧭 Overview

The application is designed to:

- Interact with the Document360 API for folder management  
- Provide simple functions for folder CRUD operations  
- Handle API requests and responses efficiently  
- Manage authentication using API tokens  
- Log all operations for debugging  

---

## ✨ Key Features

- ✅ GET Operation – Fetch all folders from Document360 API  
- ✅ POST Operation – Create new folders with custom names  
- ✅ PATCH Operation – Rename existing folders  
- ✅ DELETE Operation – Remove folders  
- ✅ Logging – Logs to both console and `api_requests.log`  
- ✅ Error Handling – Clear status codes and response messages  
- ✅ Interactive Menu – User-friendly CLI  

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.7 or higher  
- pip (Python package manager)

### Installation Steps

```bash
cd c:\Users\Dharanidharan\Desktop\Migration_task
pip install -r requirements.txt
pip list | findstr requests

