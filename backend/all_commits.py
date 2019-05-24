#!/usr/bin/python3
"""get all commits for all time"""
import requests
import sys

repo_name = sys.argv[1]
user_name = sys.argv[2]
print("{} {}".format(repo_name, user_name))
"""
all_repos = "https://api.github.com/users/" + user_name + "/repos"
end = user_name + "/" + repo_name
all_commits = "https://api.github.com/repos/" + end + "/commits"
r = requests.get(url).json()
"""
