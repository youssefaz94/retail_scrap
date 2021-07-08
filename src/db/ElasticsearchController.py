from elasticsearch import Elasticsearch

class ElasticsearchController:
    
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
    
    def index_site(self, product, pid):
        site = product["site"]
        del product["site"]
        self._elastico.index(index=site, id=pid, body=product)
    
    def index_brand(self, product, pid):
        brand = product["brand"]
        del product["brand"]
        self._elastico.index(index=brand, id=pid, body=product)
    
    def index(self, product):
        pId = product["id"]
        del product["id"]
        self.index_brand(product=product, pid=pId)
        self.index_site(product=product, pid=pId)
    
    def query(self, query, index):
        return self._elastico.search(index=index, size=7000, body={"query": query})

    def doc(self, uid, index):
        return self._elastico.get(index=index, id=uid)