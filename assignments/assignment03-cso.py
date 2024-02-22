# assignments03-cso.py
# Assignment 3. Using an api to get data for the exchequer account (historical series) from the cso web site
# author K Donovan


import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
def get_all_as_file():
    with open("cso.json", "wt") as fp:
        print(json.dumps(get_all()), file = fp)
def get_all():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    get_all_as_file()