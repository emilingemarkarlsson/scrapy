import scrapy
from myproject.items import MyprojectItem
from apify_client import ApifyClient

class ShlSpider(scrapy.Spider):
    name = "shl"
    start_urls = ['https://old.shl.se/statistik/tabell?season=2023&gameType=regular']

    def __init__(self, *args, **kwargs):
        super(ShlSpider, self).__init__(*args, **kwargs)
        self.client = ApifyClient()
        # Create or get the default dataset associated with this actor run
        self.dataset = self.client.datasets().get_or_create(name='default')
    
    def parse(self, response):
        rows = response.xpath('//tr')
        items_to_store = []
        
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
            items_to_store.append(item)
        
        # Store items in the Apify dataset
        self.dataset.items().put_multiple(items_to_store)

        for item in items_to_store:
            yield item