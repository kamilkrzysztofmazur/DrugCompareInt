import re
import requests
from bs4 import BeautifulSoup
# print('Wpisz nazwe leku 1: ')
# first_drug = 'paracetamol' #input()
# print('Wpisz nazwe leku 2: ')
# second_drug = 'tramadol' #input()
# print('Wpisz nazwe choroby: ')
# disease = 'pain' #input()
# set_of_serch_items = {first_drug, second_drug, disease}
# searching_words = f"{first_drug}+{second_drug}+{disease}"
# no_interaction_set = {
# 'nointeraction',
# 'nointeractions',
# 'nopain',
# 'noadditionalpain',
# 'noservepain',
# 'nosideeffects',
# 'harmless',
# 'save',
# 'nocomplications',
# 'notcausesinflammation',
# 'notcauseinflammation',
# }
class LinksGetter:
    def __init__(self, searching_words):
        self.searching_words = searching_words
        self.link_to_service = None
        self.list_of_article_links = None
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
        self.no_interaction_set = None
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
      
        
        
        
        # for x in self.list_of_abstract_sentence_sets:
        #     if set_of_serch_items.issubset(x) and no_interaction_set.intersection(x):
        #         return True
        #     else:
        #         return False



