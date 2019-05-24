#!/usr/bin/env python3
"""
this module contains a User class
"""


import datetime
import requests

class User:
    """a User class"""
    url = 'https://api.github.com'

    def __init__(self, *args, **kwargs):
        """instantiation of User class object"""
        if kwargs:
            self.__set_attributes(kwargs)
        self.user_dict = {}

    @property
    def __set_attributes(self, attr_dict):
        """sets attributes for a User object"""
        for attr, val in attr_dict.items():
            setattr(self, attr, val)

    @property
    def user_dict(self):
        """creates dictionary of user's info"""
        usern = self.username
        passw = self.password
        r = requests.get('https://api.github.com/user', auth=(usern, passw))
        self.user_dict = r.json()

    def public_repos(self):
        """returns number of public repos of a user"""
        return self.user_dict['public_repos']

    def followers(self):
        """returns number of followers of a user"""
        return self.user_dict['followers']

    @property
    def readme_pct(self):
        """Returns the percentage of repos that have a README"""
        repo_list = requests.get('{}/users/{}/repos'.format(url, self.username), auth=(self.username, self.password))
        readme_count = 0
        for repo in repo_list:
            response = requests.get('{}/repos/{}/{}/readme'.format(url, self.username, repo.get('name')), auth=(self.username, self.password))
            if response.status_code == 404:
                pass
            else:
                readme_count += 1
        return '{:.1%}'.format(readme_count/self.user_dict.get('public_repos'))
