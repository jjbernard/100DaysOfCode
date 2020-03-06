import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult', 
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')

search = input('What would you like to search for? ')
url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()
movie_data = resp.json()

movies_list = movie_data.get('hits')

#print(movies_list)

movies = [MovieResult(**md) for md in movies_list]
#for md in movies_list:
#    m = MovieResult(**md)
#    movies.append(m)

print('Found {} movies for search {}'.format(len(movies), search))
for m in movies:
    print('{} ---- {}'.format(m.year, m.title))