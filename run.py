import crochet
crochet.setup()

import json

from flask import Flask, request
from scrapy.crawler import CrawlerRunner

from extract_text import QuoteSpider


app = Flask('Scrape With Flask')
crawl_runner = CrawlerRunner()
quotes_list = []
scrape_in_progress = False
scrape_complete = False


@app.route('/add_url')
def greeting():
    url = request.args.get('url')
    return 'Hello %s' % (url)


@app.route('/crawl')
def crawl_for_quotes():
    global scrape_in_progress
    global scrape_complete

    if not scrape_in_progress:
        scrape_in_progress = True
        global quotes_list
        scrape_with_crochet(quotes_list)
        return 'SCRAPING'
    elif scrape_complete:
        return json.dumps(quotes_list)
    return 'SCRAPE IN PROGRESS'


@crochet.run_in_reactor
def scrape_with_crochet(_list):
    eventual = crawl_runner.crawl(QuoteSpider, quotes_list=_list)
    eventual.addCallback(finished_scrape)


def finished_scrape(null):
    global scrape_complete
    scrape_complete = True


if __name__ == '__main__':
    app.run('0.0.0.0', 9000)
