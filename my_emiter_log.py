import pika
import json
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

type_message = ''.join(sys.argv[1]).lower()
my_message = ' '.join(sys.argv[2:]).lower()


body= {
    'type': type_message,
    'message': my_message
}

channel.basic_publish(exchange='direct_logs', routing_key=type_message, body=json.dumps(body))

print('[X] sent')

connection.close()