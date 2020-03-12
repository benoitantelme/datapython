from src.github.api.StatsService import StatsService

stat_service = StatsService()
stat_service.get_token()
print("Your token is " + stat_service.ACCESS_TOKEN)
stat_service.get_most_starred_repos()
print(stat_service.MOST_STARRED)



