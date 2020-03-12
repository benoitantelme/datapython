from collections import defaultdict


class Stats:
    MOST_STARRED = defaultdict(list)

    def add_repo(self, language, repo):
        self.MOST_STARRED[language].append(repo)

    def print(self):
        print(self.MOST_STARRED)
