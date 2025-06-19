# googledrive-backup
## How to use?
1. Setup Upload to Telegram.
2. Goto Actions and Select the workflow [Download Google Drive Folder].
3. Click Run Workflow.
4. Paste Google Drive Public Access Link and Enter the filename to be used for zip file.
5. Click Run Workflow and wait for it to complete.

## Setup Upload to Telegram
1. Create a Telegram APP at [https://my.telegram.org/apps](https://my.telegram.org/apps).
2. Get api_id and api_hash.
3. Run `python get-session.py` on local system. [Important: Run this locally. Before that do `pip install telethon`]
4. Now that we got api_id, api_hash and session_string, save in Github Repo secrets with Name: **TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_SESSION**. https://github.com/<your-user-name>/<your-repo-name>/settings/secrets/actions/new 
```
Example:
Name: TELEGRAM_API_ID
Value: 62976733787
```
5. Thats it!

## Note
1. TELEGRAM_API_ID is always a number.
2. If TELEGRAM_API_ID and TELEGRAM_API_HASH are somehow leaked, just delete the app.
3. If TELEGRAM_SESSION string is leaked, just close the session in Telegram App.
4. If Telegram account password or 2-FA is changed, then all sessions are terminated. You need to update TELEGRAM_SESSION value in secrets. Generate new session string using `python get-session.py` locally.
5. While entering phone number for login, enter full with international code. Eg: +1XXXXXXXX.
6. 2GB File takes nearly 30mins to complete. [Maybe Replace with a better solution or Keep artifact retention with small duration so that after download, the workflow run can be deleted.]
