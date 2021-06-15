from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings

from flasgger import Swagger
from flasgger import swag_from

from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("mongodb://rs3:27043/")
db = conn.test
collection = db.col

app = Flask(__name__)

swagger = Swagger(app)

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning)

@app.route('/login', methods=['GET','POST'])
@app.route("/", methods=['GET','POST'])
@swag_from('apidocs/api_login.yml')
def login():
    
    if request.method == 'POST':
        username=request.values['username']
        password=request.values['password']
        
        if (username=="")or(password==""):
            return "<h1>input error!</h1>"
        else:
        
            message = dict()
            message['username'] = username
            message['password'] = password
   
            message = json.dumps(message)
            logging.info('message:', message)

            dimessage = eval(message)

            if collection.find_one(dimessage) != None:
                return render_template('computer.html')
            else:
                return "<h1>Fail</h1>"
    else:
        return render_template('login.html')

@app.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5002,debug=True)
