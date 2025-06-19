import os
import sys
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Load from environment variables
api_id = int(os.getenv("TELEGRAM_API_ID"))
api_hash = os.getenv("TELEGRAM_API_HASH")
session_string = os.getenv("TELEGRAM_SESSION")
target_chat = "me"  # uploads to Saved Messages

# Take file path from argument
if len(sys.argv) < 2:
    raise ValueError("Please provide a file path to upload")

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
    print(f"✅ Connected as {client.get_me().username}")
    print(f"📤 Uploading: {file_path}")

    message = client.send_file(
        target_chat,
        file_path,
        caption=f"📦 Uploaded: {os.path.basename(file_path)}"
    )
    print("✅ Upload complete!")