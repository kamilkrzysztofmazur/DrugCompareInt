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




# funkcja sprawdzająca czy w abstrakcie występują trzy słowa kluczowe, 
def check_abstract(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    abstract = soup.find(id="Abs1-section").get_text() # wybiera text z sekcjii Abs1-section
    abstract = abstract.replace(", "," ")
    abstract = abstract.replace("/"," ")
    set_of_abstract_words = set(abstract.split(" "))
    if set_of_serch_items.issubset(set_of_abstract_words):
        return url
    # if lek1 and lek2 and choroba in abstract:
    #     return url
        

#funkcja sprawdzająca czy w zdaniach abstraku występują trzy słowa kluczowe 
def check_abstract_sentences(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    abstract = soup.find(id="Abs1-section").get_text() # wybiera text z sekcjii Abs1-section
    abstract = abstract.replace(", "," ")
    abstract = abstract.replace("/"," ")
    list_abstract_sentence = [abstract.split(". ")]
    for x in list_abstract_sentence:
        set_of_serch_items.issubset(set(x))
        return url
    # for sentence in list_of_sentence:
    #     if lek1 and lek2 and choroba in sentence:
    #         return url

            

# funkcja sprawdzająca czy w zdaniach abstraku występują trzy słowa kluczowe i słowa  typu "no interaction"
def check_abstract_sentences_interaction_words(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    abstract = soup.find(id="Abs1-section").get_text() # wybiera text z sekcjii Abs1-section
    abstract = abstract.replace(", "," ")
    abstract = abstract.replace("/"," ")
    list_abstract_sentence = [abstract.split(". ")]
    for x in list_abstract_sentence:
        set_of_serch_items.issubset(set(x))
        no_interaction_set.intersection(set(x))
        return url
    # for sentence in list_of_sentence:
    #     if lek1 and lek2 and choroba in sentence:
    #         for word in no_interaction_list:
    #             if word in sentence:
    #                 return url

list_of_first_loop_result = [check_abstract(x) for x in list_of_article_links]
list_of_second_loop_result = [check_abstract_sentences(x) for x in list_of_first_loop_result]
list_of_third_loop_result = [check_abstract_sentences_interaction_words(x) for x in list_of_second_loop_result]

print(list_of_third_loop_result)

# funkcja zwracająca uszczuploną listę linków ( gdy w abstrakcie występują wymienione słowa)
# list_of_article_links_with_all_words_in_abstract = 
# #if lek1 and lek2 and choroba in abstract:
# #    print('znaleziono podane zmienne')
# #else:
# #    print('nie znaleziono')
# for i in zdania:
#     if lek1 and lek2 and choroba1 in i:
#         print('znaleziono podane zmienne w jednym zdaniu --> może zachodzić interakcja. Nalezy się skonsultować z lekarzem lub farmaceutą i zapoznac z artyklem')
#     else:
#         print('nie znaleziono ich razem w zdaniu')
# search = f"{lek1}+{lek2}+{choroba}"
# print(search)
# #if lek1 and lek2 and choroba in abstract:
# #    print('znaleziono podane zmienne')
# #else:
# #    print('nie znaleziono')
# zdania = abstract.split(". ")
# liczba_zdan_negatywnych = 0
# for liczba_zdan, i in enumerate(zdania):
#     if lek1 and lek2 and choroba in i:
#         pass
#     else:
#         liczba_zdan_negatywnych +=1
# procent = (1-(liczba_zdan_negatywnych/liczba_zdan)) * 100
# print(f'Pierwszy grade artykułu {procent} %.')