def greeting_callback(channel, method, properties, body):
    print(f"Message received:{body}")
    # channel.basic_ack(delivery_tag=method.delivery_tag)