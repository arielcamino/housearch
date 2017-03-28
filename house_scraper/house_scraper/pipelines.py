# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import django
django.setup()

from houses.models import House, HouseImage


class SaveHousesPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'idealista':
            try:
                house = House.objects.get(external_id=item['external_id'])
            except House.DoesNotExist:
                house = House(external_id=item['external_id'])

            house.title = item['title']
            house.url = item.get('url')
            house.title = item.get('title')
            if item.get('description'):
                house.description = ' '.join(item.get('description'))
            house.updated_date = item.get('updated_date')
            house.updated_date_string = item.get('updated')
            house.advertiser_name = item.get('advertiser_name')
            house.advertiser_phone = item.get('advertiser_phone')
            house.city = item.get('city')
            house.district = item.get('district')
            house.neighborhood = item.get('neighborhood')
            house.street = item.get('street')
            house.price_m2 = item.get('price_m2')
            house.size = item.get('size')
            house.price = item.get('price')
            house.deposit_months = item.get('deposit_months')
            house.rooms = item.get('rooms')

            if item.get('basic_features'):
                house.basic_features = ','.join(item.get('basic_features'))

            if item.get('building_features'):
                house.building_features = ','.join(item.get('building_features'
                                                            ))

            if item.get('equipment'):
                house.equipment = ','.join(item.get('equipment'))

            house.save()
            if(item.get('pictures')):
                house.houseimage_set.all().delete()
                for i in xrange(len(item['pictures'])):
                    houseimage = HouseImage()
                    houseimage.house = house
                    houseimage.order = i
                    houseimage.url = item['pictures'][i]
                    houseimage.url_small = item['mini_pictures'][i]

                    houseimage.save()

        return item
