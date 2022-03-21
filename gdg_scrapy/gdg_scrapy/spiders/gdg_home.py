import datetime
from email.policy import default
import scrapy
from gdg_scrapy.items import GdgScrapyItem
from itemloaders import ItemLoader


class GdgHomeSpider(scrapy.Spider):
    name = 'gdg_home'
    allowed_domains = ['www.graodegente.com.br']
    start_urls = ['https://www.graodegente.com.br']

    def parse(self, response):
        categorias = response.xpath(
       '//nav[@class="sidebar-home"]//li/a'
        )
       
        self.log(len(categorias))
        
        for categoria in categorias:
            cat_url = categoria.xpath('./@href').extract_first()
            cat_nome = categoria.xpath('./text()')
            link = 'http://www.graodegente.com.br' + cat_url
            yield scrapy.Request(
                url=link,
                callback=self.parse_grid
            )

    def parse_grid(self, response):
        
        item = GdgScrapyItem()    
                              
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

            

            loader.add_xpath('url', url) if produto.xpath(url) else loader.add_value('url', 'NA')
            
            loader.add_xpath('desconto', desconto) if produto.xpath(desconto) else loader.add_value('desconto', '0')
            loader.add_xpath('valor_boleto', valor_boleto) if produto.xpath(valor_boleto) else loader.add_value('valor_boleto', '0')        
            loader.add_xpath('nome', nome) if produto.xpath(nome) else loader.add_value('nome', 'NA')
            loader.add_xpath('imagem', imagem) if produto.xpath(imagem) else loader.add_value('imagem', 'NA')
            loader.add_css('valor_riscado', valor_riscado) if produto.css(valor_riscado) else loader.add_value('valor_riscado', '0')            
            #loader.add_css('str_parcelas', str_parcelas)
            loader.add_css('ref', ref) if produto.css(ref) else loader.add_value('ref', 'NA')           
            loader.add_xpath('esgotado', esgotado) if produto.xpath(esgotado) else loader.add_value('esgotado', False)       
            
            loader.add_xpath('promocao', promocao) if produto.xpath(promocao) else loader.add_value('promocao', False)
            loader.add_xpath('entrega_imediata', entrega_imediata) if produto.xpath(entrega_imediata) else loader.add_value('entrega_imediata', False)
            loader.add_xpath('frete_gratis', frete_gratis) if produto.xpath(frete_gratis) else loader.add_value('frete_gratis', False)
            loader.add_xpath('lancamento', lancamento) if produto.xpath(lancamento) else loader.add_value('lancamento', False)
            loader.add_value('date_scrapy', date)
            loader.add_xpath('categoria_url', url) if produto.xpath(url) else loader.add_value('categoria_url', 'NA')
            loader.add_css('n_parcelas', str_parcelas) if produto.css(str_parcelas) else loader.add_value('n_parcelas', '0')
            loader.add_css('valor_parcelas', str_parcelas) if produto.css(str_parcelas) else loader.add_value('valor_parcelas', '0')
            item = loader.load_item()
            
            
          
            
            yield item   
        
        
        next_page = response.xpath('//ul[@class ="paginate container-flex"]/li[last()]/a/@href'
        ).extract_first()
        
        np_complete_url = 'http://www.graodegente.com.br' + next_page

        if next_page is not None:
            yield response.follow(np_complete_url, callback=self.parse_grid)