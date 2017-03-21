# -*- coding: utf-8 -*-
import scrapy
import logging

from scrapy.http import Request

from house_scraper.items import IdealistaItem
from scrapy.loader import ItemLoader


class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    start_urls = ['https://www.idealista.com/areas/alquiler-viviendas/con-precio-hasta_1400/?shape=%28%28kthvFfv%60W_hC%7DuGdyLuxPmhAgfIcrFsuKwnFihCqkAugKxwEj_A%60x%40uaBdlGl_%40vbA%60gB%7CWi%60F%7CkB_yBfeAmSlAxiEllBzi%40zt%40l~B%7C%60Cj%7B%40d~AngCp%7D%40hCmZ%7ClBc_AnxBgnAj%7CA_Zb%7C%40n~BvwEkn%40npAek%40tcAt%40%3F%7DiChjBw%7CB%7CkHgtD%7BeDiw%40~bCvsB~%7DG_jKneK%29%29']

    def parse(self, response):
        last_page = int(response.css('.pagination li a::text').extract()[-1])
        for page in xrange(1, last_page+1):
        #for page in xrange(1, 2):
            url = 'https://www.idealista.com/areas/alquiler-viviendas/con-precio-hasta_1400/pagina-'+str(page)+'?shape=%28%28kthvFfv%60W_hC%7DuGdyLuxPmhAgfIcrFsuKwnFihCqkAugKxwEj_A%60x%40uaBdlGl_%40vbA%60gB%7CWi%60F%7CkB_yBfeAmSlAxiEllBzi%40zt%40l~B%7C%60Cj%7B%40d~AngCp%7D%40hCmZ%7ClBc_AnxBgnAj%7CA_Zb%7C%40n~BvwEkn%40npAek%40tcAt%40%3F%7DiChjBw%7CB%7CkHgtD%7BeDiw%40~bCvsB~%7DG_jKneK%29%29'
            yield Request(
                url=url,
                callback=self.parse_page)

    def parse_page(self, response):
        self.domain = 'https://www.idealista.com'
        publications = response.css('.items-container > article > .item')
        #publications = response.css('.items-container > article > .item')[:1]
        for house in publications:
            url = house.css('.item-link::attr(href)').extract_first()
            #puede lanzar items, lo scrapea, y si lanzas urls como aca, definis la url y el callback
            yield Request(
                url=self.domain + url,
                callback=self.parse_publication)

    def parse_publication(self, response):
        loader = ItemLoader(response=response, item=IdealistaItem())
        loader.add_value('url', response.url)
        loader.add_value('external_id', response.url.split('/')[-2])
        loader.add_css('title', 'h1 span::text')
        loader.add_css('size', '#main >.container > .clearfix .main-info .info-data span:nth-child(2) .txt-big::text')
        loader.add_css('price', '#main >.container > .clearfix .main-info .info-data span:nth-child(1) .txt-big::text')
        loader.add_css('deposit_months', '.txt-deposit > span::text')
        loader.add_css('description', '.commentsContainer .adCommentsLanguage::text')
        loader.add_css('price_m2','.details-block div p:nth-child(2)::text')
        loader.add_css('basic_features', '#details > div:nth-child(3) ul li::text')
        loader.add_css('building_features', '#details > div:nth-child(4) ul li::text')
        loader.add_css('equipment', '#details > div:nth-child(5) ul li::text')
        loader.add_css('street','#addressPromo > ul > li:nth-child(1)::text')
        loader.add_css('neighborhood','#addressPromo > ul > li:nth-child(2)::text')
        loader.add_css('district','#addressPromo > ul > li:nth-child(3)::text')
        loader.add_css('city','#addressPromo > ul > li:nth-child(5)::text')
        loader.add_css('updated', '#stats p::text')
        loader.add_css('advertiser_phone', '.phone >p::text')
        loader.add_css('advertiser_name','.advertiser-data > p:first-child::text')

        loader.add_css('pictures', '.placeholder-multimedia img::attr(data-service)')
        loader.add_css('mini_pictures', '.placeholder-multimedia img::attr(data-service)')
        yield loader.load_item()
