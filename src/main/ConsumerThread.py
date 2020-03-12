from src.kafka.StatsConsumer import StatsConsumer
from src.storage.Stats import Stats
from threading import Thread


class ConsumerThread(Thread):
    def __init__(self, cons: StatsConsumer, s: Stats):
        super().__init__()
        self.cons = cons
        self.stats = s

    def run(self):
        self.cons.wait_for_stats(self.stats)
