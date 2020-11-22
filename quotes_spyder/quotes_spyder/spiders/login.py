import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath('//input[@name="csrf_token"]/@value').extract_first()
        self.log('Your csrf_token: ' + csrf_token)

        yield FormRequest('http://quotes.toscrape.com/login',
                          formdata={'csrf_token': csrf_token,
                                    'username': 'sample',
                                    'password': 'sample'},
                          callback=self.parse_after_login)

    def parse_after_login(self, response):
        # check if log in is successful
        if response.xpath('//a[text()="Logout"]'):
            self.log("Login is successful!")

        # open browser after login
        open_in_browser(response)
