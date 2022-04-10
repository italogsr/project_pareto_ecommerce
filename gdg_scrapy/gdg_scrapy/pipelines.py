# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class GdgScrapyPipeline:
    def __init__(self):
        self.create_conection()
        self.create_table()
        self.ref_seen = set()
 

    
    
    def create_conection(self):    
        #Dados de autenticação definidos no arquivo json
        self.conn = mysql.connector.connect(
            host = "host_name",
            user = "user_name",
            passwd = "passwd",
            database = "database_name"
        )
        self.cur = self.conn.cursor()
     
    
    def create_table(self):
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS produtos(
        url              TEXT,
        desconto         FLOAT,
        valor_boleto     FLOAT,       
        nome             TEXT, 
        imagem           TEXT,
        valor_riscado    FLOAT,            
        ref              TEXT,            
        esgotado         BOOL,
        promocao         BOOL,
        entrega_imediata BOOL,
        frete_gratis     BOOL, 
        lancamento       BOOL, 
        date_scrapy      DATETIME,
        categoria_url    TEXT,
        n_parcelas       INT,
        valor_parcelas   FLOAT
        )""")
    
    def process_item(self, item, spider):
        #Converter desconto para decimal 
        item['desconto'] = float(item['desconto'])/100

        #Remover item duplicado        
        adapter = ItemAdapter(item)
       
        if adapter['ref'] in self.ref_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ref_seen.add(adapter['ref'])
                  
        #Grava no DB
        self.store_db(item)
        return item
        

    def store_db(self, item):
        self.cur.execute(
            """INSERT INTO produtos (url,
            desconto,
            valor_boleto,
            nome,
            imagem,
            valor_riscado,
            ref,
            esgotado,
            promocao,
            entrega_imediata,
            frete_gratis,
            lancamento,
            date_scrapy,
            categoria_url,
            n_parcelas,
            valor_parcelas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            
            (item['url'],
            item['desconto'],
            item['valor_boleto'],       
            item['nome'], 
            item['imagem'],
            item['valor_riscado'],            
            item['ref'],            
            item['esgotado'],
            item['promocao'],
            item['entrega_imediata'],
            item['frete_gratis'], 
            item['lancamento'], 
            item['date_scrapy'],
            item['categoria_url'],
            item['n_parcelas'],
            item['valor_parcelas']
         ))       
        self.conn.commit()