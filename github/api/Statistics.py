from github import Github
import os
import sys


class Statistics:
    ACCESS_TOKEN = ""

    def get_token(self) -> str:
        abs_path = sys.path[0]
        base_name = os.path.dirname(abs_path)
        resources_path = os.path.join(base_name, ".." + os.path.sep + "resources" + os.path.sep + "github.token")
        file = open(resources_path, "r")
        self.ACCESS_TOKEN = file.read()
        file.close()


s = Statistics()
s.get_token()
print(s.ACCESS_TOKEN)
