import requests

url = "https://api.telegram.org/bot738095135:AAGoDa90OCX5JckiOYDTknU1cD7MJWtR08M/getUpdates"
r = requests.get(url)

if r.status_code == 200:
    response = r.json()

    last_update = response["result"][-1]
    last_chat = last_update["message"]["chat"]
    print("Chat id:", last_chat["id"])