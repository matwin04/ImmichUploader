import requests
import os
import configparser
from datetime import datetime


class Immich:
    def __init__(self, config_file="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.server_url = self.config.get("Immich", "server_url", fallback="http://localhost:2283/api/assets").strip()
        self.api_key = self.config.get("Immich", "api_key", fallback="").strip()

        if not self.api_key:
            print("❌ ERROR: API Key is missing! Check config.ini")
            raise ValueError("Missing API Key")

    def upload_file(self, file_path):
        if not os.path.exists(file_path):
            print(f"❌ Error: File not found - {file_path}")
            return False

        headers = {
            "x-api-key": self.api_key,
            "Accept": "application/json"
        }

        # Generate metadata
        device_asset_id = os.path.basename(file_path)  # Using filename as a unique ID
        device_id = "PythonUploader"  # Change if needed
        file_created_at = datetime.fromtimestamp(os.path.getctime(file_path)).isoformat()
        file_modified_at = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()

        files = {
            "assetData": (os.path.basename(file_path), open(file_path, "rb"), "application/octet-stream")
        }

        payload = {
            "deviceAssetId": device_asset_id,
            "deviceId": device_id,
            "fileCreatedAt": file_created_at,
            "fileModifiedAt": file_modified_at
        }

        print(f"📤 Uploading {file_path} to {self.server_url}...")

        response = requests.post(self.server_url, headers=headers, files=files, data=payload)

        if response.status_code == 201:
            print(f"✅ Upload successful: {file_path}")
            return True
        else:
            print(f"❌ Upload failed: {file_path} - {response.text}")
            return False
