from main.ConsumerThread import ConsumerThread
from src.storage.Stats import Stats
from time import sleep

# setup storage
stats = Stats()

# start consumer thread
t = ConsumerThread(stats)
t.start()

# wait and print
print("Server before sleep")
sleep(30)
print("Server After sleep")
stats.print()
print("After stats print")

