class DetailScrapper:
    
    def normalisation(self, value):
        for key in ["name", "brand"] : value[key] = value[key].strip().replace("-","").replace(" ","_")
        value["brand"] = value["brand"].lower()
        return value