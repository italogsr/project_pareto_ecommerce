# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
import re

def remove_moeda(valor):
    return float(valor.replace('R$', '').replace('.','').replace(',','.').strip())

def limpa_categoria(valor):
   return re.sub('\d+','', valor).split('/')[3].replace('-', ' ').title().strip()

def remove_valor_riscado(valor):
    return float(valor.replace('de R$', '').replace('.', '').replace(',', '.').strip())

def remove_ref(valor):
    return valor.replace('Ref:','').strip()


def limpa_desconto(valor):
    return valor.replace('%', '').strip()


def limpa_parcelas(condicao):
    return condicao.strip()

def testa_esgotado(value):
    return isinstance(value, str)

class GdgScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    url = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    ref = scrapy.Field(
        input_processor=MapCompose(remove_ref),
        output_processor=TakeFirst()
    )
    
    nome = scrapy.Field(
        output_processor=TakeFirst()
    )

    categoria_url = scrapy.Field(
        input_processor = MapCompose(limpa_categoria),
        output_processor = TakeFirst()
    )
    
    imagem = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    valor_riscado = scrapy.Field(
        input_processor=MapCompose(remove_valor_riscado),
        output_processor=TakeFirst()
    )
    
    valor_boleto = scrapy.Field(
        input_processor=MapCompose(remove_moeda),
        output_processor=TakeFirst()
    )
    
    str_parcelas =  scrapy.Field(
        input_processor=MapCompose(limpa_parcelas),
        output_processor=TakeFirst()
    )
    
    desconto = scrapy.Field(
        input_processor=MapCompose(limpa_desconto),
        output_processor=TakeFirst()
    )
    
    categoria = scrapy.Field(
        output_processor=TakeFirst()
    )

    esgotado = scrapy.Field(
        input_processor=MapCompose(testa_esgotado),
        output_processor=TakeFirst()
    )
    
    promocao = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    entrega_imediata = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    frete_gratis = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    lancamento = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    data_scrapy = scrapy.Field(
        output_processor=TakeFirst()
    )