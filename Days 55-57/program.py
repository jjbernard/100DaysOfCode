import api
from typing import Tuple, Dict
from pprint import pprint

BASE_URL = "http://movie_service.talkpython.fm/"


def header():
    print("************************************")
    print("        MOVIE SEARCH")
    print("************************************")
    print()


def get_search_query() -> Tuple:
    while True:
        type_req = input("Would you like to search by [k]eyword, [d]irector or [i]mdb number? ")
        if type_req.lower() in ["k", "d", "i"]:
            break
        else:
            continue

    query = input("What is your search term? ")

    return type_req, query.lower()


def query_api(search: Tuple) -> Dict:
    client = api.MovieSearchClient(BASE_URL)

    if search[0] == "k":
        response = client.get_by_keyword(search[1])
        response.raise_for_status()
    elif search[0] == "d":
        response = client.get_by_director(search[1])
        response.raise_for_status()
    else:
        response = client.get_by_number(search[1])
        response.raise_for_status()

    data = response.json()

    return data


if __name__ == '__main__':
    header()
    search = get_search_query()
    data = query_api(search)
    pprint(data)
