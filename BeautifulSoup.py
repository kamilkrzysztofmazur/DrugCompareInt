import requests
from bs4 import BeautifulSoup


page = requests.get('https://link.springer.com/article/10.2165/11205830-000000000-00000')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
abstract = soup.find(id="Abs1-section").get_text()
print(abstract)
#str(abstract)
#print(abstract.find('Tramadol'))


lek1 = 'tramadol'
lek2 = 'paracetamol'
choroba1 = 'pain'


#if lek1 and lek2 and choroba in abstract:
#    print('znaleziono podane zmienne')
#else:
#    print('nie znaleziono')


zdania = abstract.split(". ")
print(zdania)

for i in zdania:
    if lek1 and lek2 and choroba1 in i:
        print('znaleziono podane zmienne w jednym zdaniu --> może zachodzić interakcja. Nalezy się skonsultować z lekarzem lub farmaceutą i zapoznac z artyklem')
    else:
        print('nie znaleziono ich razem w zdaniu')

