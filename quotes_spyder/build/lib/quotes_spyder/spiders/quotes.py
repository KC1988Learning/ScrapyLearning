from scrapy import Request
from scrapy import Spider
from scrapy.loader import ItemLoader
# from itemloaders.processors import MapCompose, TakeFirst, Join
from quotes_spyder.items import QuotesSpyderItem

def strip_double_quotes(text):
    return text.strip('“').strip('”').replace('‘',"\'").replace('’',"\'")

def encode_UTF8(text):
    return text.encode(encoding='UTF-8')

# class QuotesLoader(ItemLoader):
    # default output processor

    # quote_text_in = MapCompose(str.strip('â€œ'), str.strip('â€'))
    # quote_text_in = MapCompose(str.upper)
    # quote_text_in = MapCompose(encode_UTF8)
    # quote_author_in = MapCompose(encode_UTF8)

class QuotesSpider(Spider):
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
        # quotes_dict = dict()
        index = 0
        for quote in quotes:
            index += 1
            quote_text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            # print(quote_text)
            quote_author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            # print(quote_author)
            quote_tags = quote.xpath('.//*[@class="tag"]/text()').extract()
            # print(quote_tags)
            # quote_dict = dict()
            # quote_dict['Author'] = quote_author
            # quote_dict['Quote'] = quote_text
            # quote_dict['Tags'] = quote_tags
            # quotes_dict['Quote ' + str(index)] = quote_dict

            yield{'text' :quote_text,
                  'author' :quote_author,
                  'tags' :quote_tags}
            # l = ItemLoader(item=QuotesSpyderItem(), response=response)
            # l.add_value('quote_text', quote_text)
            # l.add_value('quote_author', quote_author)
            # l.add_value('quote_tags', quote_tags)
            # yield l.load_item()

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url)