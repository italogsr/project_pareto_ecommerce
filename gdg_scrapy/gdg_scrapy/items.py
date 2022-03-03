# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_moeda(valor):
    return valor.replace('R$', '').strip()


class GdgScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    ref = scrapy.Field()
    nome = scrapy.Field()
    imagem = scrapy.Field()
    valor_riscado = scrapy.Field()
    valor_boleto = scrapy.Field()
    parcelas =  scrapy.Field()
    desconto = scrapy.Field()
    categoria = scrapy.Field()
    

