# from time import sleep
from json import dumps
from kafka import KafkaProducer
import jsonpickle


class StatsProducer:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             dumps(x, indent=4).encode('utf-8'))

    def send_stats(self, language: str, repos: list):
        for repo in repos:
            data = {language: jsonpickle.encode(repo)}
        self.producer.send('github_stats', value=data)
