import requests
import json

import requests
import json

pricing_api_endpoint = "https://prices.azure.com/api/retail/prices"
pages = {"api-version": "2023-01-01-preview"}

def caller():
    response = requests.get(pricing_api_endpoint, params=pages)
    pricing_data = response.json()
    print(json.dumps(pricing_data, indent=2))

caller()

pages = {"api-version": "2023-01-01-preview", "$skip": "100"}
caller()

pages = {"api-version": "2023-01-01-preview", "$skip": "200"}
caller()
