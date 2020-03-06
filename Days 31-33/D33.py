import sys
import requests
import collections
import json
import logbook

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')


def request_search_from_user(log=None):
    while True:
        search = input('What would you like to search for? ')
        if search.strip() == '':
            print("You must enter a search term")
            log.warn("Missing search term")
            continue
        log.notice('searching for {}'.format(search))
        url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)
        return url, search


def get_movie_data(url, log=None):
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("There is an issue with your Internet connection")
        log.critical('No internet connection')
        return None
    log.trace('Received status code {}'.format(resp.status_code))
    try:
        movie_data = resp.json()
    except json.decoder.JSONDecodeError:
        print("Issue with the data received, cannot process it")
        log.error('Bad JSON data received')
        return None
    return movie_data


def build_movie_list(data):
    movies_list = data.get('hits')
    movie_list = [MovieResult(**md) for md in movies_list]
    return movie_list


def print_movies(lst, search, log=None):
    print('Found {} movies for search {}'.format(len(lst), search))
    log.info('Search term {} retrieved {} movie{}.'.format(search, len(lst), '' if len(lst) <= 1 else 's'))
    for m in lst:
        print('{} ---- {}'.format(m.year, m.title))


def setup_logging(filename=None):
    level = logbook.TRACE
    log_filename = filename
    if not log_filename:
        logbook.StreamHandler(sys.stdout, level=level).push_application()
    else:
        logbook.TimedRotatingFileHandler(log_filename, level=level).push_application()

    app_log = logbook.Logger('Movie App')
    return app_log


if __name__ == '__main__':
    #log = setup_logging('app-log')
    log = setup_logging()
    log.notice('Starting movie search application')
    url, search = request_search_from_user(log=log)
    data = get_movie_data(url, log=log)

    if data:
        lst = build_movie_list(data)
        print_movies(lst, search, log=log)
    else:
        print("Exiting... Try again later")
        log.warn('Exiting with errors')

    log.notice('Exiting application')
