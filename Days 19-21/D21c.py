import itertools
import os
import urllib.request
import functools
from time import perf_counter
import socket

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
letters_score = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split(' ')}


def measure_time(func):
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        begin = perf_counter()
        res = func(*args, **kwargs)
        end = perf_counter()
        print("Function {} executed in {:.2f} seconds.".format(func.__name__, end - begin))
        return res

    return _wrapper


@measure_time
def get_possible_dict_words(draw, dictionary):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    results = []
    for result in get_permutations_draw(draw):
        for item in result:
            if "".join(item).lower() in dictionary:
                results.append("".join(item).lower())
    return set(results)


def compute_score(word):
    return sum([letters_score[letter] for letter in word.upper()])


@measure_time
def find_word_with_highest_score(words):
    scores = dict()
    for word in words:
        scores[word] = compute_score(word)

    return max(scores.items(), key=lambda x: x[1])


@measure_time
def get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    for i in range(2, len(draw) + 1):
        yield itertools.permutations(draw, i)


@measure_time
def get_dictionary(dico, dictionary):
    if not os.path.exists(dictionary):
        try:
            urllib.request.urlretrieve(
                f'https://bites-data.s3.us-east-2.amazonaws.com/{dico}',
                dictionary)
        except socket.gaierror:
            print("It seems something is wrong with your Internet connection...")
        except urllib.error.URLError:
            print("There is an issue with the URL provided")

    try:
        with open(dictionary) as f:
            stored_dictionary = set([word.strip().lower() for word in f.read().split()])
    except FileNotFoundError:
        print("Couldn't find file {}".format(dictionary))
        stored_dictionary = None
    finally:
        return stored_dictionary


if __name__ == '__main__':
    TMP = os.getenv("TMP", "/tmp")
    DICT = 'dictionary.txt'
    DICTIONARY = os.path.join(TMP, DICT)
    draw = 'H, E, I, A, T, B, R'
    draw = draw.split(', ')
    dictionary = get_dictionary(DICT, DICTIONARY)
    if dictionary:
        results = get_possible_dict_words(draw, dictionary)
        word = find_word_with_highest_score(results)
        print("The word with the highest score is {} with a score of {}".format(word[0], word[1]))
    else:
        print("Something went wrong...")
