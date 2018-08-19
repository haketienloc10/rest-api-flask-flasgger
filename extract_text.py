import scrapy
from selenium import webdriver
from  bs4 import BeautifulSoup
import time

class ExtractTextSpider(scrapy.Spider):

    name = 'text'
    handle_httpstatus_list = [404, 500, 503]

    def parse(self, response):
        try:
            start = time.time()
            print(response.url)
            print(self.sxpath)
            browser = webdriver.PhantomJS('/home/dtloc/flask-scrapy/tool/phantomjs')
            browser.get(response.url)
            html = browser.execute_script("return document.documentElement.outerHTML")
            print(html)
            soup = BeautifulSoup(html,'html.parser')
            print(soup.findAll('//*[@id="yesnojs"]'))
            # element = browser.find_elements(By.XPATH,self.sxpath)
            # for e in element:
            #     print(e.text.strip() + "XXX")
            #     self.quotes_list.append(e.text.strip())
        finally:
            browser.quit()
            end = time.time()
            print(end - start)
