# -*- coding: utf-8 -*-
from _csv import writer
import codecs
import csv

import xlwt


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class FootballPipeline(object):
    def __init__(self):
        
        self.i = 0
        self.file = xlwt.Workbook()
        self.sheet = self.file.add_sheet('sheet')
        self.sheet.write(self.i,0,u'比赛时间')
        self.sheet.write(self.i,1,u'赛事编号')
        self.sheet.write(self.i,2,u'联赛')
        self.sheet.write(self.i,3,u'比分')
        self.sheet.write(self.i,4,u'')
        self.sheet.write(self.i,5,u'')
        self.sheet.write(self.i,6,u'')
        self.sheet.write(self.i,7,u'让球')
        self.sheet.write(self.i,8,u'胜')
        self.sheet.write(self.i,9,u'平')
        self.sheet.write(self.i,10,u'负')
        
        self.style = xlwt.XFStyle()
        
        self.font0 = xlwt.Font()
        self.font0.colour_index = 2
        self.font0.bold = True
        self.style.font = self.font0

        
        pass
    
    def open_spider(self,spider):
        
        pass
    
    def close_spider(self,spider):
        self.file.save("D://result.xls")
    
    def process_item(self, item, spider):
        
        bisai_result = item['zhu'] + ' (' + item['bifen_half'] + ') ' + item['bifen_all'] + item['ke']
        self.i += 1
        
        self.sheet.write(self.i,0,item['date'])
        self.sheet.write(self.i,1,item['bianhao'])
        self.sheet.write(self.i,2,item['liansai'])
        self.sheet.write(self.i,3,bisai_result)
        if item['last'] == '胜':
            self.sheet.write(self.i,4,item['sheng2'],self.style)
        else:
            self.sheet.write(self.i,4,item['sheng2'])
            
        if item['last'] == '平':
            self.sheet.write(self.i,5,item['ping2'],self.style)
        else:
            self.sheet.write(self.i,5,item['ping2'])
        if item['last'] == '负':
            self.sheet.write(self.i,6,item['fu2'],self.style)
        else:
            self.sheet.write(self.i,6,item['fu2'])
        
    
        self.sheet.write(self.i,7,item['rang'])
        if item['rang_last'] == '胜':
            self.sheet.write(self.i,8,item['sheng1'],self.style)
        else:
            self.sheet.write(self.i,8,item['sheng1'])
            
        if item['rang_last'] == '平':
            self.sheet.write(self.i,9,item['ping1'],self.style)
        else:
            self.sheet.write(self.i,9,item['ping1'])
        if item['rang_last'] == '负':
            self.sheet.write(self.i,10,item['fu1'],self.style)
        else:
            self.sheet.write(self.i,10,item['fu1'])
        
        return item
