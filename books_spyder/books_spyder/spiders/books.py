# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
from time import sleep

from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException

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
        # enter each book link on the first page, parse and scrape
        self.driver = webdriver.Chrome(r"C:\Users\KC Cheng\Documents\chromedriver.exe")
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse_book)

        # Use Selenium to go to next page
        while True:
            try:
                # next_page is the web element containing the text "next"
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')

                # sleep for 3 s in case error arises in the request
                # while Selenium tries to click the next page again
                sleep(3);
                self.log("Sleeping for 3 seconds.")

                # click on the next page button
                next_page.click()

               # once the new page is accessed, select the page source again
                sel = Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                for book in books:
                    url = 'http://books.toscrape.com/catalogue/' + book
                    yield Request(url, callback=self.parse_book)

            # Break the loop when reaching the last page
            except NoSuchElementException:
                self.log.info("No more pages to load.")
                self.driver.quit() # quite the drive instance
                break

    def parse_book(self, response):
        pass