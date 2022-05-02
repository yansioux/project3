import pickle5 as pickle

import pickle5 as pickle
import bz2


def load_dict(dict_file):
    with bz2.open(dict_file, 'rb') as file:
        return pickle.load(file)


def get_schemesandbasewordsforword(dict, word):
    schemeandbaseword = dict.get('words').get(word.strip().lower())
    return schemeandbaseword


def get_wordsforscheme(dict, scheme):
    words = dict.get('schemes').get(scheme)
    return words
