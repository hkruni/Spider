import scrapy

from scrapy.item import Item, Field
class KujialeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Kujiale_Item(Item):
    site = Field()
    title = Field()

    origin_url = Field()
    new_url = Field()
    
    mb = Field()
    pixel = Field()
    size = Field()
    format  = Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    pass