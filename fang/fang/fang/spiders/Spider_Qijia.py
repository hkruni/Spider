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
    params = []
    a1 = ['keting','chufang','woshi','weishengjian']
    #a1 = ['keting','chufang','woshi','weishengjian','xuanguan','canting','yangtai','ertongfang','yimaojian','shufang']
    a2 = ['xiandai','jianou','jianyue','zhongshi','oushi','tianyuan','dizhonghai','hunda','meishi','rihan','dongnanya','gudian']
    a3 = ['beijqiang','piaochuang','zoulang','diaoding','louti','chugui','yigui','chuang','dianshigui','shafa','chuanglian',
          'geduan','zuhegui','chuwugui','shugui','batai','xiegui','chaji','tatami','zhaopianqiang',
          'bizhi','pingfeng','yingerchuang','dengju','canzhuo','yugang','chuangtougui','jiugui','shuzhuangtai','shujia']

    for i in a1:
        for j in a2:
            for k in a3:
                param = [i,j,k]
                params.append(param)
      
    for index in params:
        for i in range(1,101):
            url = 'http://home.fang.com/album/lanmu/?sortid=11&a1=%s&a2=%s&a3=%s&page=%d'%(index[0],index[1],index[2],i)
            start_urls .append(url)
    
        
    def parse(self, response):
        
        preachs=Selector(response).xpath("//div[@class='photo_list']/ul/li/ol/span/a/@href").extract();
        if len(preachs) > 1 :
            for item_url in preachs:
                yield scrapy.Request(item_url, self.parse_item)    
            

        
    def parse_item(self,response):

        
        item = Fang_Item()
        
        item['site'] = response.url
        item['title'] = Selector(response).xpath("//div[@class='info']/h1/text()").extract()[0]
        item['shortDescription'] = ''
        try:
            short_des = "".join(Selector(response).xpath("//div[@class='info']/p/text()").extract())
            item['shortDescription'] = short_des.strip()
            
        except Exception,e:
            print e
            
        item['category']=''
        item['style']=''
        item['tag']=''
        
        category = Selector(response).xpath("//div[@class='info']/ul/li[1]/a/text()").extract()
        if len(category)>0:
            item['category']=category[0]
            
        style = Selector(response).xpath("//div[@class='info']/ul/li[2]/a/text()").extract()
        if len(style)>0:
            item['style']=style[0]
        
        tags =Selector(response).xpath("//div[@class='tag']/ul/a/text()").extract()
        if len(tags) > 0:
            item['tag'] = ','.join(tags);
        url = Selector(response).xpath("//img[@id='LeftImg']/@src").extract()[0]
        item['origin_url'] = url
        item['new_url']=''
        item['mb']=''
        item['pixel']=''
        item['format']=url.split("/")[-1].split('.')[-1]
        return item;
    pass   
        
        
        