# -*- coding: utf-8 -*-
import scrapy


class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    start_urls = ['https://www.idealista.com/alquiler-viviendas/barcelona-barcelona/con-precio-hasta_900,terraza,publicado_ultimo-mes/']

    def parse(self, response):
        publications = response.css('.items-container > article > .item')
        for house in publications:
            yield {
                'id': int(house.css('::attr(data-adid)').extract_first()),
                'title': house.css('a.item-link::attr(title)').extract_first(),
                'url': house.css('a.item-link::attr(href)').extract_first()}
