#!/usr/bin/python
from datetime import timedelta
from flask import Flask, jsonify, make_response, request, current_app, abort
from functools import update_wrapper, wraps
from utils import initialize, get_chart_data, get_content_data_chart, get_cdt_data,get_crossref_data_chart
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.contrib.cache import SimpleCache

app = Flask(__name__)

CACHE_TIMEOUT = 300

cache = SimpleCache()

class cached(object):

    def __init__(self, timeout=None):
        self.timeout = timeout or CACHE_TIMEOUT

    def __call__(self, f):
        @wraps(f)
        def decorator(*args, **kwargs):
            response = cache.get(request.path)
            if response is None:
                response = f(*args, **kwargs)
                cache.set(request.path, response, self.timeout)
            return response
        return decorator

def crossdomain(origin=None, methods=None, headers=None,max_age=21600, attach_to_all=True,automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        @wraps(f)
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/chartdata',methods = ['GET'])
@crossdomain(origin='*')
@cached()
def get_chartdata():
	obj = get_chart_data()
	return jsonify(obj)

@app.route('/cdt',methods = ['GET'])
@crossdomain(origin='*')
@cached()
def get_cdt():
    obj = get_cdt_data()
    return jsonify(obj)

'''
@app.route('/cdtdata/<string:ht>',methods = ['GET'])
@crossdomain(origin='*')
def get_cdtdata(ht):
    obj = get_cdtdata(ht)
    return jsonify(obj)
'''

@app.route('/crossref/<string:ht>',methods = ['GET'])
@crossdomain(origin='*')
def get_crossref(ht):
    obj = get_crossref_data_chart(ht)       
    return jsonify(obj)

@app.route('/contentdata/<string:ht>',methods = ['GET'])
@crossdomain(origin='*')
def get_contentdata(ht):
    contentArray = get_content_data_chart(ht)
    obj = {
        "data" : contentArray
    }       
    return jsonify(obj)

@app.route('/test')
@crossdomain(origin='*')
def get_test():
    return "Testing the Seeding Food Studies Application"

if __name__ == '__main__':
    handler = RotatingFileHandler('seedfoodstudy.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.WARNING)
    app.logger.addHandler(handler)
    initialize()
    app.run(debug='true')


