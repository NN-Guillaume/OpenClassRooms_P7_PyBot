from app.bot import botAnswer

class TestAnswer:

    BOTANSWER = botAnswer()

    def test_bot1(self):
        assert type(self.BOTANSWER.goodAnswer()) == str

    def test_bot2(self):
        assert type(self.BOTANSWER.badAnswer()) == str