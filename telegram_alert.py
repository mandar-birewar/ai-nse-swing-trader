import requests

TOKEN = "8649443155:AAEfg6q8W5LIcghrHOgf7WZgIqj1-478-0s"
CHAT_ID = "5782188556"

def send_message(text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    requests.post(url, data=payload)