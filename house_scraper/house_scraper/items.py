# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import TakeFirst, MapCompose, Compose


class IdealistaItem(scrapy.Item):
    # define the fields for your item here like:
    external_id = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    size = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    deposit_months = scrapy.Field(output_processor=Compose(
                lambda v: v[0],
                lambda v: re.findall('Fianza de (\d+)', v)[0])
                )
    pictures = scrapy.Field(output_processor=MapCompose(
                lambda v: v.replace(',WEB_DETAIL', '')))
    mini_pictures = scrapy.Field(output_processor=MapCompose(
                lambda v: v.replace(',WEB_DETAIL', ''),
                lambda v: v.replace('WEB_DETAIL', 'WEB_LISTING')
                ))
    description = scrapy.Field(output_processor=TakeFirst())
    price_m2 = scrapy.Field(output_processor=Compose(
                lambda v: v[0],
                lambda v: re.findall('\d+\,*\d*', v)[0],
                lambda v: v.replace(',', '.')
                ))
    basic_features = scrapy.Field()
    building_features = scrapy.Field()
    equipment = scrapy.Field()
    street = scrapy.Field(output_processor=TakeFirst())
    neighborhood = scrapy.Field(output_processor=TakeFirst())
    district = scrapy.Field(output_processor=TakeFirst())
    city = scrapy.Field(output_processor=TakeFirst())
    updated = scrapy.Field(output_processor=TakeFirst())
    advertiser_phone = scrapy.Field(output_processor=TakeFirst())
    advertiser_name = scrapy.Field(output_processor=TakeFirst())
