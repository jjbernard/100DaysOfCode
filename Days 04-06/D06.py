import csv
import os
from urllib.request import urlretrieve
from collections import namedtuple, defaultdict

movie_data = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
movie_csv = 'movies.csv'

# todo: extract first line of movie_data file instead

Movies = namedtuple('Movies',
                    "color director_name num_critic_for_reviews duration director_facebook_likes actor_3_facebook_likes\
                     actor_2_name actor_1_facebook_likes gross genres actor_1_name movie_title num_voted_users \
                     cast_total_facebook_likes actor_3_name facenumber_in_poster plot_keywords movie_imdb_link \
                     num_user_for_reviews language country content_rating budget title_year actor_2_facebook_likes \
                     imdb_score aspect_ratio movie_facebook_likes")

MoviesShort = namedtuple('MoviesShort', 'title year score')


def print_header():
    print('-----------------------------------')
    print('     MOVIE DIRECTOR RANKING')
    print('-----------------------------------')
    print()


def get_data_from_file(file):
    with open(file, encoding='utf-8') as f:
        line = csv.DictReader(f)
        yield line


def create_movies_dataset(file):
    pass


def get_movies_list(data=movie_csv):
    with open(data, encoding='utf-8') as f:
        return [Movies(**line) for line in csv.DictReader(f)]


def get_movies_by_director(film_list, earliest_year):
    directors = defaultdict(list)
    for film in film_list:
        try:
            if int(film.title_year) <= earliest_year:
                continue
            director = film.director_name
            year = int(film.title_year)
            title = film.movie_title.replace('\xa0', '')
            score = float(film.imdb_score)
        except ValueError:
            continue

        m = MoviesShort(title=title, year=year, score=score)
        directors[director].append(m)

    return directors


def compute_average_imdb_score_per_director(directors_list, min_number):
    director_scores = defaultdict(list)
    for director, movies in directors_list.items():
        if len(movies) < min_number:
            continue
        else:
            score = 0
            length = 0
            for movie in movies:
                score += movie.score
                length += 1
            director_scores[director].append(round(score / length, 2))

    return director_scores


def print_director_ranking(ranking, directors, number):
    counter = 0

    for k, v in ranking.items():
        print("{:<40} {:>40}".format(str(k), str(v)))
        print('-' * 81)
        for movie in directors[k]:
            print('{:<40} {:>40}'.format(movie.title.strip()[:45], movie.score))
        print()
        counter += 1
        if counter >= number:
            break


def user_input(msg: str, error_msg: str):
    while True:
        try:
            result = input(msg)
            int(result)
            break
        except ValueError:
            print(error_msg)

    return int(result)


def ask_user_for_input():
    year = user_input('What is the earliest year of analysis for this dataset? [YYYY] ',
                      'You should enter the earlier year of analysis')
    number = user_input('How many directors would you like to list? ',
                        'You should enter the maximum number of directors for the analysis')
    number_of_movies = user_input('How many movies at minimum should we consider per director? ',
                                  'You should enter the minimum number of movies per \
                                  director for consideration')

    return year, number, number_of_movies


if __name__ == '__main__':
    print_header()
    year, number, number_of_movies = ask_user_for_input()
    print()
    if not os.path.exists(movie_csv):
        urlretrieve(movie_data, movie_csv)

    data = get_movies_list(data=movie_csv)
    directors = get_movies_by_director(data, year)
    scores = compute_average_imdb_score_per_director(directors, number_of_movies)

    ranking = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}

    print_director_ranking(ranking, directors, number)
