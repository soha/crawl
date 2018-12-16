# -*- coding: utf-8 -*-
import scrapy


class EsolspiderSpider(scrapy.Spider):
    name = 'ESolSpider'
    allowed_domains = ['https://ssl4.eir-parts.net']
    start_urls = ['https://ssl4.eir-parts.net/V4Public/EIR/4420/ja/announcement/announcement_1.xml/']

    def parse(self, response):

        item = MoneyCrawlItem()
        ##response.selector.remove_namespaces() # これをやらないとデータが見えない
        
        item['title'] =response.xpath('//item/title/text()').extract()
        item['link'] =response.xpath('//item/link/text()').extract()
        item['pub_date'] =response.xpath('//item/pubDate/text()').extract()
        
        yield item

