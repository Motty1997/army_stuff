import json
import os
from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from db.mongo.repository.repository_row_data import insert_email

app = Flask(__name__)

load_dotenv(verbose=True)

def consume_all_messages():
    consumer = KafkaConsumer(
        'all_messages',
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest'
    )

    for message in consumer:
        insert_email(message.value)
        print(f'Received: {message.key}, {message.value}')


if __name__ == '__main__':
    consume_all_messages()
    app.run()
