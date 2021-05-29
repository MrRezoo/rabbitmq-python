import pika
from utils import greeting_callback

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.exchange_declare('logs', exchange_type='fanout')
queue = channel.queue_declare(queue='')
queue_name = queue.method.queue

channel.queue_bind(exchange='logs', queue=queue_name, routing_key='echo')

channel.basic_consume(
    queue=queue_name, on_message_callback=greeting_callback,
    auto_ack=True
)

channel.start_consuming()
