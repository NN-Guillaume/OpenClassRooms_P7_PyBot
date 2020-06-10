from app.words_list import *
import re


class Parser:
    """manage the user input and prevent XSS loophole"""

    def __init__(self, value):
        self.input = value

    def ponctuation(self):
        """ Remove all punctuation """

        PONCTUATION = ",;.:/?!#=+<>()"
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
            if item.lower() not in STOPWORDS:
                not_common_words.append(item)
        self.input = " ".join(not_common_words)
        print(self.input)
        return self.input

        # ------------------------------------------------------------------------

    def regul_express(self):
        """can prevent from XSS loophole too"""
        # exemple
        # p = re.compile('(blue|white|red)')
        # p.sub('colour', 'blue socks and red shoes') # remplace les couleurs par le mot 'color'
        #'colour socks and colour shoes'

        p = re.compile('|[|]|{|}|(|)|<|>|"|/|!|?|\\|.|\|')
        p.sub(" ", self.input)
        return self.input
