from json.encoder import py_encode_basestring
from operator import concat
from numpy import concatenate
import scrapy


class GdgHomeSpider(scrapy.Spider):
    name = 'gdg_home'
    allowed_domains = ['www.graodegente.com.br']
    start_urls = ['http://www.graodegente.com.br/']

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
        self.log(response.xpath(
            '//*[@id="main-app"]/div[4]/section/div[7]/div[2]/div[1]/b/text()').extract_first()
            )
    
    def parse_product(self, response):
        pass

    
    def parse_inner_product(self, response):
        pass