# querying the OMDb API
# http://www.omdbapi.com/?apikey=xxxxxxxx&

import json
from pprint import pprint
import requests
from typing import Dict
import sys

URL = "http://www.omdbapi.com/"
APIKEY = "xxxxxxxx"


def get_json_data(search: str) -> Dict:
    url = URL + '?apikey=' + APIKEY + '&t=' + search + '&plot=full'
    try:
        r = requests.get(url)
    except requests.exceptions.HTTPError as e:
        print(f'Got an HTTP error {e}')
        sys.exit(1)

    r.raise_for_status()

    return json.loads(r.text)


def main():
    search_term = input('What would you like to search for? ')

    result = get_json_data(search_term)

    # pprint(result)
    print(result['Title'])
    print(result['Plot'])


if __name__ == '__main__':
    main()
