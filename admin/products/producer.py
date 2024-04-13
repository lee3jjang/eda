import pika

params = pika.URLParameters(
    "amqps://hjrwcpkr:hTiyvkypUcYq-1FicLwDl054cO7BE1xs@dingo.rmq.cloudamqp.com/hjrwcpkr"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="main", body="hello")
