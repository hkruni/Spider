#encoding=utf-8
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule

from meilele.items import Meilele_Item
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Qijia(Spider):
    name = 'meilele'
    
    allowed_domain = ['meilele.com']
    start_urls = [
                  
                  ]
    for i in range(1850000,1999999):
        #id = str(i).zfill(6)
        url = "http://zx.meilele.com/albums/p-%d/"%i
        start_urls.append(url)
     
     
        
    def parse(self,response):

        
        item = Meilele_Item()
        
        item['site'] = response.url
        title = Selector(response).xpath("//span[@id='jsImgName']/text()").extract()
        if len(title) > 0 :
            item['title'] = title[0]
        else :
            return
        
        tags = Selector(response).xpath("//div[@class='content']/a/text()").extract();
        if len(tags) > 0 :
            item['tag'] = ','.join(tags)
        else :
            item['tag'] = ''
            
        url = Selector(response).xpath("//div[@id='jsGalleryStageIn']/img/@src").extract()[0]
        item['origin_url'] = url
        item['new_url']=''
        item['mb']=''
        item['pixel']=''
        item['format']=url.split("/")[-1].split('.')[-1]
        return item;
    pass    
        
        
        