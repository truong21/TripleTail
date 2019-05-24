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

    def __init__(self, username):
        """instantiation of User class object"""
        self.user_dict = self.user_dict(username)

        self.followers = self.user_dict['followers']
        self.avatar_url = self.user_dict['avatar_url']
        self.following = self.user_dict['following']
        self.bio = self.user_dict['bio']
        self.hireable = self.user_dict['hireable']
        self.name = self.user_dict['name']
        self.email = self.user_dict['email']
        self.public_repos = self.user_dict['public_repos']

        self.readme_pct = self.readme_pct(self.user_dict, User.url, username)

        print(self.readme_pct)
        self.tier = self.tier()
        print(self.tier())
        self.account_age = self.account_age()
        print(self.account_age())



    def user_dict(self, username):
        """creates dictionary of user's info"""
        r = requests.get('https://api.github.com/users/{}'.format(username))
        r = r.json()
        print(r)
        r = {k: v for k, v in r.items() if k in ['followers',
                                                 'avatar_url',
                                                 'email',
                                                 'created_at',
                                                 'following', 'bio',
                                                 'hireable',
                                                 'name',
                                                 'public_repos']}
        return r



    def account_age(self):
        """calculates and returns age of the account"""
        self.now = datetime.now()
        self.created_at = datetime.strptime(self.user_dict['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        age = self.now - self.created_at
        age_str = str(age)
        age_str_split = re.split('[, :\.]*', age_str)
        if len(age_str_split) > 5:
            age_dhms = age_str_split[0] + ' ' + age_str_split[1] + ' ' + age_str_split[2] + ' hours ' + age_str_split[3] + ' minutes ' + age_str_split[4] + ' seconds'
        else:
            age_dhms = '0 days ' + age_str_split[0] + ' hours ' + age_str_split[1] + ' minutes ' + age_str_split[2] + ' seconds'
        return age_dhms


    def readme_pct(self, user_dict, url, username):
        """Returns the percentage of repos that have a README"""
        repo_list = requests.get('{}/users/{}/repos'.format(url, username)).json()
        readme_count = 0
        if user_dict['public_repos'] is 0:
            return 0
        for repo in repo_list:
            response = requests.get('{}/repos/{}/{}/readme'.format(url, username, user_dict['name']))
            if response.status_code == 404:
                pass
            else:
                readme_count += 1
        return '{:.1%}'.format(readme_count/user_dict['public_repos'])


"""
    def tier(self):
returns the tier of the user
        acc_age_str_split = self.account_age.split()
        days_old = acc_age_str_split[0]
        if self.followers > 4 and self.public_repos > 10 and int(days_old) > 180:
            return User.tiers['tier3']
        elif self.followers > 0 and self.public_repos > 4 and int(days_old) > 90:
            return User.tiers['tier2']
        else:
            return User.tiers['tier1']
"""
