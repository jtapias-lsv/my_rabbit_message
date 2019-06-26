import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# for each consumer in a queue
result_queue = channel.queue_declare(queue='', exclusive=True)

queue_name=result_queue.method.queue

# making a list whit parameters passing by console
my_list = sys.argv[1:]

# loop for catching parameters
for rk in my_list:
    channel.queue_bind(exchange='direct_logs', queue = queue_name, routing_key=rk )

def callback(ch, method, properties, body):
    print(eval(body.decode())['type'])

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Starting consuming.....')
channel.start_consuming()