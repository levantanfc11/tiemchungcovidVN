# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiemchungItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tinh_thanhpho = scrapy.Field()
    dukien_vacxinphanbo = scrapy.Field()
    phanbo_thucte = scrapy.Field()
    dansodudieukientiemchung = scrapy.Field()
    solieudatiemchung = scrapy.Field()
    tyledukiensetiemchung = scrapy.Field()
    tyledatiemchung = scrapy.Field()
    tyledatiemitnhatmotmui = scrapy.Field()
    tyledatiemchung_trenvacxinphanbothucte = scrapy.Field()
    tylephanbovacxin_trenvacxinphanbocanuoc = scrapy.Field()
    pass
