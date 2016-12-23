# -*- coding: utf-8 -*-
'''


@author: Administrator
'''
import json
from urllib2 import urlopen


initial_url = 'https://mainsite-restapi.ele.me/shopping/restaurants?extras%5B%5D=activities&geohash=wx4eq7kf7f4&latitude=39.96454&limit=24&longitude=116.29697&offset='

url = initial_url + '0'

responseJson = urlopen(url).read().decode('utf-8') 
jsonObj = json.loads(responseJson)

for j in jsonObj:
    print j['name']
    print j['address'] 
    print j['recent_order_num']
    print j['rating']
    print 'https://www.ele.me/shop/' + str(j['id'])
    
    imageCode = j['image_path']
    
    imageurl = 'http://fuss10.elemecdn.com/' + imageCode[0] + '/' + imageCode[1:3] + '/' +imageCode[3:] + '.jpeg?imageMogr2/thumbnail/70x70/format/webp/quality/85'
    
    print imageurl
    
    
    print '-----------------------------'