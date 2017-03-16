# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import Request

from house_scraper.items import IdealistaItem
from scrapy.loader import ItemLoader


class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    start_urls = ['https://www.idealista.com/areas/alquiler-viviendas/con-precio-hasta_1400/?shape=%28%28kthvFfv%60W_hC%7DuGdyLuxPmhAgfIcrFsuKwnFihCqkAugKxwEj_A%60x%40uaBdlGl_%40vbA%60gB%7CWi%60F%7CkB_yBfeAmSlAxiEllBzi%40zt%40l~B%7C%60Cj%7B%40d~AngCp%7D%40hCmZ%7ClBc_AnxBgnAj%7CA_Zb%7C%40n~BvwEkn%40npAek%40tcAt%40%3F%7DiChjBw%7CB%7CkHgtD%7BeDiw%40~bCvsB~%7DG_jKneK%29%29']

    def parse(self, response):
        self.domain = 'https://www.idealista.com'
        publications = response.css('.items-container > article > .item')
        for house in publications:
            url = house.css('.item-link::attr(href)').extract_first()
            yield Request(
                url=self.domain + url,
                callback=self.parse_publication)

    def parse_publication(self, response):
        loader = ItemLoader(response=response, item=IdealistaItem())
        loader.add_css('title', 'h1 span::text')
        yield loader.load_item()
