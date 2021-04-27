import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

ch = connection.channel()

ch.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = ch.queue_declare(queue='', exclusive=True)

queue_name = result.method.queue

severities = ('warning', 'error', 'info')

for severity in severities:
    ch.queue_bind(exchange='direct_logs', queue=queue_name,routing_key=severity)

print('Waiting for message')


def callback(channel, method, properties, body):
    print(f'{method.routing_key}', {body}, properties, channel)


ch.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
ch.start_consuming()
