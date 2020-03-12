from src.kafka.StatsConsumer import StatsConsumer
from src.storage.Stats import Stats
from time import sleep


# setup storage
stats = Stats()

# setup kafka consumer
consumer = StatsConsumer()
consumer.wait_for_stats(stats)

sleep(100)
stats.print()
