# -*- coding: utf-8 -*-
from urllib import urlopen



initial_url = 'https://www.zhihu.com/people/rooney-hk/activities'


response = urlopen(initial_url).read().decode('utf-8') 
print response
