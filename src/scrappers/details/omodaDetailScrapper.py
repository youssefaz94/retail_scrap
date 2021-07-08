from bs4 import BeautifulSoup
from src.scrappers.details.detailsScrapper import DetailScrapper
import json

class OmodaDetailScrapper(DetailScrapper):
    
    def scrap(self, detail):
        soup = BeautifulSoup(detail["body"], features="html.parser")
        # value = soup.find("main", {"id": '\\"detail\\"'}).get("data-google")
        value = soup.find("main", {"id": "detail"}).get("data-google")
        value = json.loads(value)
        return self.normalisation(value) 
