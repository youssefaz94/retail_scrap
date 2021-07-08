from elasticsearch.exceptions import NotFoundError

# decorator to handle elasticsearch queries exception and return format
def elastic_queries_hander(func):
    def query_hander(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundError:
            return {}
    return query_hander
