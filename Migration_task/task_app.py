import requests
import json
import logging
import sys

API_TOKEN = input("Enter API Token: ").strip()
USER_ID = "9bc90a13-4c7a-45e6-b51d-839bc3a5a209"
BASE_URL = "https://apihub.document360.io/v2/Drive/Folders"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler("api_requests.log")]
)

def get_folders():
    print("\n--- GET: Fetch All Folders ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    r = requests.get(BASE_URL, headers=headers)
    print("Status Code:", r.status_code)
    print(r.text)
    return r.json()

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

def rename_folder(folder_id, new_name):
    print("\n--- PATCH: Rename Folder ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    body = {"title": new_name, "userId": USER_ID}
    r = requests.patch(f"{BASE_URL}/{folder_id}", headers=headers, json=body)
    print("Status Code:", r.status_code)
    print(r.text)

def delete_folder(folder_id):
    print("\n--- DELETE: Remove Folder ---")
    headers = {"api_token": API_TOKEN, "Content-Type": "application/json"}
    r = requests.delete(f"{BASE_URL}/{folder_id}", headers=headers)
    print("Status Code:", r.status_code)
    print(r.text)

if __name__ == "__main__":
    get_folders()

    folder_name = input("\nEnter folder name to create: ").strip()
    folder_id = create_folder(folder_name)

    if folder_id:
        print("Folder Created ID:", folder_id)

        new_name = input("\nEnter new name for folder: ").strip()
        rename_folder(folder_id, new_name)

        confirm = input("\nDelete this folder? (yes/no): ").lower()
        if confirm == "yes":
            delete_folder(folder_id)
