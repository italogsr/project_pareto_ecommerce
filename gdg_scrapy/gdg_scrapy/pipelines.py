# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class GdgScrapyPipeline:
    def __init__(self):
        self.create_conection()
        self.create_table()
        self.ref_seen = set()
 

    
    
    def create_conection(self):    
        self.conn = sqlite3.connect('gdg_db_geral')
        self.cur = self.conn.cursor()
     
    
    def create_table(self):
        self.cur.execute(""" CREATE TABLE IF NOT EXISTS gdg_produtos_3(
        url              TEXT,
        desconto         REAL,
        valor_boleto     REAL,       
        nome             TEXT, 
        imagem           TEXT,
        valor_riscado    REAL,            
        ref              TEXT,            
        esgotado         TEXT,
        promocao         TEXT,
        entrega_imediata TEXT,
        frete_gratis     TEXT, 
        lancamento       TEXT, 
        date_scrapy      TEXT,
        categoria_url    TEXT,
        n_parcelas       REAL,
        valor_parcelas   REAL
        )""")
    
    def process_item(self, item, spider):
        #Converter desconto para decimal 
        item['desconto'] = float(item['desconto'])/100

        #Dropar Dublicados
        #if item['ref'] in self.ref_seen:
        #    raise DropItem("Duplicate item refs found: %s" % item)
        #else:
        #    self.ref_seen.add(item['ref'])            
        adapter = ItemAdapter(item)
       
        if adapter['ref'] in self.ref_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.ref_seen.add(adapter['ref'])
                  
        #Grava no DB
        self.store_db(item)
        return item
        

    def store_db(self, item):
        self.cur.execute(""" INSERT OR IGNORE INTO gdg_produtos_3 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
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