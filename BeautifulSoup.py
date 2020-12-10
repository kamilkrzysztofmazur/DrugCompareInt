import re
import requests
from bs4 import BeautifulSoup
lek1 = 'tramadol'
lek2 = 'paracetamol'
choroba = 'pain'
set_of_serch_items = {'tramadol','paracetamol','pain'}
list_of_article_links = [
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
'https://link.springer.com/article/10.2165/11205830-000000000-00000',
]
no_interaction_set = {
'no interaction',
'no interactions',
'no pain',
'no additional pain',
'no serve pain',
'no side effects',
'harmless',
'save',
'no complications',
'not causes inflammation',
'not cause inflammation',
}
class Filter:
    def __init__(self, url):
        self.url = url
        self.abstract = None
        self.set_of_abstract_words = None
        self.list_of_abstract_sentence_sets = None
    def get_abstract(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.abstract = soup.find(id="Abs1-section").get_text().lower() # wybiera text z sekcjii Abs1-section
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
        if set_of_serch_items.issubset(self.set_of_abstract_words):
            return True
    def check_abstract_sentences(self):
        for x in self.list_of_abstract_sentence_sets:
            if set_of_serch_items.issubset(x):
                return True
    def check_for_no_interaction_words(self):
        for x in self.list_of_abstract_sentence_sets:
            if set_of_serch_items.issubset(x) and no_interaction_set.intersection(x):
                return True
            else:
                return False
list_of_objects = [Filter(x) for x in list_of_article_links]
list_of_proper_links = []
for x in list_of_objects:
    x.get_data_from_page()
for x in list_of_objects:
    if x.check_abstract() == True:
        if x.check_abstract_sentences() == True:
            if x.check_for_no_interaction_words() == True:
                list_of_proper_links.append(x)
print(list_of_proper_links)