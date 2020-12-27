# -*- coding: utf-8 -*-
import scrapy
from pachong5.items import Pachong5Item

class Aijia1Spider(scrapy.Spider):
    name = 'aijia1'
    allowed_domains = ['bj.5i5j.com']
    start_urls = ['https://bj.5i5j.com/ershoufang/n/' + str(x) for x in range(1,6)]

    def parse(self, response):
        xiaoqus = response.xpath('/html/body/div[6]/div[1]/div[2]/ul/li')
        for xiaoqu in xiaoqus:
            item = Pachong5Item()
            item['xiaoqu'] = xiaoqu.xpath('div[2]/h3/a/text()').extract_first()
            item['zongjia'] = xiaoqu.xpath(
            '/html/body/div[6]/div[1]/div[2]/ul/li[6]/div[2]/div[1]/div/p[1]/strong/text()').extract_first()
            yield item