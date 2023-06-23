from config import SITE_API, HOST_API
from api.utils.site_api_handler import SiteApiInterFace

url = "https://hotels4.p.rapidapi.com/locations/search"
querystring = {"query": "new york", "locale": "en_US"}

headers = {
	"X-RapidAPI-Key": SITE_API,
	"X-RapidAPI-Host": HOST_API
}

site_api = SiteApiInterFace()

if __name__ == '__main__':
	site_api()

# response = requests.request("GET", url, headers=headers, params=querystring)
# data = response.json()
#
# # print(response.text)
# pprint(data)
