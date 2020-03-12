from collections import defaultdict
from github import Github
import os
import sys


class StatsService:
    ACCESS_TOKEN = ""
    LANGUAGES = ["Java", "JavaScript", "C", "C++", "Python", "Go", "Rust"]
    MOST_STARRED = defaultdict(list)

    def get_token(self) -> str:
        abs_path = sys.path[0]
        base_name = os.path.dirname(abs_path)
        resources_path = os.path.join(base_name, ".." + os.path.sep + "resources" + os.path.sep + "github.token")
        file = open(resources_path, "r")
        self.ACCESS_TOKEN = file.read()
        file.close()

    def get_most_starred_repos(self):
        github = Github(self.ACCESS_TOKEN)

        for language in self.LANGUAGES:
            query = language + "+in:language&sort=stars&order=desc"
            result = github.search_repositories(query, 'stars')
            for repo in result[:10]:
                self.MOST_STARRED[language].append(repo)

