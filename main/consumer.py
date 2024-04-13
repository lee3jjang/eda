import json

import pika

from app import app, Product, db

params = pika.URLParameters(
    "amqps://hjrwcpkr:hTiyvkypUcYq-1FicLwDl054cO7BE1xs@dingo.rmq.cloudamqp.com/hjrwcpkr"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="main")


def callback(ch, method, properties, body):
    print("Received in main")
    data = json.loads(body)
    print(data)
    with app.app_context():
        if properties.content_type == "product_created":
            product = Product(id=data["id"], title=data["title"], image=data["image"])
            db.session.add(product)
            db.session.commit()

        if properties.content_type == "product_updated":
            product: Product = Product.query.get(data["id"])
            product.title = data["title"]
            product.image = data["image"]
            db.session.commit()

        if properties.content_type == "product_deleted":
            product: Product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)

print("Start Consuming")

channel.start_consuming()

channel.close()
