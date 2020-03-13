from collections import defaultdict
import redis
import pickle


class Stats:
    MOST_STARRED = defaultdict(list)
    conn = redis.Redis()
    LANGUAGES = ["Java", "JavaScript", "C", "C++", "Python", "Go", "Rust"]

    def add_repo(self, language, repo):
        self.MOST_STARRED[language].append(repo)
        print("Stats length for " + language + " is " + str(len(self.MOST_STARRED[language])))
        if len(self.MOST_STARRED[language]) >= 10:
            self.conn.set(language, pickle.dumps(self.MOST_STARRED[language]))
            self.MOST_STARRED.pop(language, None)
            print("Stats Repos added to redis for " + language)

    def print(self):
        for language in self.LANGUAGES:
            print(pickle.loads(self.conn.get(language)))
