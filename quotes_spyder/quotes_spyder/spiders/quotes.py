import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        '''
        h1_tag = response.xpath('//h1/a/text()').extract()
        tag_list = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        yield {'H1 Tag': h1_tag,
               'Tags' : tag_list}
        '''
        quotes = response.xpath('//*[@class="quote"]')
        quotes_dict = dict()
        index = 0
        for quote in quotes:
            index += 1
            quote_text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            # print(quote_text)
            quote_author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            # print(quote_author)
            quote_tags = quote.xpath('.//*[@class="tag"]/text()').extract()
            # print(quote_tags)
            quote_dict = dict()
            quote_dict['Author'] = quote_author
            quote_dict['Quote'] = quote_text
            quote_dict['Tags'] = quote_tags
            quotes_dict['Quote ' + str(index)] = quote_dict

            yield quotes_dict