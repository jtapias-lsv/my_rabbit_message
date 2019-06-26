import pika
import time
from random import randint

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    tiempo = randint(1, 10)
    time.sleep(tiempo)
    print(f'[X]recived {body.decode()} con un tiempo de {tiempo}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

# asi se llama en orden no importando cuanto demore
#channel.basic_consume(queue='test', on_message_callback=callback, auto_ack=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test', on_message_callback=callback)

print('Waiting for a message...')
channel.start_consuming()