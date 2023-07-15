import requests
import json
import os, time

# open api search made by splars#1252

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
sleep = lambda: os.system("timeout 5 >nul" if os.name == "nt" else time.sleep(5))
os.system("title Open API Search" if os.name == "nt" else "pass")
os.system("color c" if os.name == "nt" else "pass")
cls()

with open("api.json", encoding="utf-8") as status:
    api = json.load(status)

def main():
    username = input("Quick search: ")
    try:
        search = requests.get(f"{api['api']}{username}").json()
        print(f"\n{search}")
    except:
        print(f"\nUser was not found.")
    sleep()
    cls()
    main()

main()