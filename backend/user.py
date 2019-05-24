#!/usr/bin/env python3
"""
this module contains a User class
"""


import datetime
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

    def 
