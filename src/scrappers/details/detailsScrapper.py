class DetailScrapper:
    
    def normalisation(self, value):
        for key in ["name", "brand"] : value[key] = value[key].strip().replace("-","").replace(" ","_")
        value["brand"] = value["brand"].lower()
        value["name"] = value["name"].lower()
        # if any(map(str.isdigit,value["name"].split("_")[-1]) and len(value["name"].split("_")) > 1):
        #     value["name"] = "_".join(value["name"].split("_")[:-1])
        return value