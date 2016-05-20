# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class FangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Fang_Item(Item):
    id = Field()
    site = Field()
    title = Field()
    community = Field()
    budget = Field()
    type = Field()
    houseType = Field()
    square = Field()
    style = Field()
    needs = Field()
    image_urls = Field()
    new_url = Field()
    images = Field()
    imageDes = Field()
    pass


