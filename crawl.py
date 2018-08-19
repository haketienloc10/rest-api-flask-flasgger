import crochet
crochet.setup()

from flask import request, jsonify, Blueprint
import json
from scrapy.crawler import CrawlerRunner
from extract_text import ExtractTextSpider
from extract_href import ExtractHrefSpider
from extract_img import  ExtractImgSpider
from bson import json_util

crawl_bp = Blueprint('scrapy', __name__)

crawl_runner = CrawlerRunner()
quotes_list = []
scrape_in_progress = False
scrape_complete = False
star_urls = []
_sxpath = ''

@crawl_bp.route("/", methods=['GET'])
def hello():
    return 'hello!'

@crawl_bp.route("/", methods=['POST'])
def add_url():
    global star_urls
    star_urls = request.json['urls']
    print(star_urls)
    for i in range(0, len(star_urls)):
        print(star_urls[i].find('/', 8))
        x = star_urls[i].find('/', 8)
        s = star_urls[i][:x+1]
        e = star_urls[i][x + 1:]
        star_urls[i] = s + e
        print(star_urls[i])
    return jsonify(star_urls)

@crawl_bp.route('/extract', methods=['GET'])
def extract_text():
    global scrape_in_progress
    global scrape_complete
    global _sxpath
    _sxpath = request.args.get('sxpath')
    if not scrape_in_progress:
        scrape_in_progress = True
        global quotes_list
        scrape_with_crochet(ExtractTextSpider,quotes_list)
        return 'SCRAPING'
    elif scrape_complete:
        scrape_in_progress = False
        scrape_complete = False
        res_js = json.loads(json_util.dumps(quotes_list))
        return jsonify(res_js)
    return 'SCRAPE IN PROGRESS'

@crawl_bp.route('/extract_href', methods=['GET'])
def extract_href():
    global scrape_in_progress
    global scrape_complete
    if not scrape_in_progress:
        scrape_in_progress = True
        global quotes_list
        scrape_with_crochet(ExtractHrefSpider,quotes_list)
        return 'SCRAPING'
    elif scrape_complete:
        scrape_in_progress = False
        scrape_complete = False
        res_js = json.loads(json_util.dumps(quotes_list))
        return jsonify(res_js)
    return 'SCRAPE IN PROGRESS'

@crawl_bp.route('/extract_img', methods=['GET'])
def extract_img():
    global scrape_in_progress
    global scrape_complete
    if not scrape_in_progress:
        scrape_in_progress = True
        global quotes_list
        scrape_with_crochet(ExtractImgSpider,quotes_list)
        return 'SCRAPING'
    elif scrape_complete:
        scrape_in_progress = False
        scrape_complete = False
        res_js = json.loads(json_util.dumps(quotes_list))
        return jsonify(res_js)
    return 'SCRAPE IN PROGRESS'

@crochet.run_in_reactor
def scrape_with_crochet(_spider, _list):
    global star_urls
    if len(_list) > 0:
        _list.clear()
        print('clear')
    print("1:" + _sxpath)
    eventual = crawl_runner.crawl(_spider, start_urls=star_urls, quotes_list=_list, sxpath= _sxpath)
    eventual.addCallback(finished_scrape)

def finished_scrape(null):
    global scrape_complete
    scrape_complete = True
    print("crawl end..")

@crawl_bp.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@crawl_bp.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400
