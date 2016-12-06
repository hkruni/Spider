# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FootballItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    liansai = scrapy.Field()
    zhu = scrapy.Field()
    ke = scrapy.Field()
    bifen_half = scrapy.Field()
    bifen_all = scrapy.Field()
    rang = scrapy.Field()
    sheng1 = scrapy.Field() 
    ping1 = scrapy.Field()
    fu1 = scrapy.Field()
    sheng2 = scrapy.Field() 
    ping2 = scrapy.Field()
    fu2 = scrapy.Field()
    
    last = scrapy.Field()
    rang_last = scrapy.Field()
    pass
