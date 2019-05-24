import requests

TOKEN = "bot738095135:AAGoDa90OCX5JckiOYDTknU1cD7MJWtR08M/getMe"

server = "https://api.telegram.org"
endpoint = "getMe"

url = server + "/" + TOKEN + "/" +endpoint

response = requests.get(url)
if response.status_code == 200:
    print(response.json())