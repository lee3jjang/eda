import pika

params = pika.URLParameters(
    "amqps://hjrwcpkr:hTiyvkypUcYq-1FicLwDl054cO7BE1xs@dingo.rmq.cloudamqp.com/hjrwcpkr"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback)

print("Start Consuming")

channel.start_consuming()

channel.close()