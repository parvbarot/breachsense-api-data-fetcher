import requests
import json

websites = input("Please enter a list of website names separated by commas: ").split(",")
date = input("Enter date (YYYYMMDD): ")
license_key = input("Enter license key: ")

endpoints = [
    "combo",
    "creds",
    "darkweb",
    "radar",
    "sessions",
    "stealer",
]

for website in websites:
    for endpoint in endpoints:
        url = f"https://api.breachsense.io/{endpoint}?lic={license_key}&date={date}&search={website}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            with open(f"{endpoint}_{website}_{date}.json", "w") as f:
                json.dump(data, f)
            print(f"Data for {website} on {date} successfully saved to {endpoint}_{website}_{date}.json")
        else:
            print(f"Failed to retrieve data from {endpoint} endpoint for {website} on {date}")
