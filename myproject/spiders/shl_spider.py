import scrapy
from myproject.items import MyprojectItem

class ShlSpider(scrapy.Spider):
    name = "shl"
    start_urls = ['https://old.shl.se/statistik/tabell?season=2023&gameType=regular']

    def parse(self, response):
        rows = response.xpath('//table/tbody/tr')
        for row in rows:
            item = MyprojectItem()
            item['position'] = row.xpath('./td[1]/text()').get()
            item['team'] = row.xpath('./td[2]/a/span[1]/text()').get()
            item['games_played'] = row.xpath('./td[3]/text()').get()
            yield item