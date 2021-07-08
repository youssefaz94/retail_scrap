from bs4 import BeautifulSoup
import json

class ZiengsListingScrapper:
    
    def __init__(self):
        pass
    
    def scrap(self, detail):
        attributes = dict()
        soup = BeautifulSoup(detail["body"], features="html.parser")
        page_num = detail["page_number"]
        values = soup.find("div",{"id":"content"}).findAll("div", {"class":"item"})
        for i, pId in enumerate(values): attributes.update({pId: (i+1)*page_num})
        return attributes