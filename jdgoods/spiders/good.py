# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
# from jdgoods.items import JdgoodsItem
from lxml import etree
from scrapy.http import Request


class GoodSpider(scrapy.Spider):
    name = 'good'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def start_requests(self):
        ua = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        ]
        catAll = []
        fh = open('F:/python_practice/scrapy练习/jdgoods/jdgoods/spiders/demo.md', 'r', encoding='utf-8')
        # request1 = urllib.request.Request("https://book.jd.com/")
        # request1.add_header("User-Agent", random.choice(ua))
        # allPdData = urllib.request.urlopen(request1).read().decode("utf-8", "ignore")
        pat1 = '(https:..channel.jd.com.*?.html)'
        # allPd = re.compile(pat1).findall(fh)
        # print(allPd)
        for i in fh:
            thisPd = re.compile(pat1).findall(i)
            print(thisPd)
            if len(thisPd) != 0:
                catAll.append(thisPd[0])


    def parse(self, response):
        pass
