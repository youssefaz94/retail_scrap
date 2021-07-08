from elasticsearch import Elasticsearch
from src.utils.exceptionDecorators import elastic_queries_hander

class ElasticsearchController:
    
    """
    singleton class manages elasticsearch
    """
    
    _elastico = None
    _instance = None
         
    def __init__(self):
        raise RuntimeError('Call getInstance() instead')
    
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
            cls.bootstrap()
        return cls._instance
    
    @classmethod
    def bootstrap(cls):
        cls._elastico = Elasticsearch()
    
    # adds new doc for site indexes
    def index_site(self, product, pid):
        site = product["site"]
        self._elastico.index(index=site, id=pid, body=product)
    
    # adds new doc for brands indexes
    def index_brand(self, product, pid):
        brand = product["brand"]
        self._elastico.index(index=brand, id=pid, body=product)
    
    ## adds a new document
    def index(self, product):
        pId = product["name"]
        self.index_brand(product=product, pid=pId)
        self.index_site(product=product, pid=pId)
    
    # search query
    @elastic_queries_hander
    def query(self, query, index):
        res = self._elastico.search(index=index, size=7000, body={"query": query})
        return res["hits"]

    # get by id query
    @elastic_queries_hander
    def doc(self, uid, index):
        res = self._elastico.get(index=index, id=uid)
        return res["_source"]