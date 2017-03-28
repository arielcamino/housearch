from __future__ import unicode_literals

from django.db import models


class House(models.Model):
    external_id = models.CharField(
        max_length=256,
        db_index=True)
    url = models.URLField(null=True, blank=True, db_index=True)
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    updated_date_string = models.CharField(max_length=256, null=True,
                                           blank=True)
    advertiser_name = models.CharField(max_length=256, null=True, blank=True)
    advertiser_phone = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    district = models.CharField(max_length=256, null=True, blank=True)
    neighborhood = models.CharField(max_length=256, null=True, blank=True)
    street = models.CharField(max_length=256, null=True, blank=True)
    basic_features = models.TextField(null=True, blank=True)
    building_features = models.TextField(null=True, blank=True)
    equipment = models.TextField(null=True, blank=True)
    price_m2 = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                   blank=True)
    size = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                               blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                blank=True)
    deposit_months = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class HouseImage(models.Model):

    house = models.ForeignKey(House)
    order = models.IntegerField(null=True, blank=True)
    url = models.URLField(max_length=512, null=True, blank=True)
    url_small = models.URLField(max_length=512, null=True, blank=True)

    def __unicode__(self):
        return self.house.title
