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
        resp = requests.get(api_url)
        if resp.status_code != 200:
            return {}
        return resp.json()

    def query_user_info(self, userid):
        user_url = 'https://api.github.com/users/%s?access_token=%s' % (userid, self.personal_access_token)
        resp = requests.get(user_url)
        if resp.status_code != 200:
            return {}
        return resp.json()

    def query_user_repos(self, userid, page=1, per_page=20):
        repos_url = 'https://api.github.com/users/%s/repos?page=%d&per_page=%d&access_token=%s' % (
            userid, page, per_page, self.personal_access_token)
        resp = requests.get(repos_url)
        if resp.status_code != 200:
            return []
        return resp.json()

    def query_repo_info(self, userid, repo):
        repo_url = 'https://api.github.com/repos/%s/%s' % (userid, repo)
        resp = requests.get(repo_url)
        if resp.status_code != 200:
            return {}
        return requests.get(repo_url).json()

    def star_repo(self, owner, repo):
        star_repo_url = 'https://api.github.com/user/starred/%s/%s?access_token=%s' % (
            owner, repo, self.personal_access_token)
        return requests.put(star_repo_url).status_code

    def remove_repo(self, userid, repo):
        remove_repo_url = 'https://api.github.com/repos/%s/%s?access_token=%s' % (
            userid, repo, self.personal_access_token)
        return requests.delete(remove_repo_url).status_code


def pretty_print(data):
    """
    pretty print json data
    :param data:
    :return:
    """
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
