from app.parser import Parser

class TestParser:

    SENTENCE = Parser('this!, sentence; is: over? <<ponctuated>>')

    def __init__(self, text):
        self.text = text
        self.ban = '!?#<>'
        self.parse = self._parsing()

    def test_ponctuation1(self):
        assert ',' not in self.SENTENCE.ponctuation()

    def test_ponctuation2(self):
        assert '>' not in self.SENTENCE.ponctuation()

    def test_list_it(self):
        assert type(self.SENTENCE.list_it()) == list

    def test_delete_common_words(self):
        assert type(self.SENTENCE.delete_common_words()) == str

    def _parsing(self):
        return ''.join(' ' if c in self.ban else c for c in self.text)