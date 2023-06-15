import requests
from bs4 import BeautifulSoup


class DataMiner(object):

    def __init__(self):
        self.BASE_URL = "https://www.futurelearn.com/courses"
        self.SEARCH_URL = "https://www.futurelearn.com/search?filter_type=course&q="
        self.page = 0
        self.client = requests

    def get_courses(self, topic: str):
        soup = self._make_request(topic)

        ul_tag = soup.find('ul', class_='m-link-list--search-results')
        li_tags = ul_tag.find_all('li', class_='m-link-list__item')

        courses = self._convert_courses_to_list(topic, li_tags)

        return courses

    def _convert_courses_to_list(self, topic: str, li_tags: list):
        courses = []

        for li_tag in li_tags:
            h3_tag = li_tag.find('h3')
            a_tag = h3_tag.find('a')
            parent_tag = a_tag.parent
            p_tag = parent_tag.find_next_sibling('p')
            if (
                topic.lower() in a_tag.text.lower()
                or
                topic.lower() in p_tag.text.lower()
            ):
                courses.append({"name": a_tag.text, "description": p_tag.text})
        return self._remove_duplicates(courses)

    def _remove_duplicates(self, dictionary_list: list):
        unique_dictionaries = []
        seen_values = set()

        for dictionary in dictionary_list:
            values = tuple(dictionary.values())

            if values not in seen_values:
                seen_values.add(values)
                unique_dictionaries.append(dictionary)

        return unique_dictionaries

    def _make_request(self, endpoint: str):
        response = self.client.get("{}/{}".format(
            self.SEARCH_URL,
            endpoint
            ),
            headers={'User-Agent': 'Mozilla/5.0'},
        )

        if response.status_code != 200:
            raise self.client.HTTPError(f"HTTP request error. Status code: {response.status_code}")

        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

