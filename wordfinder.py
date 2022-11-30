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
        list_of_words = [line.strip() for line in file]
        print(f"{len(list_of_words)} words read")

        return list_of_words

    def random(self):
        """ Returns random word """

        return choice(self.words)

class SpecialWordFinder(WordFinder):
    """ Special Word Finder: creates list of words that are not
    blank spaces or start with '#' """

    def parse(self):
        """ returns list of valid words """
        # review why super().words cant be accessed
        # print("super_words", super().words)

        filtered_words = [word for word in super().parse() if
            len(word) > 1 and word[0] != "#"]
        return filtered_words
