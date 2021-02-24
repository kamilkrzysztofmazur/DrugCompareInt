import requests
from bs4 import BeautifulSoup
from lxml import html

'''
class Drug1:

    def __init__(self, url):
        self.url = url
        self.nazwa_produktu = None
        self.nazwa_powszechnie_stosowana = None
        self.moc = None
        self.substancja_czynna = None
        self.postac_farmaceutyczna = None
        self.podmiot_odpowiedzialny = None
        self.waznosc_pozwolenia = None
        self.link_do_PDF = None
        self.tree = None
        self.page = None


    def find_by_xpath(self):
        self.page = requests.get(self.url)
        self.tree = html.fromstring(self.page.content)
        # This will create a list of drugs:
        self.nazwa_produktu = self.tree.xpath('/html/body/form/div[5]/div[4]/div/div/dl/dd[1]/text()')
        # This will create a list of prices
        self.nazwa_powszechnie_stosowana = self.tree.xpath('/html/body/form/div[5]/div[4]/div/div/dl/dd[3]/text()')


url1 = f'https://pub.rejestrymedyczne.csioz.gov.pl/ProduktSzczegoly.aspx?id=225'
xpath_expression1 = f'#prezentacja > div > div > dl > dd > [1] '

Pierwszy = Drug1(url1)
Pierwszy.find_by_xpath()
print(Pierwszy.page)



#def parse_name_from_soup(self):
        #self.page = requests.get(self.url)
        #self.soup = BeautifulSoup(self.page.content, 'lxml')
        #self.nazwa_produktu = self.soup.select('#prezentacja > div > div > dl > dd > [1]').get_text()

        #xpath("""//*[@id="prezentacja"]/div/div/dl/dd[1]""")
        #xpath("""//*[id="prezentacja"]/div/div/dl/dd[1]""")

#url1 = f'https://pub.rejestrymedyczne.csioz.gov.pl/ProduktSzczegoly.aspx?id=225'

#Pierwszy = Drug1(url1)
#Pierwszy.parse_name_from_soup()
#print(Pierwszy.nazwa_produktu)



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("""//*[@id="prezentacja"]/div/div/dl/dd[1])""")


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

    path = """//*[@id="prezentacja"]/div/div/dl/dd[1])"""
    search_input = driver.find_element_by_xpath(path)
    print(search_input.get_name(1))


'''
class Drug:
    def __init__(self, url):
        self.url = url
        self.nazwa_produktu = None
        self.nazwa_powszechnie_stosowana = None
        self.moc = None
        self.substancja_czynna = None
        self.postac_farmaceutyczna = None
        self.podmiot_odpowiedzialny = None
        self.waznosc_pozwolenia = None
        self.link_do_PDF = None
        self.soup = None

    def get_abstract(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, 'lxml')
        dl_data = self.soup.find_all("dd")
        for dlitem in dl_data:
            print(dlitem.string)

        #self.nazwa_produktu = self.soup.find(id="abstract").get_text().lower()  # wybiera text z sekcji Abs1-section

url1 = f'https://pub.rejestrymedyczne.csioz.gov.pl/ProduktSzczegoly.aspx?id=225'

Pierwszy = Drug(url1)
Pierwszy.get_abstract()
print(Pierwszy.soup)

'''
dl_data = soup.find_all("dd") 
for dlitem in dl_data:     
print dlitem.string

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
        self.list_of_article_links = ['https://pubmed.ncbi.nlm.nih.gov' + x.a['href'] for x in content]


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
        self.abstract = soup.find(id="abstract").get_text().lower()  # wybiera text z sekcjii Abs1-section

    def create_set_of_abstract_words(self):
        self.abstract_regex = re.sub(r"[^a-zA-Z]", " ", self.abstract)
        self.set_of_abstract_words = set(self.abstract_regex.split(" "))

    def create_list_of_sets_of_sentence(self):
        self.list_abstract_sentence = self.abstract.split(". ")
        self.list_of_abstract_sentence_sets = [set(re.sub(r"[^a-zA-Z]", " ", x).split(" ")) for x in
                                               self.list_abstract_sentence]

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
'''
