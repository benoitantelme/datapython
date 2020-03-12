from time import sleep
from json import dumps
from kafka import KafkaProducer


class StatsProducer:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))

    def send_stats(self, language: str, repos: list):
        data = {language: repos}
        self.producer.send('github_stats', value=data)
        sleep(1)
