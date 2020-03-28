import json
import requests
from collections import namedtuple
from typing import List
import webbrowser

SEARCH_URL = 'https://search.talkpython.fm/api/search?q='
BASE_URL = 'https://talkpython.fm'

SearchResult = namedtuple('SearchResult', 'category id url title description')


def main():
    print('******* SEARCH TALK PYTHON *******')
    search = input('What would you like to search? ')
    search = search.split(sep=' ')
    search = '-'.join(search)

    res = json.loads(search_api(search))
    res = res['results']

    data = print_results(res)

    while True:
        selection = input('Which episode would you like to view? ')
        try:
            selection = int(selection)
            break
        except ValueError:
            print("You must enter the number corresponding to the episode")

    open_url(data, selection)


def open_url(data: List[SearchResult], selection: int):
    res = [r.url for r in data if r.id == selection]
    full_url = f'{BASE_URL}{res[0]}'
    webbrowser.open(full_url, new=2)


def search_api(search: str) -> str:
    url = f'{SEARCH_URL}{search}'

    r = requests.get(url)

    r.raise_for_status()

    return r.text


def print_results(results: list) -> List[SearchResult]:
    data = [SearchResult(**item) for item in results]
    data = set(data)
    
    print(f'There are {(len(data))} matching episodes')
    for d in data:
        print(f'{d.id}. {d.title}')

    return data


if __name__ == '__main__':
    main()
