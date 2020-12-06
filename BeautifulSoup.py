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
        self.abstract = soup.find(id="Abs1-section").get_text() # wybiera text z sekcjii Abs1-section
    
    def create_set_of_abstract_words(self):
        abstract1 = self.abstract.replace(", "," ")
        abstract2 = self.abstract.replace("/"," ")
        self.set_of_abstract_words = set(abstract2.split(" "))

    def create_list_of_sets_of_sentence(self):
        abstract1 = self.abstract.replace(", "," ")
        abstract2 = self.abstract.replace("/"," ")
        self.list_abstract_sentence = abstract2.split(". ")
        self.list_of_abstract_sentence_sets = []
        self.list_of_abstract_sentence_sets = [set(x.split(" ")) for x in self.list_abstract_sentence] 
    
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

    #def check_abstract_sentence(self):

            

obiekt = Filter('https://link.springer.com/article/10.2165/11205830-000000000-00000')

obiekt.get_data_from_page()

print(obiekt.check_for_no_interaction_words())



# list_of_objects = []
# list_of_first_loop_result = []
# list_of_second_loop_result = []

# for x in list_of_article_links:
#     list_of_objects.append(MyClass(x))

# for x in list_of_objects:
#     if set_of_serch_items.issubset(x.set_of_abstract_words):
#         list_of_first_loop_result.append(x.url)


# for x in list_of_objects:
#     for y in x.list_abstract_sentence:
#         print(x.list_abstract_sentence)
        # if set_of_serch_items.issubset(y):
        #     list_of_second_loop_result.append(x.url)
        

# print(list_of_second_loop_result)


# list_of_first_loop_result = [check_abstract(x) for x in list_of_article_links]
# list_of_second_loop_result = [check_abstract_sentences(x) for x in list_of_first_loop_result]
# list_of_third_loop_result = [check_abstract_sentences_interaction_words(x) for x in list_of_second_loop_result]

# print(list_of_first_loop_result)

