# -*- coding: utf-8 -*-

import scrapy

from Photo.items import PhotoItem

from scrapy import Spider

from scrapy import Selector

from scrapy.http import Request

class imageSpider(Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = [
        "https://car.autohome.com.cn/jingxuan/list-0-p1.html",
    ]
    def parse(self, response):
        item = PhotoItem()
        sel = Selector(response)
        item['image_urls'] = sel.xpath('//ul[@class="content"]/li/a/img/@src').extract()

        print item['image_urls'], '..image_urls..'
        yield item

        # 翻页
        new_urls = response.xpath('//div[@class="pageindex"]/a[9]/@href').extract_first()

        new_url = "https://car.autohome.com.cn" + new_urls

        print new_url, '..new_url...'
        if new_url:

           yield Request(new_url, callback=self.parse)