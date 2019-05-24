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

    def __init__(self, token):
        """instantiation of User class object"""
        self.token = token
        self.user_dict = self.user_dict()
        self.username = self.username()
        self.public_repos = self.public_repos()
        self.followers = self.followers()
        self.account_age = self.account_age()
        self.readme_pct = self.readme_pct()
        self.tier = self.tier()
        self.avatar_url = self.avatar_url()
        self.following = self.following()
        self.bio = self.bio()
        self.hireable = self.hireable()
        self.name = self.name()
        self.email = self.email()
        self.commits = ((self.public_repos + self.followers) * 110)

    def user_dict(self):
        """creates dictionary of user's info"""
        header = {'Authorization': 'Bearer {}'.format(self.token)}
        r = requests.get('https://api.github.com/user', headers=header)
        allowed = ['public_repos', 'followers']
        return r.json()

    def public_repos(self):
        """returns number of public repos of a user"""
        return self.user_dict['public_repos']

    def followers(self):
        """returns number of followers of a user"""
        return self.user_dict['followers']

    def account_age(self):
        """calculates and returns age of the account"""
        self.now = datetime.now()
        self.created_at = datetime.strptime(self.user_dict['created_at'],
                                            "%Y-%m-%dT%H:%M:%SZ")
        age = self.now - self.created_at
        age_str = str(age)
        age_str_split = re.split('[, :\.]*', age_str)
        if len(age_str_split) > 5:
            age_dhms = age_str_split[0] \
                + ' ' + age_str_split[1] \
                + ' ' + age_str_split[2] \
                + ' hours ' + age_str_split[3] \
                + ' minutes ' + age_str_split[4] \
                + ' seconds'
        else:
            age_dhms = '0 days ' \
                + age_str_split[0] \
                + ' hours ' + age_str_split[1] \
                + ' minutes ' + age_str_split[2] \
                + ' seconds'
        return age_dhms

    def readme_pct(self):
        """Returns the percentage of repos that have a README"""
        header = {'Authorization': 'Bearer {}'.format(self.token)}
        repo_list = requests.get('{}/users/{}/repos'
                                 .format(self.url, self.username),
                                 headers=header).json()
        readme_count = 0
        if self.user_dict.get('public_repos') is 0:
            return 0
        for repo in repo_list:
            response = requests.get('{}/repos/{}/{}/readme'
                                    .format(self.url,
                                            self.username,
                                            repo.get('name')),
                                    headers=header)
            if response.status_code == 404:
                pass
            else:
                readme_count += 1
        return '{:.1%}'.format(readme_count/self.user_dict.get('public_repos'))

    def tier(self):
        """returns the tier of the user"""
        acc_age_str_split = self.account_age.split()
        days_old = acc_age_str_split[0]
        if self.followers > 4 and \
                self.public_repos > 10:
            return User.tiers['tier3']
        elif self.followers > 0 and \
                self.public_repos > 4:
            return User.tiers['tier2']
        else:
            return User.tiers['tier1']

    def commits(self):
        """returns number of commits"""
        from bs4 import BeautifulSoup
        from requests import get
        from sys import argv
        
        url = 'https://github.com/{}'.format(self.username)
        url = 'https://github.com/suhearsawho'
        header = {"User-Agent": "Holberton"}
        page = get(url, headers=header)
        soup = BeautifulSoup(page.text, "html.parser")
        resdiv = soup.find_all("h2", {"class": "f4 text-normal mb-2"})
        reslist = []

        for i in resdiv:
            reslist.append(i.text)

        data = reslist[0]
        data = data.split("contributions")
        return data[0].strip()

    def avatar_url(self):
        """returns url of user's avatar"""
        return self.user_dict['avatar_url']

    def username(self):
        """returns username"""
        return self.user_dict['login']

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
    
    def commits(self):
        """get users email"""
        return self.user_dict['commits']

if __name__ == "__main__":
    url = argv[1]
    commits = scrape_commits(url)
