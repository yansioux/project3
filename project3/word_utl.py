import random

from . import dictionary_utl


def get_schemes_by_word(dict, word):
    schemes = dictionary_utl.get_schemesandbasewordsforword(
        dict, word)
    return schemes[0] if schemes else []


def get_word_by_scheme(dict, scheme):
    words = dictionary_utl.get_wordsforscheme(dict, scheme)
    return words[random.randint(0, len(words)-1)]
