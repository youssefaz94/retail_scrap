from bs4 import BeautifulSoup
import json

class ZalandoListingScrapper:
    
    def __init__(self):
        pass
    
    def preProcessing(self, line):
        return {
            line.get("data-artikel"): line.get("data-position")
        }
    
    def scrap(self, detail):
        attributes = dict()
        soup = BeautifulSoup(detail["body"], features="html.parser")
        values = soup.findAll('li', {"data-position": True})
        for val in values: attributes.update(self.preProcessing(val))
        return attributes