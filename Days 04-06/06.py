import csv
from urllib.request import urlretrieve
from collections import namedtuple, defaultdict, Counter

movie_data = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
movie_csv = 'movies.csv'
urlretrieve(movie_data, movie_csv)

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


def ask_for_earliest_year():
    year = input('What is the earliest year of analysis for this dataset? ')
    return year


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
    # for k, v in ranking.items():
    #     print('{} has an average score of {} from IMDB'.format(k, v))
    counter = 0

    for k, v in ranking.items():
        print("{:<30} {:>30}".format(str(k), str(v)))
        print('-'*61)
        for movie in directors[k]:
            print('{:<30} {:>30}'.format(movie.title, movie.score))
        print()
        counter += 1
        if counter >= number:
            break


def ask_for_how_many_directors_to_print():
    number = input('How many directors would you like to list? ')
    return int(number)


def ask_how_many_movies_to_count_per_director():
    number = input('How many movies at minimum should we consider per director? ')
    return int(number)


if __name__ == '__main__':
    print_header()
    year = ask_for_earliest_year()
    number = ask_for_how_many_directors_to_print()
    number_of_movies = ask_how_many_movies_to_count_per_director()
    print()
    data = get_movies_list(data=movie_csv)
    directors = get_movies_by_director(data, int(year))
    scores = compute_average_imdb_score_per_director(directors, number_of_movies)

    ranking = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}

    print_director_ranking(ranking, directors, number)
