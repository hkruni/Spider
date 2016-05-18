#encoding=utf-8
import scrapy
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.spiders import Spider
from scrapy.spiders.crawl import CrawlSpider, Rule

from kujiale.items import Kujiale_Item
import string 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Spider_Kujialejia(Spider):

    name = 'kujiale'
    allowed_domain = ['kujiale.com']
    start_urls = []
    params = []
    #a1=['xingudian']
    a1 = ['beiou','xiandai','oushi','zhongshi','meishi','tianyuan','dizhonghai',
          'gongyefeng','dongnanya','hunda','rishi','msxc','jianou','xingudian']
    a2 = ['chufang','keting','weishengjian','woshi','canting','shufang','xuanguan','yangtai','ertongfang','zoulang','chuwujian']
    a3 = ['chuju','yushiju','ctj','shugui','chuang1','shuzhuo','chuwuju','shafa','jiugui','chuanglian','diaodeng','yigui','xiegui','etc']
    #a4 = ['diaoding','tatami','beijingqiang','geduan','kazuo','shouna','piaochuang','ganshifenli','yuedujiao','yimaojian','louti','batai','dsq','yinxingmen']
       
    for i in a1:
        for j in a2:
            for k in a3:
            #for l in a4:
                param = i + '-' + j + '-' + k
        #param = i
                params.append(param)
    
    for i in params:
        for j in range(1,51):
            k = str(j)
            url = 'http://www.kujiale.com/xiaoguotu/%s/%s'%(i,k)
            start_urls.append(url)
    
    
    def parse(self, response):
        #currentPage = string.atoi(response.url.split("/")[-1])
        #prefix = '/'.join(response.url.split("/")[:-1])
    
        #flag = Selector(response).xpath("//h3[@class='n yahei fs20 g3']/text()").extract()
        #if len(flag) == 0:
        preachs=Selector(response).xpath("//ul[@class='clearfix']/li/div[@class='pic']/a/@href").extract();
        if len(preachs)>0:
            for item_url in preachs:
                url1 = 'http://www.kujiale.com' + item_url
                url2 = url1.split('?')[0]
                yield scrapy.Request(url2, self.parse_item)   
 
        
        #    list1 = Selector(response).xpath("//div[@class='page-r']/a/text()").extract()

        #   if len(list1) > 0:
        #        pageNum = string.atoi(list1[-2])#最后一页的编号
        #        if currentPage < pageNum:
        #            nextpage = currentPage + 1
        #            url_next = prefix + '/' + str(nextpage)
        #            yield scrapy.Request(url_next,self.parse) 
    pass

    def parse_item(self,response):

        
        item = Kujiale_Item()
        
        item['site'] = response.url
        item['title'] = Selector(response).xpath("//h1[@class='yahei n ell']/@title").extract()[0]
        url = Selector(response).xpath("//img[@class='gallery loading32']/@data-url").extract()[0]
        item['origin_url'] = url
        item['new_url']=''
        item['mb']=''
        item['size']=''
        item['pixel']=''
        item['format']=url.split("@")[0].split('.')[-1]
        return item;
    pass   
    
    
    
    
    
        