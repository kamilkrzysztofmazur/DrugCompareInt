import re
import requests
from bs4 import BeautifulSoup

first_drug = 'paracetamol'

second_drug = 'tramadol'

disease = 'pain'
set_of_search_items = {first_drug, second_drug, disease}
searching_words = f"{first_drug} + {second_drug} + {disease}"
no_interaction_set = {
    'nointeraction',
    'nointeractions',
    'nopain',
    'noadditionalpain',
    'noservepain',
    'nosideeffects',
    'harmless',
    'save',
    'nocomplications',
    'notcausesinflammation',
    'notcauseinflammation',
    }


class LinksGetter:

    def __init__(self, searching_words):
        self.searching_words = searching_words
        self.soup = BeautifulSoup(self.link_to_service.content, 'html.parser')
        self.link_to_service = None
        self.list_of_article_links = None

    def get_page_content(self):
        self.link_to_service = requests.get(f'https://pubmed.ncbi.nlm.nih.gov/?term={searching_words}')
        self.link_to_service.raise_for_status()

    def get_list_of_links(self):
        content = self.soup.find_all("div", {"class": "docsum-content"})
        self.list_of_article_links = ['https://pubmed.ncbi.nlm.nih.gov'+x.a['href'] for x in content]


class Filter:

    def __init__(self, url):
        self.list_abstract_sentence = self.abstract.split(". ")
        self.abstract_regex = re.sub(r"[^a-zA-Z]", " ", self.abstract)
        self.url = url
        self.abstract = None
        self.set_of_abstract_words = None
        self.list_of_abstract_sentence_sets = None

    def get_abstract(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.abstract = soup.find(id="abstract").get_text().lower()  # selects text from the section Abs1-section

    def create_set_of_abstract_words(self):
        self.set_of_abstract_words = set(self.abstract_regex.split(" "))

    def create_list_of_sets_of_sentence(self):
        self.list_of_abstract_sentence_sets = [set(re.sub(r"[^a-zA-Z]", " ", x).split(" "))
                                               for x in self.list_abstract_sentence]

    def get_data_from_page(self):
        self.get_abstract()
        self.create_set_of_abstract_words()
        self.create_list_of_sets_of_sentence()

    def check_abstract(self):
        if set_of_search_items.issubset(self.set_of_abstract_words):
            return True

    def check_abstract_sentences(self):
        for sentence in self.list_of_abstract_sentence_sets:
            if set_of_search_items.issubset(sentence):
                return True

    def check_for_no_interaction_words(self):
        for sentence in no_interaction_set:
            if sentence in self.abstract.replace(' ', ''):
                return True

object = LinksGetter(searching_words)
object.get_page_content()
object.get_list_of_links()
print(object.list_of_article_links)
list_of_objects = [Filter(x) for x in object.list_of_article_links]
list_of_proper_links = []
for x in list_of_objects:
    x.get_data_from_page()
for x in list_of_objects:
    if x.check_abstract():
        if x.check_abstract_sentences():
            if x.check_for_no_interaction_words():
                list_of_proper_links.append(x.url)
print(list_of_proper_links)
