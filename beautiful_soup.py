import re
import requests
from bs4 import BeautifulSoup


class LinksGetter:
    def __init__(self, searching_words):
        self.searching_words = searching_words
        self.link_to_service = None
        self.list_of_article_links = None
        self.soup = None
    def get_page_content(self):
        self.link_to_service = requests.get(f'https://pubmed.ncbi.nlm.nih.gov/?term={self.searching_words}')
        self.link_to_service.raise_for_status()
        self.soup = BeautifulSoup(self.link_to_service.content, 'html.parser')
    def get_list_of_links(self):
        content = self.soup.find_all("div", {"class": "docsum-content"})
        self.list_of_article_links = ['https://pubmed.ncbi.nlm.nih.gov'+x.a['href'] for x in content]

class Filter:
    def __init__(self, url):
        self.url = url
        self.abstract = None
        self.set_of_abstract_words = None
        self.set_of_search_items = None
        self.no_interaction_set = {}
        self.abstract_regex = None
        self.list_abstract_sentence = None
        self.list_of_abstract_sentence_sets = None

    def get_abstract(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.abstract = soup.find(id="abstract").get_text().lower() # wybiera text z sekcjii Abs1-section
    def create_set_of_abstract_words(self):
        self.abstract_regex = re.sub(r"[^a-zA-Z]", " ", self.abstract)
        self.set_of_abstract_words = set(self.abstract_regex.split(" "))
    def create_list_of_sets_of_sentence(self):
        self.list_abstract_sentence = self.abstract.split(". ")
        self.list_of_abstract_sentence_sets = [set(re.sub(r"[^a-zA-Z]", " ", x).split(" ")) for x in self.list_abstract_sentence]
    def get_data_from_page(self):
        self.get_abstract()
        self.create_set_of_abstract_words()
        self.create_list_of_sets_of_sentence()
    def check_abstract(self):
        if self.set_of_search_items.issubset(self.set_of_abstract_words):
            return True
    def check_abstract_sentences(self):
        for x in self.list_of_abstract_sentence_sets:
            if self.set_of_search_items.issubset(x):
                return True
    def check_for_no_interaction_words(self):
        for x in self.no_interaction_set:
            if x in self.abstract.replace(' ', ''):
                return True
      

if __name__ == '__main__':
    first_drug = 'paracetamol'
    second_drug = 'tramadol'
    disease = 'pain'
    set_of_search_items = {first_drug, second_drug, disease}
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

    links_getter = LinksGetter(f"{first_drug} + {second_drug} + {disease}")
    links_getter.get_page_content()
    links_getter.get_list_of_links()
    print(links_getter.list_of_article_links)
    list_of_objects = [Filter(x) for x in links_getter.list_of_article_links]
    list_of_proper_links = []
    list_of_proper_links1 = []
    list_of_proper_links2 = []
    for link_x in list_of_objects:
        link_x.set_of_search_items = set_of_search_items
        link_x.no_interaction_set = no_interaction_set
        link_x.get_data_from_page()
    for link_x in list_of_objects:
        if link_x.check_abstract() == True:
            list_of_proper_links.append(link_x.url)
            if link_x.check_abstract_sentences() == True:
                list_of_proper_links1.append(link_x.url)
                if link_x.check_for_no_interaction_words() == True:
                    list_of_proper_links2.append(link_x.url)
