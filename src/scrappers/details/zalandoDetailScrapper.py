from bs4 import BeautifulSoup
from src.scrappers.details.detailsScrapper import DetailScrapper
import json

class ZalandoDetailScrapper(DetailScrapper):
    
    _key_names = {
        "productName": "name",
        "productBrand": "brand",
        "productCategory": "category",
        "productPrice": "price"
    }
    
    def scrap(self, detail):
        soup = BeautifulSoup(detail, features="html.parser")
        value = soup.findAll("script")[6].string
        value = json.loads(str(value)[62:-4].replace("\\n","").replace("\\",""))
        return self.postProcessing(value) 
    
    def postProcessing(self, value):
        final_result = {"site": "zalando"}
        for old_name , new_name in self._key_names.items():
            final_result[new_name] = value[old_name]
        return self.normalisation(final_result)