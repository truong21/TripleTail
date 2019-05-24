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

    def __init__(self, username, password):
        """instantiation of User class object"""
        self.username = username
        self.password = password
        self.user_dict = self.user_dict()
        if self.user_dict.get('followers') is None:
            self.followers = 0
        else:
            self.followers = self.user_dict.get('followers')
        if self.user_dict.get('avatar_url') is not None:
            self.avatar_url = self.user_dict.get('avatar_url')
        if self.user_dict.get('following') is None:
            self.following = 0
        else:
            self.following = self.user_dict.get('following')
        if self.user_dict.get('bio') is None:
            self.bio = ""
        else:
            self.bio = self.user_dict.get('bio')
        if self.user_dict.get('hireable') is None:
            self.hireable = "No"
        else:
            self.hireable = self.user_dict.get('hireable')
        if self.user_dict.get('name') is not None:
            self.name = self.user_dict.get('name')
        else:
            self.name = "Mysterious stranger"
        if self.user_dict.get('email') is not None:
            self.email = self.user_dict.get('email')
        if self.user_dict.get('public_repos') is None:
            self.public_repos = 0
        else:
            self.public_repos = self.user_dict.get('public_repos')
        self.readme_pct = self.readme_pct()

    def user_dict(self):
        """creates dictionary of user's info"""
        r = requests.get('https://api.github.com/user', auth=(self.username, self.password))
        r_d = r.json()
        user_info = {k: v for k, v in r_d.items() if k in ['followers',
                                                 'avatar_url',
                                                 'email',
                                                 'created_at',
                                                 'following', 'bio',
                                                 'hireable',
                                                 'name',
                                                 'public_repos']}
        return user_info

    def account_age(self):
        """calculates and returns age of the account"""
        self.now = datetime.now()
        self.created_at = datetime.strptime(self.user_dict.get('created_at'), "%Y-%m-%dT%H:%M:%SZ")
        age = self.now - self.created_at
        age_str = str(age)
        age_str_split = re.split('[, :\.]*', age_str)
        if len(age_str_split) > 5:
            age_dhms = age_str_split[0] + ' ' + age_str_split[1] + ' ' + age_str_split[2] + ' hours ' + age_str_split[3] + ' minutes ' + age_str_split[4] + ' seconds'
        else:
            age_dhms = '0 days ' + age_str_split[0] + ' hours ' + age_str_split[1] + ' minutes ' + age_str_split[2] + ' seconds'
        self.age = age_dhms
        return age_dhms

    def readme_pct(self):
        """Returns the percentage of repos that have a README"""
        if self.user_dict.get('public_repos') is None or self.user_dict.get('public_repos') == 0:
            return '0.0%'
        repo_list = requests.get('{}/users/{}/repos'.format(self.url, self.username), auth=(self.username, self.password)).json()
        readme_count = 0
        for repo in repo_list:
            response = requests.get('{}/repos/{}/{}/readme'.format(self.url, self.username, repo.get('name')), auth=(self.username, self.password))
            if response.status_code == 404:
                pass
            else:
                readme_count += 1
        return '{:.1%}'.format(readme_count/self.user_dict.get('public_repos'))

    def tier_finder(self):
        """returns the tier of the user"""
        acc_age_str_split = self.account_age().split()
        days_old = acc_age_str_split[0]
        if self.followers > 4 and self.public_repos > 10 and int(days_old) > 180:
            return User.tiers['tier3']
        elif self.followers > 0 and self.public_repos > 4 and int(days_old) > 90:
            self.tier =  User.tiers['tier2']
        else:
            self.tier =  User.tiers['tier1']
        return self.tier
