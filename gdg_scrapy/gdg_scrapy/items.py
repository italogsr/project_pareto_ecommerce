# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose

def remove_moeda(valor):
    return valor.replace('R$', '').strip()


def remove_valor_riscado(valor_riscado):
    return valor_riscado.replace('de R$', '').strip()


def remove_ref(valor_raw):
    return valor_raw.replace('Ref:','').strip()


def limpa_desconto(valor):
    return valor.replace('%', '').strip()


def limpa_parcelas(condicao):
    return condicao.strip()


class GdgScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    
    url = scrapy.Field(output_processor=TakeFirst())
    
    ref = scrapy.Field(
        input_processor=MapCompose(remove_ref),
        output_processor=TakeFirst()
    )
    
    nome = scrapy.Field(output_processor=TakeFirst())
    
    imagem = scrapy.Field(output_processor=TakeFirst())
    
    valor_riscado = scrapy.Field(
        input_processor=MapCompose(remove_valor_riscado),
        output_processor=TakeFirst()
    )
    
    valor_boleto = scrapy.Field(
        input_processor=MapCompose(remove_moeda),
        output_processor=TakeFirst()
    )
    
    parcelas =  scrapy.Field(
        input_processor=MapCompose(limpa_parcelas),
        output_processor=TakeFirst()
    )
    
    desconto = scrapy.Field(
        input_processor=MapCompose(limpa_desconto),
        output_processor=TakeFirst()
    )
    
    categoria = scrapy.Field(output_processor=TakeFirst())
    

