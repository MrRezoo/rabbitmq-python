import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.exchange_declare('logs', exchange_type='fanout')

# channel.queue_declare(queue='echo')
# channel.queue_declare(queue='logs')

channel.basic_publish(exchange='', routing_key='echo', body=b'Hello word')
channel.basic_publish(exchange='logs', routing_key='logs', body=b'Hello word')

connection.close()
