import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')

#body = input('please write something:')
for i in range(10):
    channel.basic_publish(exchange='',routing_key='test', body=str(i))

print('[X] Sent')
connection.close()