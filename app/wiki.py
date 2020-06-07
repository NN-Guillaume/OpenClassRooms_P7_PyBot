from requests import get
import requests

class Wiki:
    def __init__(self):

        self.url = "https://fr.wikipedia.org/w/api.php"

    def get_page_id(self, lat, lng):
        """request to wikipedia to check pages about a place near of google
        coordinates. Select the first result which mean the nearest place"""

        lat_lng = "|".join([str(lat), str(lng)])
        parameters = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 1000,
            "gscoord": lat_lng,
            "format": "json",
        }
        response = requests.get(self.url, params=parameters)
        data = response.json()
        page_id = data["query"]["geosearch"][0]["pageid"]
        return page_id

    def get_summary(self, id):
        """request to wikipedia. Extract a summary from the page"""

        parameters = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1,
            "exsentences": "5",
            "pageids": id,
        }
        response = requests.get(self.url, params=parameters)
        data = response.json()
        summary = data["query"]["pages"][str(id)]["extract"]
        return summary