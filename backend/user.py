#!/usr/bin/env python3
"""
this module contains a User class
"""


from datetime import datetime, timedelta
import re
import requests

class User:
    """a User class"""
    url = 'https://api.github.com'
    tiers = {'tier1': 'O(n!)', 'tier2': 'O(n)', 'tier3': 'O(1)'}

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

    def account_age(self):
        """calculates and returns age of the account"""
        self.now = datetime.now()
        self.created_at = datetime.strptime(self.user_dict['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        age = self.now - self.created_at
        age_str = str(age)
        age_str_split = re.split('[, :\.]+', age_str)
        age_dhms = age_str_split[0] + ' ' + age_str_split[1] + ' ' + age_str_split[2] + ' hours ' + age_str_split[3] + ' minutes ' + age_str_split[4] + ' seconds'
        return age_dhms

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

    def tier(self):
        """returns the tier of the user"""
        acc_age_str_split = self.account_age.split()
        days_old = acc_age_str_split[0]
        if self.followers > 4 and self.public_repos > 10 and int(days_old) > 180:
            return User.tiers['tier3']
        elif self.followers > 0 and self.public_repos > 4 and int(days_old) > 90:
            return User.tiers['tier2']
        else:
            return User.tiers['tier1']

    def avatar_url(self):
        """returns url of user's avatar"""
        return self.user_dict['avatar_url']

    def following(self):
        """returns number of users the user is following"""
        return self.user_dict['following']

    def bio(self):
        """get users bio"""
        return self.user_dict['bio']

    def hireable(self):
        """status on whether user is hireable"""
        return self.user_dict['hireable']

    def name(self):
        """users name on github"""
        return self.user_dict['name']

    def email(self):
        """get users email"""
        return self.user_dict['email']
