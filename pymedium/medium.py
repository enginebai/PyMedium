#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import json

import requests
from pymedium.parser import parse_user, parse_publication, parse_post, parse_post_detail
from pymedium.constant import ROOT_URL, HTML_PARSER, ACCEPT_HEADER, ESCAPE_CHARACTERS


class Medium(object):
    def __init__(self):
        pass

    def get_user_profile(self, username):
        url = "{}@{}/latest".format(ROOT_URL, username)
        return self._send_request(url, parse_user)

    def get_publication_profile(self, publication_name):
        url = "{}{}/latest".format(ROOT_URL, publication_name)
        return self._send_request(url, parse_publication)

    def get_user_posts(self, username):
        pass

    def get_publication_posts(self, publication):
        pass

    def get_top_posts(self):
        pass

    def search_posts_by_tag(self, tag, sort):
        pass

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