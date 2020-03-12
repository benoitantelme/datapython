from kafka import KafkaConsumer
from json import loads
import jsonpickle
from src.storage.Stats import Stats


class StatsConsumer:
    consumer = KafkaConsumer(
        'github_stats',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    def wait_for_stats(self, stats: Stats):
        print("Waiting for stats")
        for message in self.consumer:
            message = message.value
            print('{} received'.format(message))
            for x, y in message.items():
                stats.add_repo(x, jsonpickle.decode(y))
