import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

ch = connection.channel()
ch.queue_declare(queue='first', durable=True)
print('waiting for messages, press ctrl + c to exit')


def callback(channel, method, properties, body):
    print(f'received {body}')
    time.sleep(9)
    print('Done. . .')
    channel.basic_ack(delivery_tag=method.delivery_tag)


ch.basic_qos(prefetch_count=1)
ch.basic_consume(queue='first', on_message_callback=callback)
