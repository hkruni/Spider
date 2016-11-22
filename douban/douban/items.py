# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field


class DoubanBookItem(scrapy.Item):
    name = scrapy.Field()            # 书名
    price = scrapy.Field()           # 价格
    edition_year = scrapy.Field()    # 出版年份
    publisher = scrapy.Field()       # 出版社
    ratings = scrapy.Field()         # 评分
