# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from email.policy import default
from optparse import Option
from posixpath import split
import scrapy
from scrapy.loader import ItemLoader
from dataclasses import dataclass, field
from typing import Optional
from itemloaders.processors import TakeFirst, MapCompose
import re



########################### Funções de limpeza ##################################
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

def testa_str(value):
    return isinstance(value, str)

def limpar_n_parcelas(value):
    return int(value.split()[0].replace('x', ''))

def limpar_valor_parcelas(value):
    return float(value.split()[-1].replace('R$', '').replace('.','').replace(',', '.'))

########################### Items ############################

class GdgScrapyItem(scrapy.Item):

    # define the fields for your item here like:
    
    url = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    ref: Optional[str] = scrapy.Field(default='Null',
        input_processor=MapCompose(remove_ref),
        output_processor=TakeFirst())
    
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
        input_processor=MapCompose(testa_str),
        output_processor=TakeFirst()
    )
    
    promocao: Optional[bool] = scrapy.Field(default=False,
        output_processor=TakeFirst(),
        input_processor = MapCompose(testa_str)
    )
    
    entrega_imediata = scrapy.Field(
        output_processor=TakeFirst(),
        input_processor = MapCompose(testa_str)
    )
    
    frete_gratis = scrapy.Field(
        output_processor=TakeFirst(),
        input_processor = MapCompose(testa_str)
    )
    
    lancamento = scrapy.Field(
        output_processor=TakeFirst(),
        input_processor = MapCompose(testa_str)
    )
    
    date_scrapy = scrapy.Field(
        output_processor=TakeFirst()
    )
    
    n_parcelas = scrapy.Field(
        output_processor=TakeFirst(),
        input_processor=MapCompose(limpar_n_parcelas)
    )

    valor_parcelas = scrapy.Field(
        input_processor=MapCompose(limpar_valor_parcelas),
        output_processor=TakeFirst()
    )