import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
ch1 = connection.channel()

ch1.queue_declare(queue='hello')

ch1.basic_publish(body="hello word", exchange='', routing_key='hello')
print(" [x] Sent 'Hello World!'")
connection.close()
