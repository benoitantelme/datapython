from main.ConsumerThread import ConsumerThread
from src.kafka.StatsConsumer import StatsConsumer
from src.storage.Stats import Stats
from time import sleep

# setup storage
stats = Stats()

# setup kafka consumer
consumer = StatsConsumer()

# start listening thread
t = ConsumerThread(consumer, stats)
t.start()

# wait and print
print("Server before sleep")
sleep(30)
print("Server After sleep")
stats.print()
print("After stats print")

