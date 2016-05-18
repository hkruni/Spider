#encoding=utf-8
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule

from aiuw.items import Aiuw_Item
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Qijia(Spider):
    name = 'aiuw'
    
    allowed_domain = ['aiuw.com']
    start_urls = [
                  
                  ]
    for i in range(0,999999):
        id = str(i).zfill(6)
        url = "http://www.aiuw.com/albums/g-%s/"%id
        start_urls.append(url)
     
     
        
    def parse(self,response):

        
        item = Aiuw_Item()
        
        item['site'] = response.url
        title = Selector(response).xpath("//span[@id='imgExplain']/text()").extract()
        if len(title) > 0 :
            item['title'] = title[0]
        else :
            return
        
        tags = Selector(response).xpath("//div[@class='tag']/a/text()").extract()
        if len(tags) > 0 :
            item['tag'] = ','.join(tags)
        else :
            item['tag'] = ''
            
        url = Selector(response).xpath("//div[@class='img_boxlist up userSelectNone']/img/@src").extract()[0]
        item['origin_url'] = url.replace("zip@q80", "zip@w400")
        item['new_url']=''
        item['mb']=''
        item['pixel']=''
        item['format']=url.split("/")[-1].split('.')[-1]
        return item;
    pass    
        
        
        