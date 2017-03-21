from django.contrib import admin
from houses.models import (House, HouseImage)


class HouseImageInline(admin.StackedInline):
    model = HouseImage
    extra = 0


class HouseAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'basic_features', 'equipment']
    list_display = ['title', 'price', 'size', 'price_m2', 'deposit_months']

    inlines = [HouseImageInline]

admin.site.register(House, HouseAdmin)
admin.site.register(HouseImage)
