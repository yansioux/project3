import random
import re

from . import word_utl


# получить случайное предложение из массива схем
def get_randomized_variant(dict, schemes_set):
    random_sentence = ''
    random_schemes = []
    for variant in schemes_set:
        scheme = variant[random.randint(0, len(variant) - 1)]
        random_sentence += word_utl.get_word_by_scheme(dict, scheme) + ' '
        random_schemes.append(scheme)
    return random_sentence, random_schemes


# получить массив схем из предложения
def get_schemes(dict, sentence):
    if sentence:
        # разделим на слова
        words = re.split(r'\s+|\W+', sentence)
        schemes_set = [len(words)]
        # получим по каждому слову массив схем
        schemes_set = [word_utl.get_schemes_by_word(dict,
                                                    word) for word in words]
    return schemes_set, words
