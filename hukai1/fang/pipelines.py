# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import os  
from os.path import join, getsize
import string
import time
import uuid

import MySQLdb.cursors
from PIL import Image
from scrapy import log
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi

from fang import settings


class FangPipeline(object):
    def process_item(self, item, spider):
        return item


class FangImagesPipe(ImagesPipeline):
    def get_media_requests(self, item, info):
        for i in range(0,len(item['image_urls'])):
            id = str(i+1)
            yield scrapy.Request(item['image_urls'][i],meta={'name':item['id']+'_'+id})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]

        if len(image_paths)>0:
            for i in image_paths:
                new_url = settings.IMAGES_STORE + i
                item['new_url'].append(new_url)

        return item
    
    def file_path(self, request, response=None, info=None):
        image_name = request.meta.get('name')
        image_guid = request.url.split('/')[-1]
        hour = time.strftime("%H")
        suffix = image_guid.split('.')[-1]
        hour = time.strftime("%H")

        imagePath1 = str(time.time()).replace('.','1') + '.' + suffix
        newimage = image_name + '.' + suffix
        return '%s/%s' % (hour,newimage)


class InsertTitlePipe(object):
    def __init__(self, dbargs):
        self.dbargs = dbargs
    
    def open_spider(self,spider):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **(self.dbargs))
        
    def close_spider(self,spider):
        self.dbpool.close()
        
    @classmethod
    def from_crawler(cls,crawler):
        settings = crawler.settings
        dbargs = dict(
                      host=settings['MYSQL_HOST'],
                      db=settings['MYSQL_DBNAME'],
                      user=settings['MYSQL_USER'],
                      passwd=settings['MYSQL_PASSWD'],
                      port=settings['MYSQL_PORT'],
                      charset='utf8',
                      cursorclass = MySQLdb.cursors.DictCursor,
                      use_unicode= True,
                      )
        return cls(dbargs)
        
    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insertTitleSql,item)
        #self.dbpool.runInteraction(self.insertImageSql,item)
        return item
    
    def insertTitleSql(self, tx,item):

        sql = "insert into fang"
        sql_insert = sql + " (id,site,title,community,budget,type,houseType,square,style,needs) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        tx.execute(sql_insert,(item['id'],item['site'],item['title'],item['community'],
                               item['budget'],item['type'],item['houseType'],item['square'],
                               item['style'],item['needs']))

        #sql2 = "insert into image(caseid,id,des,origin_url,new_url,mb,pixel,size,format) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #aa = item.images
        #for i in aa:
        #    tx.execute(sql2,(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
        
        sql2 = "insert into image(caseid,id,des,origin_url,new_url,mb,pixel,size,format) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        aa = item['image_urls']
        bb = item['imageDes']
        cc = item['new_url']
        new_url=''
        mb=''
        pixel=''
        size=''
        format=''
        for i in range(0,len(aa)):
            id = str(i+1)
            im = Image.open(cc[i])
            if im :
				new_url=cc[i]
				mb = str(getsize(new_url) /1024) + 'KB'
				width = im.size[0]
				height = im.size[1]
				size = str(width) + 'x' + str(height)
				pixel = width * height
				format = cc[i].split(".")[-1]

            
            tx.execute(sql2,(item['id'],item['id']+'_'+id,bb[i],aa[i],new_url,mb,pixel,size,format))
