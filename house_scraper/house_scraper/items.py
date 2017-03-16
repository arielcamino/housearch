# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class IdealistaItem(scrapy.Item):
    # define the fields for your item here like:
    id_ = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    size = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    deposit_months = scrapy.Field(output_processor=TakeFirst())
    pictures = scrapy.Field()
    description = scrapy.Field(output_processor=TakeFirst())
    price_m2 = scrapy.Field(output_processor=TakeFirst())
    basic_features = scrapy.Field(output_processor=TakeFirst())
    building_features = scrapy.Field()
    equipment = scrapy.Field()
    street = scrapy.Field(output_processor=TakeFirst())
    neighborhood = scrapy.Field(output_processor=TakeFirst())
    district = scrapy.Field(output_processor=TakeFirst())
    city = scrapy.Field(output_processor=TakeFirst())
    updated = scrapy.Field(output_processor=TakeFirst())
    phone = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
