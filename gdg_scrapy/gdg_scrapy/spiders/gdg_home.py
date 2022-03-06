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
        './/div[@class="main-nav-sub"]/div[@class="main-nav-sub--container has-sub todas-as-categorias"]/div[@class="main-nav-sub--links"]/a'
        )
        
        self.log(len(categorias))
        for categoria in categorias:
            cat_url = categoria.xpath('./@href').extract_first()
            
            link = 'http://www.graodegente.com.br' + cat_url
        
            yield scrapy.Request(
                url=link,
                callback=self.parse_category
            )

    def parse_category(self, response):
        
        item = GdgScrapyItem()
        
        
        #Nome das Categorias             
        categoria = response.xpath(            
            '//ol[@class="container-flex"]/li[last()]/span/strong/text()'
        ).extract_first()        
                      
        #Coletar Produtos
        
        for produto in response.xpath('//ul[@class="grid-list"]/li'):
            loader = ItemLoader(item=GdgScrapyItem(),
                                selector = produto)


            loader.add_xpath('url', './/meta[@itemprop="url"]/@content')
            loader.add_xpath('desconto', './/p[@class ="content__discount"]/text()')
            loader.add_xpath('valor_boleto', './/p[@class="content__price"]/span[3]/text()')        
            loader.add_xpath('nome', './/h2/text()')
            loader.add_xpath('imagem', './/div[@class="product-tile--container__figure"]//img/@src')
            loader.add_css('valor_riscado', '.mini-letter span ::text')            
            loader.add_css('parcelas', '.content__installments ::text')
            loader.add_css('ref', '.content__ref ::text')
            loader.add_value('categoria', categoria)
            
            item = loader.load_item()
            
            
            #item['url'] = produto.xpath('.//meta[@itemprop="url"]/@content').extract_first()
            #item['ref'] = produto.css('.content__ref ::text').get()
            #item['nome']= produto.xpath('.//h2/text()').extract_first()
            #item['imagem'] = produto.xpath('.//div[@class="product-tile--container__figure"]//img/@src').extract_first()
            #item['valor_riscado'] = response.css(".mini-letter span ::text").get()
            #item['valor_boleto'] = produto.xpath('.//p[@class="content__price"]/span[3]/text()').extract_first()
            #item['parcelas'] =  produto.css(".content__installments ::text").get()
            #item['desconto'] = produto.xpath('.//p[@class ="content__discount"]/text()').extract_first()
            
            yield item   
        
        #yield{
        #        'ref': ref,
        #        'url': url,
        #        'categoria': categoria,
        #        'nome': nome,
        #        'imagem': imagem,
        #        'valor_riscado': valor_riscado,
        #        'valor_boleto': valor_boleto,
        #        'parcelas': parcelas,
        #        'desconto': desconto
        #    }
        next_page = response.xpath('//ul[@class ="paginate container-flex"]/li[last()]/a/@href').extract_first()
        np_complete_url = 'http://www.graodegente.com.br' + next_page

        if next_page is not None:
            yield response.follow(np_complete_url, callback=self.parse_category)