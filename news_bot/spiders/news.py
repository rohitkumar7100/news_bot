# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['www.indiatoday.in/top-stories']
    start_urls = ['https://www.indiatoday.in/top-stories/']
    
    def parse(self, response):
        # news_headlines=[]
        headlines=response.xpath('//div[@class="detail"]')
        for t in headlines:
            headline=t.xpath(".//h2/a/text()").get()
            yield{
                'HeadLine':headline
            }
