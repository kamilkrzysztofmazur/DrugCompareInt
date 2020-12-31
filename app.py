from flask import Flask, url_for, redirect, request
from flask import render_template
from scraping import Filter, LinksGetter

app = Flask(__name__)

no_interaction_set = {
'nointeraction'
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
# tu wklejamy clasy i funkcje z baxy dnaych bądź ją na począku importujemy z plki i tlyko wywołujemy
# tu tez wklejamy kod z BeautifulSoup.py bądź imporujemy clasy z pliku i tlyko wywołujemy zeby program wykonał

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        first_drug = request.form['content1'] # wskazac miejsca z formularza html od Beaty
        second_drug = request.form['content2'] # wskazac miejsca z formularza html od Beaty
        disease = request.form['content3'] # wskazac miejsca z formularza html od Beaty
        searching_words = f"{first_drug}+{second_drug}+{disease}"
        set_of_serch_items = {first_drug, second_drug, disease}
        try:
            object = LinksGetter(searching_words)
            object.get_page_content()
            object.get_list_of_links()
            list_of_objects = [Filter(x) for x in object.list_of_article_links]
            list_of_proper_links = []
            list_of_proper_links1 = []
            list_of_proper_links2 = []
            for x in list_of_objects:
                x.set_of_search_items = set_of_serch_items
                x.no_interaction_set = no_interaction_set
                x.get_data_from_page()
            for x in list_of_objects:
                if x.check_abstract() == True:
                    list_of_proper_links.append(x.url)
                    if x.check_abstract_sentences() == True:
                        list_of_proper_links1.append(x.url)
                        if x.check_for_no_interaction_words() == True:
                            list_of_proper_links2.append(x.url)
            if not list_of_proper_links:
                comment = "Nie znaleziono artykułów odpowiadających podanym kryteriom"
            else:
                comment = "Poniżej artykuły odpowiadające kryteriom wyszukiwania"

            return render_template('result.html', list=list_of_proper_links,  list1=list_of_proper_links1,  list2=list_of_proper_links2, comment=comment)  #redirect('/results')

        except:
           return 'Błąd wyszukiwania'

    else:
        return render_template('home.html') 

if __name__ == '__main__':
    app.run(debug=True)
