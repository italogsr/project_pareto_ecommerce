import scrapy
from scrapy import Request
from scrapy.spiders import XMLFeedSpider
from scrapy.spiders import SitemapSpider


class GdgProductSpider(SitemapSpider):
    
    name = 'gdg_product'
    #start_urls = ['https://www.graodegente.com.br/sitemap.xml']
    #sitemap_rules = [('.*/oferta/.*', 'parse')]
            
   
    sitemap_urls = ['https://www.graodegente.com.br/sitemap.xml']
    sitemap_rules = [('graodegente', 'parse_products')]

    def parse_products(self, response):
        yield {'url': response.url,
                'nome': response.xpath('//*[@id="main-product"]/div[3]/div[2]/div[2]/p/span[3]/text()').extract(),
                'id':response.xpath('//meta[@itemprop="sku"]/@content').extract(),
                'nome': response.xpath('//meta[@itemprop="name"]/@content').extract()[1],
                'cor': response.css('.specification--name span ::text').get(),
                'espec': response.css('.specification--name ::text').getall(),
                'categoria': response.xpath('//meta[@itemprop="category"]/@content').extract(),
                'url':  response.xpath('//meta[@itemprop="url"]/@content').extract()[0],
                'preco_antigo': response.css('.offers small ::text').getall()[0],
                'preco_atual': response.css('.offers small ::text').getall()[1], 
                'preco_boleto': response.xpath('//meta[@itemprop="price"]/@content').extract(),
                'condicao_parcela': response.css('.offers__installments ::text').get(),
                'desconto_destaque': response.css('.discount-percentage ::text').get()
            }
   
   
   
   
   
   
   
    #def parse(self, response):
             
    ##    yield {
    ##       'id':response.xpath('//meta[@itemprop="sku"]/@content').extract(),
    #        'nome': response.xpath('//meta[@itemprop="name"]/@content').extract()[1],
    #        'cor': response.css('.specification--name span ::text').get(),
    #        'espec': response.css('.specification--name ::text').getall(),
    #        'categoria': response.xpath('//meta[@itemprop="category"]/@content').extract(),
    #        'url':  response.xpath('//meta[@itemprop="url"]/@content').extract()[0],
    #        'preco_antigo': response.css('.offers small ::text').getall()[0],
    #        'preco_atual': response.css('.offers small ::text').getall()[1], 
    #        'preco_boleto': response.xpath('//meta[@itemprop="price"]/@content').extract(),
    #        'condicao_parcela': response.css('.offers__installments ::text').get(),
    #        'desconto_destaque': response.css('.discount-percentage ::text').get()
    #        }