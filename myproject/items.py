# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    position = scrapy.Field()
    team = scrapy.Field()
    games_played = scrapy.Field()
