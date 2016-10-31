# -*- coding: utf-8 -*-
import scrapy


class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    start_urls = ['https://www.idealista.com/alquiler-viviendas/barcelona-barcelona/con-precio-hasta_900,terraza,publicado_ultimo-mes/']

    def parse(self, response):
        publications = response.css('article .item')
        for house in publications:
            yield {'title': house.css('a::attr(title)').extract_first()}
