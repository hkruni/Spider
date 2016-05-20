#encoding=utf-8
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule

from fang.items import Fang_Item
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Qijia(Spider):
    name = 'fang'
    
    allowed_domain = ['fang.com']
    start_urls = [
                         
                  ]


    for i in range(1700000,2000000):
        url = 'http://home.fang.com/zhuangxiu/caseinfo%d/'%i
        start_urls.append(url)
        
        
    def parse(self,response):

        


        title = Selector(response).xpath("//div[@class='project_tit']/span/h2/text()").extract()

        if len(title) > 0 :
            item = Fang_Item()
            item['title'] = ''
            item['community'] = ''
            item['budget'] = ''
            item['type'] = ''
            item['houseType'] = ''
            item['square'] = ''
            item['style'] = ''
            item['needs'] = ''
            



            item['site'] = response.url
            item['id'] = response.url.split("/")[-2][8:]
            item['title'] = title[0]
            community = Selector(response).xpath("//a[@id='casexq_B02_15']/text()").extract()
            if len(community) > 0:
                item['community'] = community[0]
            budget = Selector(response).xpath("//a[@id='casexq_B02_17']/text()").extract()
            if len(budget) > 0:
                item['budget'] = budget[0]
            type = Selector(response).xpath("//div[@class='project_info2']/ol/li[2]/span[2]/i/text()").extract()
            if len(type) > 0:
                item['type'] = type[0]
            houseType = Selector(response).xpath("//a[@id='casexq_B02_18']/text()").extract()
            if len(houseType) > 0:
                item['houseType'] = houseType[0]
            square = Selector(response).xpath("//a[@id='casexq_B02_19']/text()").extract()
            if len(square) >0:
                item['square'] = square[0]
            style = Selector(response).xpath("//a[@id='casexq_B02_20']/text()").extract()
            if len(style) > 0:
                item['style'] = style[0]
            need = Selector(response).xpath("//div[@class='tc_pinfo_cont']/ol/li[3]/p/text()").extract()
            if len(need) > 0:
                item['needs'] = need[0].replace(' ','')
            
            
            item['image_urls'] = Selector(response).xpath("//div[@class='photo_cont']/ul/a/img/@src").extract()
            item['imageDes'] = Selector(response).xpath("//div[@class='photo_cont']/ol/dd/text()").extract()
            item['new_url'] = []
            #photo = Selector(response).xpath("//div[@class='photo_cont']").extract()
            #if len(photo) > 0:
            return item
    pass
        