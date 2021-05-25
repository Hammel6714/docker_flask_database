from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings

from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)

swagger = Swagger(app)

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

@app.route('/list_user', methods=['GET'])
@app.route('/', methods=['GET'])
@swag_from('apidocs/api_list_user.yml')
def create_user():

    res = dict()
    res['username_1'] = 'Alice'
    res['username_2'] = 'Bob'
    res['username_3'] = 'Cindy'
    res = make_response(jsonify(res), 200)
    return res

@app.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)
