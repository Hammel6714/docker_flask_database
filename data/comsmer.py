import pika
import time
import logging
import warnings
from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("mongodb://rs1:27041/") 
db = conn.test
collection = db.col

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq', port=5672))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):

    message = body.decode("utf-8") 
    logging.info('receive messages:' + message)
    time.sleep(body.count(b'.'))
    
    dimessage = eval(message)
    collection.insert_one(dimessage)

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
