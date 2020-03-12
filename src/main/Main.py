from src.github.api.StatsService import StatsService
from src.storage.Stats import Stats

stat_service = StatsService()
stat_service.setup()

stats = Stats()
for language in stats.LANGUAGES:
    stats.MOST_STARRED[language] = stat_service.get_most_starred_repos(language)

print(stats.MOST_STARRED)

