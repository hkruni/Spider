#encoding=utf-8
import string 
import sys

from football.items import FootballItem
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule


reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_football(Spider):
    name = 'football'
    
    allowed_domain = ['info.sporttery.cn']
    url = 'http://info.sporttery.cn/football/match_result.php?search_league=0&start_date=2013-06-04&end_date=2013-09-30&dan=&page='
    #url = 'http://info.sporttery.cn/football/match_result.php?search_league=0&page='
    start_urls = [
                  ]
    
    rootUrl = 'http://info.sporttery.cn/football/'
    
    for i in range(1,200):
        url1 = url + str(i)
        start_urls.append(url1)
    
    def parse(self, response):
        
        preachs=Selector(response).xpath("//div[@class='match_list']/table/tr");
        for a in preachs:
            info = a.xpath(".//td[8]/a/text()").extract()
            if len(info) > 0 and info[0] == '详细':
                item = FootballItem()  
                item['date'] = a.xpath(".//td[1]/text()").extract()[0] #日期
                item['bianhao'] = a.xpath(".//td[2]/text()").extract()[0] #日期
                item['bifen_half'] = a.xpath(".//td[5]/span/text()").extract()[0] #上半场比分
                item['bifen_all'] = a.xpath(".//td[6]/span/text()").extract()[0] #下半场比分
                last = item['bifen_all']
                if int(last.split(':')[0]) > int(last.split(':')[1]):
                    item['last'] = '胜'
                if int(last.split(':')[0]) == int(last.split(':')[1]):
                    item['last'] = '平'
                if int(last.split(':')[0]) < int(last.split(':')[1]):
                    item['last'] = '负'
                infoUrl = self.rootUrl + a.xpath(".//td[8]/a/@href").extract()[0]
                yield scrapy.Request(url=infoUrl, meta={'item': item},  callback=self.parse_item)
            

        
    def parse_item(self,response):
        item = response.meta['item']
        liansai = Selector(response).xpath("//div[@class='CenterTit']/text()").extract()[0]
        
        item['liansai'] = liansai.split(' ')[1]
        item['zhu'] = Selector(response).xpath("//span[@class='HomeName']/text()").extract()[0]
        item['ke'] = Selector(response).xpath("//span[@class='HomeName']/text()").extract()[1]
        
        
        #item['last'] =  Selector(response).xpath("//table[@class='date6 jf'][1]/tr[@class='Tr3 Tr_normal'][2]/td[2]/text()").extract()[0]
        item['rang_last'] =  Selector(response).xpath("//table[@class='date6 jf'][1]/tr[@class='Tr3 Tr_normal'][2]/td[4]/text()").extract()[0]
        
        item['rang'] = Selector(response).xpath("//table[@class='date6 jf'][2]/tr[@class='Tr3 Tr_normal'][1]/td[2]/text()").extract()[0]
        item['sheng1'] = Selector(response).xpath("//table[@class='date6 jf'][2]/tr[@class='Tr3 Tr_normal'][1]/td[3]/text()").extract()[0]
        item['ping1'] = Selector(response).xpath("//table[@class='date6 jf'][2]/tr[@class='Tr3 Tr_normal'][1]/td[4]/text()").extract()[0]
        item['fu1'] = Selector(response).xpath("//table[@class='date6 jf'][2]/tr[@class='Tr3 Tr_normal'][1]/td[5]/text()").extract()[0]
        if Selector(response).xpath("//table[@class='date6 jf'][3]/tr[@class='Tr3 Tr_normal'][1]/td[2]/text()"):
            
            item['sheng2'] = Selector(response).xpath("//table[@class='date6 jf'][3]/tr[@class='Tr3 Tr_normal'][1]/td[2]/text()").extract()[0]
            item['ping2'] = Selector(response).xpath("//table[@class='date6 jf'][3]/tr[@class='Tr3 Tr_normal'][1]/td[3]/text()").extract()[0]
            item['fu2'] = Selector(response).xpath("//table[@class='date6 jf'][3]/tr[@class='Tr3 Tr_normal'][1]/td[4]/text()").extract()[0]
        else:
            item['sheng2'] = u'无数据'
            item['ping2'] = u'无数据'
            item['fu2'] = u'无数据'
        return item
        
        
        