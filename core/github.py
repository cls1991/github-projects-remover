# coding: utf8

"""
   simple github api v3 test, just for fun!
"""

import pprint

import requests


class GithubSample:
    def __init__(self, personal_access_token):
        self.personal_access_token = personal_access_token

    def query_api_info(self):
        api_url = 'https://api.github.com?access_token=%s' % self.personal_access_token
        return requests.get(api_url).json()

    def query_user_info(self, userid):
        user_url = 'https://api.github.com/users/%s?access_token=%s' % (userid, self.personal_access_token)
        return requests.get(user_url).json()

    def query_user_repos(self, userid):
        repos_url = 'https://api.github.com/users/%s/repos?type=fork&access_token=%s' % (
            userid, self.personal_access_token)
        return requests.get(repos_url).json()

    def query_repo_info(self, userid, repo):
        repo_url = 'https://api.github.com/repos/%s/%s' % (userid, repo)
        return requests.get(repo_url).json()


def pretty_print(data):
    """
    pretty print json data
    :param data:
    :return:
    """
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
