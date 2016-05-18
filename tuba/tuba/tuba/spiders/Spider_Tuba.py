#encoding=utf-8
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule

from tuba.items import Tuba_Item
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Tuba(Spider):
    name = 'tuba'
    
    allowed_domain = ['to8to.com']
    start_urls = [
                  
                  ]
    for i in range(200001,400001):
        id = str(i).zfill(6)
        url = "http://m.to8to.com/xiaoguotu/p10%s.html"%id
        start_urls.append(url)
    
        
    def parse(self,response):

        
        item = Tuba_Item()
        
        item['site'] = response.url
        item['title'] = Selector(response).xpath("//div[@id='apphigh']/img/@title").extract()[0]

            
        url = Selector(response).xpath("//div[@id='apphigh']/img/@src").extract()[0]
        item['origin_url'] = url
        item['new_url']=''
        item['mb']=''
        item['pixel']=''
        item['format']=url.split("/")[-1].split('.')[-1]
        return item;
    pass   
        
        
        