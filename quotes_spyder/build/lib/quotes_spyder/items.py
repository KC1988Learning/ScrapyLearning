# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuotesSpyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quote_text = scrapy.Field()
    quote_author = scrapy.Field()
    quote_tags = scrapy.Field()

