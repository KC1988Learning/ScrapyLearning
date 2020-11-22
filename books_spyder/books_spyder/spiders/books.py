# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request

class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/']

    # rules = Rule(LinkExtractor(deny_domains=('google.com')),
    #               callback='parse_page',
    #               follow=False)

    # rules = (Rule(LinkExtractor(allow=('music')),
    #              callback='parse_page',
    #              follow=False),)
    #
    # def parse_page(self, response):
    #     yield {'URL': response.url}

    def start_requests(self):
        self.driver = webdriver.Chrome(r"C:\Users\KC Cheng\Documents\chromedriver.exe")
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)

    def parse_book(self, response):
        pass