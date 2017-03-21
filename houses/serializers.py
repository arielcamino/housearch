from rest_framework import serializers
from houses.models import (House, HouseImage)


class HouseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseImage
        fields = (
            'order',
            'url',
            'url_small'
        )


class HouseSerializer(serializers.ModelSerializer):
    houseimage_set = HouseImageSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = (
            'external_id',
            'url',
            'title',
            'description',
            'updated_date',
            'updated_date_string',
            'advertiser_name',
            'advertiser_phone',
            'city',
            'district',
            'neighborhood',
            'street',
            'basic_features',
            'building_features',
            'equipment',
            'price_m2',
            'size',
            'price',
            'deposit_months',
            'houseimage_set'
        )
