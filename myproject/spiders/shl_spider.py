import scrapy
from myproject.items import MyprojectItem
from apify_client import ApifyClient

class ShlSpider(scrapy.Spider):
    name = "shl"
    start_urls = ['https://old.shl.se/statistik/tabell?season=2023&gameType=regular']

    def parse(self, response):
        client = ApifyClient()
        dataset = client.datasets().get_or_create(name='shl-dataset')

        rows = response.xpath('//tr')
        for row in rows:
            item = MyprojectItem()
            item['position'] = row.xpath('td[1]/text()').get()
            item['team'] = row.xpath('td[2]/text()').get()
            item['games_played'] = row.xpath('td[3]/text()').get()
            item['wins'] = row.xpath('td[4]/text()').get()
            item['overtime_wins'] = row.xpath('td[5]/text()').get()
            item['overtime_losses'] = row.xpath('td[6]/text()').get()
            item['losses'] = row.xpath('td[7]/text()').get()
            item['goals_for'] = row.xpath('td[8]/text()').get()
            item['goals_against'] = row.xpath('td[9]/text()').get()
            item['goal_difference'] = row.xpath('td[10]/text()').get()
            item['points'] = row.xpath('td[11]/text()').get()

            dataset.items().put(item)

            yield item