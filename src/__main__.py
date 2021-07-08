import logging as lg 
from src.dataLoader import DataLoader
from src.app import App
from multiprocessing import Pool

_logger = lg.getLogger(__name__)

sites = [
    # {
    #     "site": "zalando",
    #     "loc": "20160530_nelson_mini_project_crawls/crawl_zalando.nl_2016-05-30T23-14-36.jl"
    # },
    {
        "site": "omoda",
        "loc": "20160530_nelson_mini_project_crawls/crawl_omoda.nl_2016-05-30T23-14-58.jl"
    },
    {
        "site": "ziengs",
        "loc": "20160530_nelson_mini_project_crawls/crawl_ziengs.nl_2016-05-30T23-15-20.jl"
    }
]

def setup_logging():
    # capture warnings issued by the warnings module
    lg.captureWarnings(True)

    logger = lg.getLogger()
    logger.setLevel(lg.DEBUG)

    # Configure stream logging if applicable
    stream_handler = lg.StreamHandler()
    stream_handler.setLevel(lg.INFO)

    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    stream_handler.setFormatter(lg.Formatter(fmt))
    logger.addHandler(stream_handler)

def main():
    setup_logging()    
    loaders = [DataLoader(site) for site in sites]
    for loader in loaders:
        loader.start()
    app = App([site["site"] for site in sites])
    app.start()

if __name__ == '__main__':
    main()
    