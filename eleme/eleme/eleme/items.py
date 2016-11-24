# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ElemeItem(scrapy.Item):
    name = Field()
    address = Field()
    recent_order_num = Field()
    rating = Field()
    url = Field()
    imageUrl = Field()
    #用于图片下载使用
    image_urls = scrapy.Field()
    images = scrapy.Field()
    pass

