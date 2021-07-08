from src.scrappers.scrapperFactory import ScrapperFactory
from src.models.product import Product
from json.decoder import JSONDecodeError
import jsonlines
import src
import os
import logging as lg

_logger = lg.getLogger(__name__)

class DataLoader:

    _products = dict()
    _positions = dict()
    _scrap_fact = None

    def __init__(self, site):
        self._site = site["site"]
        self._loc = site["loc"]
        self._scrap_fact = ScrapperFactory()
        self._scrapper = self._scrap_fact.getInstances(self._site)
                

    def start(self):
        _logger.info("Loader of {} is started".format(self._site))
        self.load_data()
        
    def new_detail(self, detail):
        new_prod = Product(self._site)
        detail_scrapper = self._scrapper["detail"]
        attrs = detail_scrapper.scrap(detail)
        new_prod.add_attributes(attrs)
        self._products[attrs["id"]] = new_prod
        _logger.info("New Product {} scrapped for site {}".format(attrs["id"], self._site))
    
    def new_listing(self, listing):
        listing_scrapper = self._scrapper["listing"]
        id_position = listing_scrapper.scrap(listing)
        self._positions.update(id_position)

    def load_data(self):
        base = os.environ['VIRTUAL_ENV'] if os.environ['VIRTUAL_ENV'] else os.path.dirname(os.path.abspath(src.__file__))
        location = os.path.join(
            os.path.dirname(base),
            self._loc
        )
        with jsonlines.open(location) as f:
            i = 1
            for line in f.iter():
                try:
                    if "detail" in line["page_type"]:
                        self.new_detail(line)
                    else:
                        self.new_listing(line)
                except AttributeError:
                    _logger.info("There are {} products that couldn't been scrapped for {}".format(i, self._site))
                    i+=1
                    continue
                
        _logger.info("Finished product scrapping for {}, starting loading into DB".format(self._site))
        self.persist()
        _logger.warn("Successfuly loaded {} products from {} into DB".format(len(self._products), self._site))
        
    def persist(self):
        for pId, prod in self._products.items():
            if pId in self._positions.keys():
                prod.add_attributes({"position": self._positions[pId]})
            else:
                prod.add_attributes({"position": "-1"})
            prod.persist()