import itertools
import os
import urllib.request
import functools

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)


# Todo: compute a score finder
# Todo: compute a higher score finder
# Todo: create a decorator to measure speed of functions
# Todo: create a decorator to store / retrieve already computed higher score finder

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    results = []
    for result in _get_permutations_draw(draw):
        for item in result:
            if "".join(item).lower() in dictionary:
                results.append("".join(item).lower())
    return set(results)


def compute_score(word):
    pass


def find_higher_score(words):
    pass


def measure_speed(func):
    pass


def cache_scores(func, size=None):
    pass


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    for i in range(2, len(draw) + 1):
        yield itertools.permutations(draw, i)


def get_dictionary(dico=DICT, dictionary=DICTIONARY):
    if not os.path.exists(dictionary):
        urllib.request.urlretrieve(
            f'https://bites-data.s3.us-east-2.amazonaws.com/{dico}',
            dictionary)

    with open(dictionary) as f:
        stored_dictionary = set([word.strip().lower() for word in f.read().split()])

    return stored_dictionary


if __name__ == '__main__':
    draw = 'T, I, I, G, T, T, L'
    draw = draw.split(', ')
    results = get_possible_dict_words(draw)

    print(results)
