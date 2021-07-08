from src.db.ElasticsearchController import ElasticsearchController
import logging as lg

_logger = lg.getLogger(__name__)

class Product:
    _es = None
    
    def __init__(self, site):
        self._required = {"id","name", "brand", "category", "position"}
        self._required_attrs_exist = False
        self._attributes = {"site":site}
        self._es = ElasticsearchController.getInstance()
        
    def check_required(self):
        self._required_attrs_exist = self._required.issubset(self._attributes)
    
    def add_attributes(self, attrs):
        self._attributes.update(attrs)
        if not self._required_attrs_exist: self.check_required()
        
    def persist(self):
        if self._required_attrs_exist: 
            _logger.info("Product {} of {} is loaded in DB".format(self._attributes["id"],self._attributes["site"]))
            self._es.index(self._attributes)