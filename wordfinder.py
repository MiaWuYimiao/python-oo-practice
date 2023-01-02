"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """Pick a random word from the file

    >>> wf = WordFinder("words4.txt")
    4 words read
    
    >>> wf.random() in ["Aaronitic", "looker", "illude", "illudedly"]
    True

    >>> wf.random() in ["Aaronitic", "looker", "illude", "illudedly"]
    True

    >>> wf.random() in ["Aaronitic", "looker", "illude", "illudedly"]
    True

    >>> wf.random() in ["Aaronitic", "looker", "illude", "illudedly"]
    True

    """
    
    def __init__(self, path) :
        """Read dictionary and reports # items read."""
        self.path = path
        file = open(self.path)
        text = file.read()
        file.close()
        self.get_word_list(text)
        print(f"{len(self.text_list)} words read")
    
    def get_word_list(self, text) :
        """Parse readin file to list of words"""
        self.text_list = text.split("\n")

    def random(self) :
        """Return a random word"""
        return random.choice(self.text_list)


class SpecialWordFinder(WordFinder):
    """Pick a random word from the file with blank lines and comments

    >>> swf = SpecialWordFinder("words4special.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    Ture

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    Ture

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    Ture

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    Ture
    """


    def get_word_list(self, text) :
        """Parse file -> list of words, skipping blanks/comments"""
        super().get_word_list(text)
        self.text_list = [ word for word in self.text_list 
                            if word != "" and not word.startswith('#') ]

