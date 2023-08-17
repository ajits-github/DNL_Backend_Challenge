from scrapy.crawler import CrawlerProcess
from parts_spider import PartsSpider
from database.db_manager import data_exists

if __name__ == "__main__": 
    if not data_exists():
        process = CrawlerProcess()
        process.crawl(PartsSpider)
        process.start()
    else:
        print("Data already exists in the database. Exiting...")
