import requests
from scrapy.selector import Selector
import scrapy

class ExtractImgSpider(scrapy.Spider):

    name = 'img'
    handle_httpstatus_list = [404, 500]

    def parse(self, response):
        if response.status in (404, 500):
            response = requests.get(response.url)
        print(response.url)
        print(self.sxpath)
        selector = Selector(response)
        quotes = selector.xpath(self.sxpath + "/@src").extract()
        if len(self.quotes_list) > 0:
            self.quotes_list.clear()
        for quote in quotes:
            if len(quote.strip()) > 0:
                self.quotes_list.append(quote.strip())