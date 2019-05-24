#!/usr/bin/env python3
"""
this module contains a User class
"""


from datetime import datetime, timedelta
import re
import requests

class User:
    """a User class"""
    def __init__(self, *args, **kwargs):
        """instantiation of User class object"""
        if kwargs:
            self.__set_attributes(kwargs)
        self.user_dict = {}

    def __set_attributes(self, attr_dict):
        """sets attributes for a User object"""
        for attr, val in attr_dict.items():
            setattr(self, attr, val)

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

    def account_age(self):
        """calculates and returns age of the account"""
        self.now = datetime.now()
        self.created_at = datetime.strptime(self.user_dict['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        age = self.now - self.created_at
        age_str = str(age)
        age_str_split = re.split('[, :\.]+', age_str)
        age_dhms = age_str_split[0] + ' ' + age_str_split[1] + ' ' + age_str_split[2] + ' hours ' + age_str_split[3] + ' minutes ' + age_str_split[4] + ' seconds'
        return age_dhms
