import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")

import django

django.setup()

import pika

from products.models import Product

params = pika.URLParameters(
    "amqps://hjrwcpkr:hTiyvkypUcYq-1FicLwDl054cO7BE1xs@dingo.rmq.cloudamqp.com/hjrwcpkr"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Received in admin")
    id = json.loads(body)
    print("id:", id)
    product = Product.objects.get(id=int(id))
    product.likes = product.likes + 1
    product.save()
    print("Product likes increased!")


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Start Consuming")

channel.start_consuming()

channel.close()
