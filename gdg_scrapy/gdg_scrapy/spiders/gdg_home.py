import scrapy


class GdgHomeSpider(scrapy.Spider):
    name = 'gdg_home'
    allowed_domains = ['www.graodegente.com.br']
    start_urls = ['https://www.graodegente.com.br/abajur-1']

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
        #Nome das Categorias             
        categoria = response.xpath(
            '//*[@id="main-app"]/div[4]/section/div[7]/div[2]/div[1]/b/text()'
        ).extract_first()        
        # categoria =  response.xpath('//h1[@class = "h2 hidden"]/text()')
        #Captura toda a grade de produtos         
        grid = response.xpath('//ul[@class="grid-list"]')
        
        #Coletar Produtos
        
        for produto in response.xpath('//ul[@class="grid-list"]/li'):
            
            url = produto.xpath('.//meta[@itemprop="url"]/@content').extract_first()
            ref = produto.xpath('.//p[@class="content__ref"]/text()').extract_first()
            nome = produto.xpath('.//h2/text()').extract_first()
            imagem = produto.xpath('.//div[@class="product-tile--container__figure"]//img/@src').extract_first()
            valor_riscado = produto.xpath('.//span[@class="line-through"]/text()').extract_first()
            valor_boleto = produto.xpath('.//p[@class="content__price"]/span[3]/text()').extract_first()
            parcelas =  produto.xpath('.//span[@class="content__installments"]/text()').extract_first()
            desconto = produto.xpath('.//p[@class ="content__discount"]/text()').extract_first()
        
            yield{
                'ref': ref,
                'url': url,
                'categoria': categoria,
                'nome': nome,
                'imagem': imagem,
                'valor_riscado': valor_riscado,
                'valor_boleto': valor_boleto,
                'parcelas': parcelas,
                'desconto': desconto
            }
        next_page = response.xpath('//ul[@class ="paginate container-flex"]/li[last()]/a/@href').extract_first()
        np_complete_url = 'http://www.graodegente.com.br' + next_page

        if next_page is not None:
            yield response.follow(np_complete_url, callback=self.parse_category)