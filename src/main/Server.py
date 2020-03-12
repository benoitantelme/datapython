from src.github.api.StatsService import StatsService
from src.storage.Stats import Stats
from src.kafka.StatsConsumer import StatsConsumer
from src.kafka.StatsProducer import StatsProducer

# setup stats service
stat_service = StatsService()
stat_service.setup()


# setup kafka consumer
consumer = StatsConsumer()
consumer.wait_for_stats()


# setup kafka producer
producer = StatsProducer()

# setup storage
stats = Stats()
for language in stats.LANGUAGES:
    producer.send_stats(language, stat_service.get_most_starred_repos(language))

# stats = Stats()
# for language in stats.LANGUAGES:
#     stats.MOST_STARRED[language] = stat_service.get_most_starred_repos(language)
#
# print(stats.MOST_STARRED)
