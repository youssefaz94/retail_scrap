import json
import os
import src
from src.scrappers.details.omodaDetailScrapper import OmodaDetailScrapper
from src.scrappers.listings.omodaListingScrapper import OmodaListingScrapper
from src.scrappers.details.ziengsDetailScrapper import ZiengsDetailScrapper
from src.scrappers.listings.ziengsListingScrapper import ZiengsListingScrapper
from src.scrappers.details.zalandoDetailScrapper import ZalandoDetailScrapper
from src.scrappers.listings.zalandoListingScrapper import ZalandoListingScrapper


class ScrapperFactory:
    """
    factory class to create scrappers for each of the sites
    """
    
    _site_scrappers = dict()
    
    def __init__(self):
        self._site_scrappers = dict()
        self.setupScrappers()
    
    def setupScrappers(self):
        self._site_scrappers = {
            "omoda":{
                "detail": OmodaDetailScrapper(),
                "listing": OmodaListingScrapper()
            },
            "zalando":{
                "detail": ZalandoDetailScrapper(),
                "listing": ZalandoListingScrapper()
            },
            "ziengs":{
                "detail": ZiengsDetailScrapper(),
                "listing": ZiengsListingScrapper()
            }
        }
            
    def getInstances(self, site):
        return self._site_scrappers[site]
    