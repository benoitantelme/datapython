from src.github.api.StatsService import StatsService
from src.kafka.StatsProducer import StatsProducer


LANGUAGES = ["Java", "JavaScript", "C", "C++", "Python", "Go", "Rust"]

# setup stats service
stat_service = StatsService()
stat_service.setup()

# setup kafka producer
producer = StatsProducer()

# get repos stats and send them
for language in LANGUAGES:
    producer.send_stats(language, stat_service.get_most_starred_repos(language))

