import itertools
import os
import urllib.request


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


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    for i in range(2, len(draw) + 1):
        yield itertools.permutations(draw, i)


if __name__ == '__main__':
    # PREWORK
    TMP = os.getenv("TMP", "/tmp")
    DICT = 'dictionary.txt'
    DICTIONARY = os.path.join(TMP, DICT)

    if not os.path.exists(DICTIONARY):
        urllib.request.urlretrieve(
            f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
            DICTIONARY)

    with open(DICTIONARY) as f:
        dictionary = set([word.strip().lower() for word in f.read().split()])

    draw = 'T, I, I, G, T, T, L'
    draw = draw.split(', ')
    results = get_possible_dict_words(draw)

    print(results)
