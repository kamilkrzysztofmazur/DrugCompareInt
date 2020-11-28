import requests
from bs4 import BeautifulSoup

page = requests.get('https://link.springer.com/article/10.2165/11205830-000000000-00000')
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('Tramadol paracetamol pain'))
lek1 = soup.find(id = 'Tramadol')

lek2 = soup.find(id = 'paracetamol')

choroba = soup.find(id = 'pain')

print(lek1)
print(lek2)
print(choroba)

