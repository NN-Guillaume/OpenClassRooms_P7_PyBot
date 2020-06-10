import geocoder

from app.config import key_value


class Geo:
    """Class who takes care of the GoogleMap API """

    def __init__(self):
        self.key = key_value

    def get_coordonnees(self, question):
        """Thanks to the user input Google will find the localisation"""

        g = geocoder.google(question, key=self.key)
        if g.ok:
            # g = geocoder.google(question, key=key_value)
            data = g.json
            latitude = data["lat"]
            longitude = data["lng"]
            return latitude, longitude
        else:
            return None  # ici g.ok est à False

    def get_address(self, coordonnees):
        """Find the wanted address thanks to the geographical coordinates"""

        g = geocoder.google(coordonnees, method="reverse", key=key_value)
        data = g.json
        address = data["address"]
        return address
