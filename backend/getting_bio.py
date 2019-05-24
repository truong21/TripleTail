#!/usr/bin/python3
import requests
import sys

print("{} {} {}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
print('hi')
r = requests.get('https://api.github.com/users/' + sys.argv[1], auth=(sys.argv[2], sys.argv[3]))
user_dict = r.json()
bio = user_dict['bio']
hireable = user_dict['hireable']
name = user_dict['name']
email = user_dict['email']
print(email)
