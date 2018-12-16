# -*- coding: utf-8 -*-
import scrapy


class EsolspiderSpider(scrapy.Spider):
    name = 'ESolSpider'
    allowed_domains = ['https://ssl4.eir-parts.net/V4Public/EIR/4420/ja/announcement/announcement_1.xml']
    start_urls = ['http://https://ssl4.eir-parts.net/V4Public/EIR/4420/ja/announcement/announcement_1.xml/']

    def parse(self, response):
        pass
