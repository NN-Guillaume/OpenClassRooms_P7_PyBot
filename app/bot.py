import random

class botAnswer:
    """ Create the answer of the bot """

    def __init__(self):
        self.result = int

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
            "Sur cette place j'ai molester Bill Gates pour avoir abandonné Windows 7",
        ]
        return random.choice(self.answer_list)

    def badAnswer(self):
        """ Bot return a negative answer """

        self.answer_list = [
            "Accès refusé, ta requête est erronée",
            "Navré mais je n'ai rien trouvé dans ma mémoire qui correspond à ta demande",
            "Je pense que quelques heures en dégrisement te ferait le plus grand bien...",
        ]
        return random.choice(self.answer_list)

    def proceedGoodAnswer(self):
        return self.goodAnswer()

    def proceedBadAnswer(self):
        return self.badAnswer()