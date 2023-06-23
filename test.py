import requests
from pprint import pprint

url = "https://hotels4.p.rapidapi.com/locations/search"

querystring = {"query": "hr", "locale": "en_US"}

headers = {
	"X-RapidAPI-Key": "1e9591aedemsh7b926b28fbfcf43p12134fjsn6c0059ef2e75",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()

# print(response.text)
pprint(data)
