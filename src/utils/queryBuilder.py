class QueryBuilder:
    
    def __init__(self):
        self.query = dict()        
            
    def get_all(self):
        self.query = {
            "match_all": {}
        }
    
    def getQuery(self):
        return self.query