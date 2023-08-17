BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Enable concurrency for faster scraping
CONCURRENT_REQUESTS = 10

# Logging
LOG_ENABLED = True
LOG_LEVEL = 'INFO'  # Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'