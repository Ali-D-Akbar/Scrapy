import scrapy


class QuotesSpider(scrapy.Spider):

    """
    scrapy shell 'http://quotes.toscrape.com/page/1/'
    use this command to enter Scrapy Shell and write:
    response.css('title::text').getall()
    to get the title text
    """
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
