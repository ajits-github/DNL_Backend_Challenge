from scrapy.crawler import CrawlerProcess
from parts_spider import PartsSpider
from database.db_manager import data_exists, initialize_database

if __name__ == "__main__":
    # Ensure the database is initialized (table is created if doesn't exist)
    initialize_database()

    if not data_exists():
        process = CrawlerProcess({'LOG_LEVEL': 'DEBUG'})
        process.crawl(PartsSpider)
        process.start()
    else:
        print("Data already exists in the database. Exiting...")
