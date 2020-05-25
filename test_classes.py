import pytest
import geocoder
import random
import requests

import app.views as script
from app.classes import *


from requests import get
from io import BytesIO

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def test_addition():
        assert addition(10,20) == 30

#exemple
class TestCalcul:

    def test_addition(self):
        assert addition(10,20) == 30
        #doesn't works

#QUESTION
"""
def traitement(question):
    coord = geocode(question)
    return "Votre question est: "+ question
"""

#------------------------------------------------------------- G O O G L E   C L A S S ----------------------------------------------------------------------------------
#GEO

FALSE_COORDINATES = {'results': [{'geometry':{'location': {'lat':0, 'lng':0}}}]}
#FALSE_COORDINATES = {'results': [{'geometry':{'location': {'lat':43.8366045, 'lng':5.0407814}}}]}

def fake_request_googlemap(*args, **kwargs):
    return TestGeo()

class TestGeo:

    def json(self):
        return FALSE_COORDINATES

def test_get_false_coordonnees(monkeypatch):
    ZONE = script.Geo('Cavaillon')
    monkeypatch.setattr(requests,'get',fake_request_googlemap)
    #assert ZONE.get_coordonnees() == FALSE_COORDINATES['results'][0]['geometry']['location']
    assert ZONE.get_coordonnees() == (43.8366045, 5.0407814)

"""
    def test_get_address(self, coordonnees):
        g = geocoder.google(coordonnees, method = "reverse", key = 'AIzaSyDf-8PO-M4h0cgIXw1dGZ4NCt1xVUWvFbY')
        data = g.json
        self.address = data["address"]
        return self.address
"""

#-------------------------------------------------------------    W I K I    C L A S S    --------------------------------------------------------------------------------

# WIKI
"""
COORDS = Wiki({self, 'lat': 0, 'lng': 0})
#COORDS = {self, 'lat': 0, 'lng': 0}

FALSE_PAGE = {'query':{'geosearch':[{'page_id':'Cavaillon'}]}}
def f_request_wiki(*args, **kwargs):
    return TestWiki()


class TestWiki:
    def json(self):
        return FALSE_PAGE

def f__get_page_id(monkeypatch):
    monkeypatch.setattr(requests, 'get', f_request_wiki)
    assert COORDS.__get_page_id() == FALSE_PAGE["query"]["geosearch"][0]['pageid']
"""
"""
    def __get_summary(self):
        parameters = {
            "action": "query",
            "format": "json",
            "prop" : "extracts",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1,
            "exsentences": "5",
            "pageids": self.page_id
        }
        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        return data["query"]["pages"][str(self.page_id)]['extract']
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# BOTANSWER

class TestAnswer:

    BOTANSWER = botAnswer()

    def test_bot1(self):
        assert type(self.BOTANSWER.goodAnswer()) == str

    def test_bot2(self):
        assert type(self.BOTANSWER.badAnswer()) == str


"""
    def proceedAnswer(self):

        try:
            result = requests.head("http://127.0.0.1:3020/")
            print(result.status_code)
            #
            if result.status_code == 200:
                # renvoie réponse +
                return self.goodAnswer()
            else :
                # renvoie réponse -
                return self.badAnswer()

        except requests.ConnectionError:
            print("failed to connect")
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PARSER

class TestParser:

    SENTENCE = Parser('this!, sentence; is: over? <<ponctuated>>')

    def test_ponctuation1(self):
        assert ',' not in self.SENTENCE.ponctuation()

    def test_ponctuation2(self):
        assert '>' not in self.SENTENCE.ponctuation()

    def test_list_it(self):
        assert type(self.SENTENCE.list_it()) == list

    def test_delete_common_words(self):
        assert type(self.SENTENCE.delete_common_words()) == str