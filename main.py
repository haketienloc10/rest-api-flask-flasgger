from flask import Flask, jsonify, request, url_for
from flask_pymongo import PyMongo
from database import mongo
from hello import hello_bp
from crawl import crawl_bp

app = Flask(__name__)
# app.config.from_object('config')
# mongo.init_app(app)

# app.register_blueprint(hello_bp, url_prefix='/hello')
app.register_blueprint(crawl_bp, url_prefix='/crawl')

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

if __name__ == "__main__":
    app.run(debug=True)
