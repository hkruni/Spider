#encoding=utf-8
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule

from shejiben.items import Shejiben_Item
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Tuba(Spider):
    name = 'shejiben'
    
    allowed_domain = ['shejiben.com']
    start_urls = [
                  
                  ]
    for i in range(1015226,1300001):
        url = "http://www.shejiben.com/works/%d.html"%i
        start_urls.append(url)
    
        
    def parse(self,response):

        
        item = Shejiben_Item()
        
        item['site'] = response.url
        title = Selector(response).xpath("//div[@class='pageTag']/a/text()").extract();
        if len(title) == 3 :
            item['title'] = title[-1]
        else :
            return 

            
        url = Selector(response).xpath("//li[@class='nowPic']/img/@src").extract()[0]
        item['origin_url'] = url
        item['new_url']=''
        item['mb']=''
        item['size']=''
        item['pixel']=''
        item['format']=url.split("/")[-1].split('.')[-1]
        return item;
    pass   
        
        
        