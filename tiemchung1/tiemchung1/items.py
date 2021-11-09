# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Tiemchung1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    a_STTs = scrapy.Field()
    b_citys = scrapy.Field()
    c_dukien_vacxinphanbo = scrapy.Field()
    d_phanbo_thucte = scrapy.Field()
    e_dansodudieukientiemchung = scrapy.Field()
    f_solieudatiemchung = scrapy.Field()
    g_tyledukiensetiemchung = scrapy.Field()
    h_tyledatiemchung = scrapy.Field()
    p_tyledatiemitnhatmotmui = scrapy.Field()
    s_tyledatiemchung_trenvacxinphanbothucte = scrapy.Field()
    t_tylephanbovacxin_trenvacxinphanbocanuoc = scrapy.Field()
    pass
