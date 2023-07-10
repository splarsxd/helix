import requests
import json

with open("api.json", encoding="utf-8") as status:
    api = json.load(status)

username = input("Quick search: ")
search = requests.get(f"{api['api']}{username}").json()

print(search)