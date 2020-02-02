# Analyse ratings of movie directors
from urllib.request import urlretrieve
import csv
from collections import namedtuple, defaultdict, Counter

movie_data = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'

movie_csv = 'movies.csv'

urlretrieve(movie_data, movie_csv)

movies = namedtuple('movies', 'title year score')


def get_movies_by_director(data=movie_csv):
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                year = int(line['title_year'])
                title = line['movie_title'].replace('\xa0', '')
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = movies(title=title, year=year, score=score)
            directors[director].append(m)

    return directors


d = get_movies_by_director()
cnt = Counter()
for director, movies in d.items():
    cnt[director] += len(movies)

# print(cnt.most_common(10))

# Let's now try to rank the directors according to their average movies' imdb scores

directorscore = defaultdict(list)

for director, movies in d.items():
    ranksum = 0
    for i in range(len(movies)):
        ranksum += movies[i][2]
    averagescore = ranksum / len(movies)
    directorscore[director].append(averagescore)

print(sorted(directorscore.items(), key=lambda k_v: k_v[1][0], reverse=True))
