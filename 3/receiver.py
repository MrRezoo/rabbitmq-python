import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
ch1 = connection.channel()

ch1.exchange_declare(exchange='logs', exchange_type='fanout')

result = ch1.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

ch1.queue_bind(exchange='logs', queue=queue_name)
print('waiting for logs')


def callback(ch, method, properties, body):
    print(f'Received {body}')


ch1.basic_consume(queue=queue_name, on_message_callback=callback,
                  auto_ack=True)

ch1.start_consuming()
