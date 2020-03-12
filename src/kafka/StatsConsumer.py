from kafka import KafkaConsumer
from json import loads


class StatsConsumer:
    consumer = KafkaConsumer(
        'github_stats',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    def wait_for_stats(self):
        print("Waiting for stats")
        for message in self.consumer:
            message = message.value
            print('{} received'.format(message))
        print("Stats read")
