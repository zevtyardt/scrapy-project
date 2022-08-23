from scrapy.utils.log import configure_logging
from rich.logging import RichHandler
import logging

LOG_ENABLED = False
configure_logging(install_root_handler=False)

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler(show_time=False, show_path=False, level=logging.INFO)]
)

BOT_NAME = 'webcrawler'
SPIDER_MODULES = ['webcrawler.spiders']
NEWSPIDER_MODULE = 'webcrawler.spiders'

LOG_LEVEL = "INFO"
TELNETCONSOLE_ENABLED = False
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}
ITEM_PIPELINES = {
    'webcrawler.pipelines.ProcessPipeline': 300,
}

STATS_DUMP = False
CONCURRENT_ITEMS = 1
CONCURRENT_REQUESTS = 5
