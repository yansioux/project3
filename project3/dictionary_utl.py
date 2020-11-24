import compress_pickle as pickle


def load_dict(dict_file):
    with open(dict_file, 'rb') as file:
        return pickle.load(file, 'bz2')


def get_schemesandbasewordsforword(dict, word):
    schemeandbaseword = dict.get('words').get(word.strip().lower())
    return schemeandbaseword


def get_wordsforscheme(dict, scheme):
    words = dict.get('schemes').get(scheme)
    return words
