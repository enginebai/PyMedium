#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import json

import requests
from pymedium.parser import parse_user, parse_publication, parse_post, parse_post_detail
from pymedium.constant import ROOT_URL, ACCEPT_HEADER, ESCAPE_CHARACTERS, COUNT
from pymedium.model import Sort


class Medium(object):
    def __init__(self):
        pass

    def get_user_profile(self, username):
        url = "{}@{}/latest".format(ROOT_URL, username)
        return self._send_request(url, parse_user)

    def get_publication_profile(self, publication_name):
        url = "{}{}/latest".format(ROOT_URL, publication_name)
        return self._send_request(url, parse_publication)

    def get_user_posts(self, username, n=COUNT):
        return self._send_post_request(ROOT_URL + "@{0}/latest?limit={count}".format(username, count=n))

    def get_publication_posts(self, publication_name, n=COUNT):
        return self._send_post_request(ROOT_URL + "{0}/latest?limit={count}".format(publication_name, count=n))

    def get_top_posts(self, n=COUNT):
        return self._send_post_request(ROOT_URL + "browse/top?limit={count}".format(count=n))

    def get_posts_by_tag(self, tag, n=COUNT, sort=Sort.TOP):
        url = "{}tag/{tag}".format(ROOT_URL, tag=tag)
        if sort == Sort.LATEST:
            url += "/latest"
        url += "?limit={}".format(n)
        return self._send_post_request(url)

    def parse_post_content(self, url):
        pass

    @staticmethod
    def _send_request(url, parse_function):
        req = requests.get(url, headers=ACCEPT_HEADER)
        print(url, req.status_code)
        if req.status_code == requests.codes.ok:
            return parse_function(json.loads(req.text.replace(ESCAPE_CHARACTERS, "").strip()))
        else:
            return None

    @staticmethod
    def _send_post_request(url):
        return Medium._send_request(url, parse_post)
