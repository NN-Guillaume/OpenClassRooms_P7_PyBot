from app.geo import Geo

####################################################
# Version en utilisant vraiment l'API, sans mock : #
####################################################
def test_get_coordonnees_online():
    """Google API test online coordonnées"""

    apigeo = Geo()
    response = apigeo.get_coordonnees("strasbourg")
    assert response == (48.5734053, 7.752111299999999), "Problème"

def test_get_address_online():

    apigeo = Geo()
    response = apigeo.get_address((48.5734053, 7.752111299999999)) # pourquoi une double parenthèse ?
    assert response == "1 Parc de l'Étoile, 67000 Strasbourg, France"

####################################################
# Version sans utiliser l'API, avec monkeypatch  : #
####################################################
def test_get_coordonnees_offline(monkeypatch):  #------------------------------------------------------------------------- F A I L E D       T E S T     ! ! !
    """Google API test online coordonnées"""
    result = {
        'lat': 2,
        'lng': 3
    }

    class MockRequests:
        """Mock class requests"""
        def google(self, url, key):
            """Mock method get function"""
            return MockResponse(200)

    class MockResponse:
        """Mock class response"""
        def __init__(self, code):
            """Google API code initialization"""
            self.json = result
            self.status_code = code

    monkeypatch.setattr('app.geo.geocoder', MockRequests())
    apigeo = Geo()
    result_coordinate = apigeo.get_coordonnees('Cybertron')
    assert result_coordinate == (2, 3), "Unicron"