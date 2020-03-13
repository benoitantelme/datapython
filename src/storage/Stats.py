from collections import defaultdict


class Stats:
    MOST_STARRED = defaultdict(list)
    LANGUAGES = ["Java", "JavaScript", "C", "C++", "Python", "Go", "Rust"]

    def add_repo(self, language, repo):
        self.MOST_STARRED[language].append(repo)
        print("Stats length for " + language + " is " + str(len(self.MOST_STARRED[language])))

    def print(self):
        print(self.LANGUAGES)
