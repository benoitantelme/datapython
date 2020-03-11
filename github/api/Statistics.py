from github import Github
import os
import sys


class Statistics:
    ACCESS_TOKEN = ""
    LANGUAGES = ["Java", "JavaScript", "C", "C++", "Python", "Go", "Rust"]

    def get_token(self) -> str:
        abs_path = sys.path[0]
        base_name = os.path.dirname(abs_path)
        resources_path = os.path.join(base_name, ".." + os.path.sep + "resources" + os.path.sep + "github.token")
        file = open(resources_path, "r")
        self.ACCESS_TOKEN = file.read()
        file.close()

    def get_languages(self):
        github = Github(self.ACCESS_TOKEN)

        for language in self.LANGUAGES:
            query = language + "+in:language"
            result = github.search_repositories(query, 'stars')
            print(f'Found {result.totalCount} repo(s) for ' + language)
            # for repo in result:
            #     print(repo.clone_url)


stat = Statistics()
stat.get_token()
print("Your token is " + stat.ACCESS_TOKEN)
stat.get_languages()

