from bs4 import BeautifulSoup
from src.scrappers.details.detailsScrapper import DetailScrapper
import json

class ZiengsDetailScrapper(DetailScrapper):
    
    def scrap(self, detail):
        soup = BeautifulSoup(detail["body"], features="html.parser")
        value = dict()
        value["name"] = detail["page_url"].split("/")[-1].split(".")[0].split("-")[-1]
        value["id"] = value["name"].split("_")[-1]
        for meta in soup.find("body").findAll("meta"):
            val = meta.get("content").strip("\"\\")
            key = meta.get("itemprop").strip("\"\\")
            value[key] = val
        return self.normalisation(value) 
    