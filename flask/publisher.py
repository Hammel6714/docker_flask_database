import pika
import sys

def publisher(re):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.1'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue',durable=True)

    #message = ''.join(sys.argv[1:]) or 'Hello World!'
    message = re or 'Hello'

    channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))
    print(" [x] Sent %r" % message)

    connection.close()

#publisher()
