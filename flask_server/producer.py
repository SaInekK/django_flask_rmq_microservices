import os
import json

import pika

# params = pika.URLParameters(os.getenv("AMQP_URL"))
# connection = pika.BlockingConnection(params)
# channel = connection.channel()


def publish(method, body):
    params = pika.URLParameters(os.getenv("AMQP_URL"))
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    if not connection or connection.is_closed:
        connection = pika.BlockingConnection(params)

        channel = connection.channel()
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
