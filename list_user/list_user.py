from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings

from flasgger import Swagger
from flasgger import swag_from

from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("mongodb://rs2:27042/")
db = conn.test
collection = db.col

app = Flask(__name__)

swagger = Swagger(app)

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

@app.route('/list_user', methods=['GET'])
@app.route('/', methods=['GET'])
@swag_from('apidocs/api_list_user.yml')

def list_user():
    user = collection.find({})
    data = [d for d in user]
    sd = ",".join('%s' %id for id in data)
    return sd

@app.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)
