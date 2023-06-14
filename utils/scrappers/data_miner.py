import requests
from bs4 import BeautifulSoup


class DataMiner(object):


    def __init__(self):
        self.BASE_URL = "https://www.futurelearn.com/courses"
        self.page = 0
        self.client = requests

    def get_course_name(self, topic: str):
        soup = self._make_request(topic)

        return soup.select("p")

    def get_course_description(self, topic: str):
        pass

    def _make_request(self, endpoint: str):
        response = self.client.get("{}/{}".format(
            self.BASE_URL,
            endpoint
            ),
            headers={'User-Agent': 'Mozilla/5.0'},
        )
        print(response.status_code)
        if response.status_code != 200:
            raise self.client.HTTPError(f"HTTP request error. Status code: {response.status_code}")

        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

