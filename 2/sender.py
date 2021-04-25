import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
# build channel
ch1 = connection.channel()
# build queue≠

ch1.queue_declare(queue='fist', durable=True)

message = "this is a testing message"

ch1.basic_publish(exchange='', routing_key='first', body=message,
                  properties=pika.BasicProperties(delivery_mode=2, ))
print('sent message')
