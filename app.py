from flask import Flask
from flask import request, redirect, jsonify

from url import UrlShortener
app = Flask(__name__)

DOMAIN_NAME = 'http://localhost:5000/'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getShortUrl', methods=['POST'])
def short_url():
    data = request.args
    if 'url' in data:
        url = data['url']
        short_url_code = UrlShortener.get_short_url(url)
        return DOMAIN_NAME + short_url_code

    return jsonify('url not provided'), 400

@app.route('/<key>')
def long_url(key):
    url = UrlShortener.get_long_url(key)
    if url:
        return redirect(url, code=302)

    return jsonify('not found'), 404
