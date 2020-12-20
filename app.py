from Flask import flask, render_template, url_for, request, redirect
from BeautifulSoup.py import LinksGetter, Filter


app = Flask(__name__)

# tu wklejamy clasy i funkcje z baxy dnaych bądź ją na począku importujemy z plki i tlyko wywołujemy
# tu tez wklejamy kod z BeautifulSoup.py bądź imporujemy clasy z pliku i tlyko wywołujemy zeby program wykonał

@app.route('/home', methods=['POST'])
def index():
    if request.method == 'POST':
        first_drug = request.form['content'] # to jest w zawartosc strony
        second_drug = request.form['content']
        disease = request.form['content']

        try:
            object = LinksGetter(searching_words)
            object.get_page_content()
            object.get_list_of_links()
            list_of_objects = [Filter(x) for x in object.list_of_article_links]
            list_of_proper_links = []
            for x in list_of_objects:
                x.get_data_from_page()
            for x in list_of_objects:
                if x.check_abstract() == True:
                    if x.check_abstract_sentences() == True:
                        if x.check_for_no_interaction_words() == True:
                            list_of_proper_links.append(x.url)

            return redirect('/results')

        except:
           return 'Błąd wyszukiwania'

    else:
        return render_template('index.html') #index -. Beata robi frontend

@app.route('/results', methods=['GET'])
def results():
    leyout_apki('formularz_od_Beaty')
    return render_template('list_of_proper_links') #result from BeautifulSoup.py


if __name__ "__main__":
    app.run(debug=True)
