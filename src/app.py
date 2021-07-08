from flask import Flask
from src.utils.queryBuilder import QueryBuilder
from src.db.ElasticsearchController import ElasticsearchController

class AppHelper:
    
    _instance = None
    app = Flask(__name__)
    _es = ElasticsearchController.getInstance()
         
    def __init__(self):
        raise RuntimeError('Call getInstance() instead')
    
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    def get_app(self): return self.app
    
    def get_elastic(self): return self._es
    
    def set_sites(self, sites): self._sites = sites
    
    def get_sites(self): return self._sites


class App:
    
    app = AppHelper.getInstance().get_app()
    
    def __init__(self, sites):
        AppHelper.getInstance().set_sites(sites)
    
    @staticmethod
    def normalize(value):
        value = value.strip().replace("'","").replace("-","")
        
    @staticmethod
    @app.route('/sites/<site>', methods=['POST'])
    def get_by_site(site):
        App.normalize(site)
        builder = QueryBuilder()
        builder.get_all()
        body = builder.getQuery()
        del builder
        return AppHelper.getInstance().get_elastic().query(body, index=site)
    
    @staticmethod
    @app.route('/brands/<brand>', methods=['POST'])
    def get_by_brand(brand):
        App.normalize(brand)
        builder = QueryBuilder()
        builder.get_all()
        body = builder.getQuery()
        del builder
        return AppHelper.getInstance().get_elastic().query(body, index=brand)
    
    @staticmethod
    @app.route('/prodbybrand/<brand>/<prod>', methods=['POST'])
    def get_prod_by_brand(brand, prod):
        App.normalize(brand)
        App.normalize(prod)
        return AppHelper.getInstance().get_elastic().doc(index=brand, uid=prod)
    
    @staticmethod
    @app.route('/details/<prod>', methods=['POST'])
    def get_prod_details(prod):
        App.normalize(prod)
        helper = AppHelper.getInstance()
        list_results = [ helper.get_elastic().doc(index=site, uid=prod) for site in helper.get_sites()]
        list_results = list(filter(any, list_results))
        if list_results :return App.group_by_site(list_results) 
        else: return {}
        
    @staticmethod
    def group_by_site(list_results):
        print(list_results)
        result = list_results.pop()
        result["sites"] = dict()
        result["sites"][result["site"]] = {"price":result["price"], "position": result["position"]}
        del result["site"]
        del result["price"]
        del result["position"]
        for res in  list_results:
            result["sites"][res["site"]] = {"price": res["price"], "position": res["position"]}
        return result
    
    def start(self):
        self.app.run(host='0.0.0.0', port=5000, debug=True)
        
    