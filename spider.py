
import scrapy
Skip to content
Pull requests
Issues
Marketplace
Explore


@kamilkrzysztofmazur
kamilkrzysztofmazur /
Drug_Interactions_Comparison

1
0

    0

Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights

    Settings

Drug_Interactions_Comparison/SryperSpider1.py /


@wojciechqj6
wojciechqj6 Utworzenie plików
Latest commit 8dfc063 20 days ago
History
1 contributor
37 lines(28 sloc) 1.01 KB


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


"""""""""
class MyS"pider(scrapy.Spider):
    name = 'myspider'
    def start_requests(self):
        return [scrapy.FormRequest("http://www.example.com/login",
                                   formdata={'user': 'john', 'pass': 'secret'},
                                   callback=self.logged_in)]
    def logged_in(self, response):
        # here you would extract links to follow and return Requests for
        # each of them, with another callback
        pass

""""""""

    © 2020 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About
