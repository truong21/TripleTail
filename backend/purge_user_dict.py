#!/usr/bin/python3
import sys
import requests
from pprint import pprint

filter = requests.get("https://api.github.com/users/" + sys.argv[1], auth=(sys.argv[1], sys.argv[2]))
filter = {k: v for k, v in filter.json().items() if k in ['followers', 'avatar_url', 'email', 'created_at', 'following', 'bio', 'hireable', 'name']}
pprint(filter)
