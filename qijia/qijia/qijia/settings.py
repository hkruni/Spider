# -*- coding: utf-8 -*-

# Scrapy settings for qijia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qijia'

SPIDER_MODULES = ['qijia.spiders']
NEWSPIDER_MODULE = 'qijia.spiders'


ITEM_PIPELINES = {
    'qijia.pipelines.QijiaImagesPipe' : 1,
    'qijia.pipelines.InsertTitlePipe' : 5
}


MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'spider_db1'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
MYSQL_PORT = 3308


IMAGES_STORE = r'/xgt/qijia/'
IMAGES_EXPIRES = 10
