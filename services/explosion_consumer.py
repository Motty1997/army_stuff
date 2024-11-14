import json
import os
from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer
from services.save_to_db import save_to_db


load_dotenv(verbose=True)

def consume_sentence_explosion():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EXPLOSION'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )

    for message in consumer:
        save_to_db(message.value, "E")
        print(f'received: {message.key} : {message.value}')


app = Flask(__name__)
if __name__ == '__main__':
    consume_sentence_explosion()
