import uplink
import requests


class MovieSearchClient(uplink.Consumer):

    def __init__(self, baseurl):
        super().__init__(base_url=baseurl)

    @uplink.get("/api/search/{keyword}")
    def get_by_keyword(self, keyword) -> requests.models.Response:
        """ Get movie data by keyword"""

    @uplink.get("/api/director/{director}")
    def get_by_director(self, director) -> requests.models.Response:
        """ Get movie data by director """

    @uplink.get("/api/movie/{imdb_number}")
    def get_by_number(self, imdb_number) -> requests.models.Response:
        """ Get movie data by IMDB number"""
