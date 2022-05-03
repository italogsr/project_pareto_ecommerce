# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem



class GdgScrapyPipeline:
    def __init__(self):
        self.ref_seen = set()


    
    def process_item(self, item, spider):
        #Converter desconto para decimal 
        item['desconto'] = float(item['desconto'])/100

        #Remover item duplicado        
        adapter = ItemAdapter(item)
       
        if adapter['ref'] in self.ref_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ref_seen.add(adapter['ref'])
                  
        
        self.produtos = {'url': item['url'],
            'desconto': item['desconto'],
            'valor_boleto': item['valor_boleto'],       
            'nome': item['nome'], 
            'imagem': item['imagem'],
            'valor_riscado': item['valor_riscado'],            
            'ref':  item['ref'],            
            'esgotado': item['esgotado'],
            'promocao': item['promocao'],
            'entrega_imediata': item['entrega_imediata'],
            'frete_gratis': item['frete_gratis'], 
            'lancamento': item['lancamento'], 
            'date_scrapy': item['date_scrapy'],
            'categoria_url': item['categoria_url'],
            'n_parcelas': item['n_parcelas'],
            'valor_parcelas': item['valor_parcelas']}
        
        return self.produtos
    
