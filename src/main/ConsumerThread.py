from src.kafka.StatsConsumer import StatsConsumer
from src.storage.Stats import Stats
from threading import Thread


class ConsumerThread(Thread):
    def __init__(self, s: Stats):
        super().__init__()
        self.consumer = StatsConsumer()
        self.stats = s

    def run(self):
        self.consumer.wait_for_stats(self.stats)
