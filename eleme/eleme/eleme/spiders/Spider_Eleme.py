import json
import string 
import sys

from eleme.items import ElemeItem
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule


reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Eleme(Spider):
    name = 'eleme'
    
    start_urls = [
                        
                  ]
    initial_url = 'https://www.ele.me'
    
    for i in range(0,100):
        id = i * 24
        iUrl = 'https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wx4eq7kf7f4&latitude=39.96454&limit=24&longitude=116.29697&offset=' + str(id)
        start_urls.append(iUrl)
    
        
    def parse(self, response):
        jsonObj = json.loads(response.body_as_unicode())
        for j in jsonObj:
            item = ElemeItem()
            item['name'] = j['name']
            item['address'] =  j['address'] 
            item['recent_order_num'] =  j['recent_order_num']
            item['rating'] =  j['rating']
            item['url'] = 'https://www.ele.me/shop/' + str(j['id'])
            imageCode = j['image_path']
            item['imageUrl'] = 'http://fuss10.elemecdn.com/' + imageCode[0] + '/' + imageCode[1:3] + '/' +imageCode[3:] + '.jpeg?imageMogr2/thumbnail/70x70/format/webp/quality/85'
            yield item
            
        

    
        
        