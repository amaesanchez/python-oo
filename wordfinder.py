from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path="/usr/share/dict/words"):
        """ Sets path and creates dict of words in file """

        self.path = path
        self.words = self.parse()

    def parse(self):
        """ Parses file from path given """

        file = open(self.path)
        list_of_words = [line for line in file]
        print(f"{len(list_of_words)} words read")
        return list_of_words

    def random(self):
        """ Returns random word """

        return choice(self.words)[:-1]