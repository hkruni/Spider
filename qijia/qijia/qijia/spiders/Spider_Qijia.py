#encoding=utf-8
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule

from qijia.items import Qijia_Item
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Qijia(Spider):
    name = 'qijia'
    
    allowed_domain = ['jia.com']
    start_urls = [
        #'http://tuku.jia.com/tags/list_a/'          
                  ]

    prefix = "http://tuku.jia.com/tags/list_a/p"
    
    for i in range(2300,3446):
        url = "http://tuku.jia.com/tags/list_a/p%d"%i
        start_urls.append(url);
     
    for i in start_urls:
        print i        
        
    def parse(self, response):        
        preachs=Selector(response).xpath("//li[@class='masonry-brick']/p/a").xpath('@href').extract()
        for item_url in preachs:
            yield scrapy.Request(item_url, self.parse_item)    
            
        
    def parse_item(self,response):

        
        item = Qijia_Item()
        
        item['site'] = response.url
        item['title'] = Selector(response).xpath("//div[@class='crumb']/i/text()").extract()[0]
        item['key'] = Selector(response).xpath("//meta[@name='keywords']").xpath('@content').extract()[0]

            
        item['tag']=Selector(response).xpath("//p[@class='pic_desp']/span/i/text()").extract()[0]
        url = Selector(response).xpath("//img[@class='lazyload']/@_src").extract()[0]
        item['origin_url'] = url
        item['new_url']=''
        item['mb']=''
        item['pixel']=''
        item['format']=url.split("/")[-1].split('.')[-1]
        return item;
    pass   
        
        
        