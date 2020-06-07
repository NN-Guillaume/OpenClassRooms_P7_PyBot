from app.wiki import Wiki

####################################################
# Version en utilisant vraiment l'API, sans mock : #
####################################################
def test_api_wiki_get_page_id_online():
    """Wikipedia API test online id page"""

    apiwiki = Wiki()
    response = apiwiki.get_page_id(48.85837009999999, 2.2944813)

    assert response == 1359783, "Problème sur l'obtention d'une page id online"

def test_api_wikiget_extract_online():
    """Wikipedia_API_test_online_extract"""

    apiwiki = Wiki()
    response1 = apiwiki.get_summary(1359783)

    assert response1[:14] == 'La tour Eiffel'


####################################################
# Version sans utiliser l'API, avec monkeypatch  : #
####################################################

def test_api_wiki_get_page_id_offline(monkeypatch): #------------------------------------------------------------------------- F A I L E D       T E S T     ! ! !
    """Wikipedia API test offline id page"""

    result = {
        'query': {
            'geosearch':
            [
                {
                    'pageid': 5
                }
            ]
        }
    }

    class MockRequests:
        """Mock class requests"""

        def get(self,url, params):
            """Mock method get function"""

            return MockResponse(200)

    class MockResponse:
        """Mock class response"""

        def __init__(self, code):
            """Wiki API code initialization"""

            self.status_code = code

        def json(self):
            """Mock method json function"""

            return result

    monkeypatch.setattr('app.wiki.requests', MockRequests())

    apiwiki = Wiki()
    pageid = apiwiki.get_page_id(48.85837009999999, 2.2944813)

    assert pageid == 5

def test_api_wiki_get_extract_offline(monkeypatch): #------------------------------------------------------------------------- F A I L E D       T E S T     ! ! !
    """Wikipedia API test offline  extract"""

    result = {
        'query':{
            'pages': {
                '5': {
                    'canonicalurl':
                    'https://fr.wikipedia.org/wiki/Tour_Eiffel',
                    'extract':
                    'La tour Mockel'
                }
            }
        }
    }

    class MockRequests():
        """Mock class requests"""

        def get(self, url, params):
            """Mock method get function"""

            return MockResponse(200)

    class MockResponse:
        """Mock class response"""

        def __init__(self, code):
            """Wiki API code initialization"""

            self.status_code = code

        def json(self):
            """Mock method json function"""

            return result

    monkeypatch.setattr('app.wiki.requests', MockRequests())
    apiwiki = Wiki()
    extract_text = apiwiki.get_summary(5)
    assert extract_text == 'La tour Mockel'