import requests
import collections
import json

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')


def request_search_from_user():
    search = input('What would you like to search for? ')
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)
    return url


def get_movie_data(url):
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("There is an issue with your Internet connection")
        return None
    try:
        movie_data = resp.json()
    except json.decoder.JSONDecodeError:
        print("Issue with the data received, cannot process it")
        return None
    return movie_data


def build_movie_list(data):
    movies_list = data.get('hits')
    movie_list = [MovieResult(**md) for md in movies_list]
    return movie_list

#
# def print_movies(lst):
#     print('Found {} movies for search {}'.format(len(movies), search))
#     for m in movies:
#         print('{} ---- {}'.format(m.year, m.title))


if __name__ == '__main__':
    url = request_search_from_user()
    data = get_movie_data(url)
    if data:
        lst = build_movie_list(data)
        print(lst)
    else:
        print("Exiting... Try again later")