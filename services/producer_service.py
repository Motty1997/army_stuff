from kafka_settings.producer import produce


def publish_all_messages(data):
    produce('all_messages', data['email'], data)