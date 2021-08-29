#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 18:26:38 2017

@author: inoueshinichi
"""

import json
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/koki0702/introducing-python/master/dummy_api/youTube_top_rated.json"

response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)

for video in data['feed']['entry'][0:6]:
    print (video['title']['$t'])
    
    