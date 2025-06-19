from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

api_id = int(0) # Add yours  
api_hash = "" # Add yours

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("✅ Session created! Now logging in...")
    session_str = client.session.save()
    print(f"🔐 SESSION_STRING={session_str}")