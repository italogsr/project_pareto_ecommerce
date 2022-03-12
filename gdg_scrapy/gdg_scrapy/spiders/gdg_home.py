import datetime
from email.policy import default
import scrapy
from gdg_scrapy.items import GdgScrapyItem
from itemloaders import ItemLoader


class GdgHomeSpider(scrapy.Spider):
    name = 'gdg_home'
    allowed_domains = ['www.graodegente.com.br']
    start_urls = ['https://www.graodegente.com.br/abajur-1']

#    def parse(self, response):
#        categorias = response.xpath(
#       '//nav[@class="sidebar-home"]//li/a'
#        #'.//div[@class="main-nav-sub"]/div[@class="main-nav-sub--container has-sub todas-as-categorias"]/div[@class="main-nav-sub--links"]/a'
#        )
        
#        self.log(len(categorias))
#       date = detetime.now().strftime()('%Y-%m-%d %H:%M:%S') 
#       for categoria in categorias:
#           cat_url = categoria.xpath('./@href').extract_first()
#           cat_nome = categoria.xpath('./text()')
#           link = 'http://www.graodegente.com.br' + cat_url
       
#           yield scrapy.Request(
#               url=link,
#               callback=self.parse_category
#           )

    def parse(self, response):
        
        item = GdgScrapyItem()
        
        
        #Nome das Categorias (Não está coletando corretamente (Será se isso ocorre apenas em itens duplicados?))             
        
        #categoria = response.xpath(            
        #    '//input[@id="categoria-nome"]/@value'
            #'//ol[@class="container-flex"]/li[last()]/span/strong/text()'
        #).extract_first()        
                      
        #Coletar Produtos
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for produto in response.xpath('//ul[@class="grid-list"]/li'):
            loader = ItemLoader(item=GdgScrapyItem(),
                                selector = produto)
            

            url = './/meta[@itemprop="url"]/@content'
            desconto =  './/p[@class ="content__discount"]/text()'
            valor_boleto =  './/p[@class="content__price"]/span[last()]/text()'
            nome = './/h2/text()'
            imagem = './/div[@class="product-tile--container__figure"]//img/@src'
            valor_riscado =  '.mini-letter span ::text'
            str_parcelas = '.content__installments ::text'
            ref = '.content__ref ::text'
            esgotado = './/div[@class="product-tile__soldoff"]/p/text()'
            promocao = './/img[@alt="Promoção"]/@src'
            entrega_imediata = './/div[@class="seloEntregaImediata"]//text()'
            frete_gratis = './/a[@class="content__freeShip freeShip-open"]/text()'
            lancamento = './/p[@class="figure__release-tag"]/text()'


            loader.add_xpath('url', url)
            loader.add_xpath('desconto', desconto)
            loader.add_xpath('valor_boleto', valor_boleto)        
            loader.add_xpath('nome', nome)
            loader.add_xpath('imagem', imagem)
            loader.add_css('valor_riscado', valor_riscado)            
            loader.add_css('str_parcelas', str_parcelas)
            loader.add_css('ref', ref)
            
            if produto in response.xpath('//ul[@class="grid-list"]/li'):
                loader.add_xpath('esgotado', esgotado)
            else:
                loader.add_value('esgotado', False)
            
            loader.add_xpath('promocao', promocao)
            loader.add_xpath('entrega_imediata', entrega_imediata)
            loader.add_xpath('frete_gratis', frete_gratis)
            loader.add_xpath('lancamento', lancamento)
            loader.add_value('data_scrapy', date)
            loader.add_xpath('categoria_url', url)
            
            item = loader.load_item()
            
            
          
            
            yield item   
        
        
        next_page = response.xpath('//ul[@class ="paginate container-flex"]/li[last()]/a/@href'
        ).extract_first()
        
        np_complete_url = 'http://www.graodegente.com.br' + next_page

        if next_page is not None:
            yield response.follow(np_complete_url, callback=self.parse)