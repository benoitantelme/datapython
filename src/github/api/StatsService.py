from github import Github
import os
import sys


class StatsService:
    ACCESS_TOKEN = ""
    service = Github()

    def get_token(self) -> str:
        abs_path = sys.path[0]
        base_name = os.path.dirname(abs_path)
        resources_path = os.path.join(base_name, ".." + os.path.sep + "resources" + os.path.sep + "github.token")
        file = open(resources_path, "r")
        self.ACCESS_TOKEN = file.read()
        file.close()

    def setup(self):
        self.service = Github(self.get_token())
        print("Your token is " + self.ACCESS_TOKEN)

    def get_most_starred_repos(self, language: str) -> list:
        values = []
        query = language + "+in:language&sort=stars&order=desc"
        result = self.service.search_repositories(query, 'stars')
        for repo in result[:10]:
            values.append(repo)
        return values
