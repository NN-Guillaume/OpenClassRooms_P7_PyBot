# --------------------------------------------------------------- I M P O R T S ------------------------------------------------------------------------------------------
import geocoder
import random
import requests

from app.config import *
from requests import get
from app.words_list import *

"""
def traitement(question):
    coord = geocode(question)
    return "Votre question est: " + question
"""

# ------------------------------------------------------------- G O O G L E   C L A S S ----------------------------------------------------------------------------------


class Geo:
    def __init__(self, question):
        self.latitude = float
        self.longitude = float
        self.address = str
        self.question = question

    def get_coordonnees(self):
        """Thanks to the user input Google will find the localisation"""

        g = geocoder.google(
            self.question, key=key_value
        )
        data = g.json
        self.latitude = data["lat"]
        self.longitude = data["lng"]
        return self.latitude, self.longitude

    def get_address(self, coordonnees):
        """Find the wanted address thanks to the geographical coordinates"""

        g = geocoder.google(
            coordonnees, method="reverse", key=key_value
        )
        data = g.json
        self.address = data["address"]
        return self.address


# -------------------------------------------------------------    W I K I    C L A S S    --------------------------------------------------------------------------------


class Wiki:
    def __init__(self, lat, lng):
        self.lat_lng = "|".join([str(lat), str(lng)])
        # lat_lng = str(lat) + "|" + str(lng)
        self.page_id = self.__get_page_id()
        self.summary = self.__get_summary()

    def __get_page_id(self):
        """request to wikipedia to check pages about a place near of google
        coordinates. Select the first result which mean the nearest place"""

        parameters = {
            "action": "query",
            "list": "geosearch",
            "gsradius": 1000,
            "gscoord": self.lat_lng,
            "format": "json",
        }
        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        return data["query"]["geosearch"][0]["pageid"]

    def __get_summary(self):
        """request to wikipedia. Extract a summary from the page"""

        parameters = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1,
            "exsentences": "5",
            "pageids": self.page_id,
        }
        response = get("https://fr.wikipedia.org/w/api.php", params=parameters)
        data = response.json()
        return data["query"]["pages"][str(self.page_id)]["extract"]


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------


class botAnswer:
    """ Create the answer of the bot """

    def __init__(self):
        self.result = int
        # self.proceed = self.__proceed_answer

    def goodAnswer(self):
        """ Bot return a positive answer """

        self.answer_list = [
            "Lieu trouvé, présence de débit de boissons confirmé, prêt à partir à votre signal Commandant",
            "Voici ce que dit mon guide des castors juniors au sujet de ce lieu",
            "Par-là j'ai flashé Lance Armstrong à 150 Km/h. Et en ville en plus",
            "C'est en ce lieu que j'ai coffré Pikachu",
            "Un soir j'ai arrêté Elsa à cet endroit (j'en avais assez de l'entendre chanter)",
            "Ici j'ai vu Shrek vendre de l'herbe à chat au Chat Potté",
            "Il me semble qu'ici j'ai interpellé monsieur Chopin pour tapage nocturne",
            "Là, j'ai surpris Optimus Prime en train de trafiquer son compteur kilométrique",
            "Dans cette rue j'ai coller un PV à Bumblebee qui était garé en double file",
            "Sur cette place j'ai molester Bill Gates pour avoir abandonné Windows 7"
        ]
        # return random.choice(self.answer_list)
        return random.choice(self.answer_list)

    def badAnswer(self):
        """ Bot return a negative answer """

        self.answer_list = [
            "Accès refusé, ta requête est erronée",
            "Navré mais je n'ai rien trouvé dans ma mémoire qui correspond à ta demande",
            "Je pense que quelques heures en dégrisement te ferait le plus grand bien...",
        ]
        return random.choice(self.answer_list)

    def proceedAnswer(self):
        return self.goodAnswer()


"""
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

# création d'une méthode vérifiant la réponse HTTP ?

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def addition(x, y):
    resultat = x + y
    return resultat


class Calcul:
    def __init__(self):
        self.x = input()
        self.y = input()

    def addition(self):
        resultat = self.x + self.y
        return resultat


# ------------------------------------------------------------- P A R S E R   C L A S S ----------------------------------------------------------------------------------


class Parser:
    def __init__(self, value):
        self.input = value

    def ponctuation(self):
        """ Remove all punctuation """

        PONCTUATION = ",;.:/!#=+<>"
        for item in PONCTUATION:
            if item in self.input:
                self.input = self.input.replace(item, " ")
        return self.input

    def list_it(self):
        """ Transforms sentence into list (1 word = 1 element of the list) """

        self.input = self.input.split()
        return self.input

    def delete_common_words(self):
        """For each element in the list, compare it with a constant list of
        common words. If the element is not in the common words list, add it in
        a thrid list. This will be finally convert into a character string"""

        not_common_words = []
        for item in self.input:
            if item not in STOPWORDS:
                not_common_words.append(item)
        self.input = " ".join(not_common_words)
        print(self.input)
        return self.input
