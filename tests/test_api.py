#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json
import unittest

import requests

ROOT = "http://localhost:5000/"


def test_user_api(username):
    url = ROOT + "{}".format(username)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print(req.status_code)


def test_post_api(username=None):
    url = ROOT + "top"
    if username is not None and username:
        url = ROOT + "{username}/posts".format(username=username)
    req = requests.get(url)
    ok = 0
    fail = 0
    if req.status_code == requests.codes.ok:
        response_list = json.loads(req.text)
        for post in response_list:
            r = requests.get(post["url"])
            print(post["title"])
            print(r.status_code, post["url"])
            if r.status_code == requests.codes.ok:
                ok += 1
            else:
                fail += 1
    else:
        print(req.status_code)
    return ok, fail


def test_posts_from_user_interest_tags(username):
    req = requests.get("{}{}".format(ROOT, username))
    ok = 0
    fail = 0
    if req.status_code == requests.codes.ok:
        user_dict = json.loads(req.text)
        print(user_dict)
        test_keys = ("interest_tags", "author_tags")
        for key in test_keys:
            if key in user_dict and user_dict[key]:
                interest_tags = user_dict[key]
                for tag_dict in interest_tags:
                    print("Send request to {} tags [{}]".format(key, tag_dict))
                    url = "{}tags/{}".format(ROOT, tag_dict["unique_slug"])
                    print("Requsting " + url)
                    search_by_tag_req = requests.get(url)
                    if search_by_tag_req.status_code == requests.codes.ok:
                        print(search_by_tag_req.text)
                        posts_list = json.loads(search_by_tag_req.text)
                        print(posts_list)
                        for post in posts_list:
                            post_req = requests.get(post["url"])
                            if post_req.status_code != requests.codes.ok:
                                fail += 1
                                raise Exception(tag_dict, post["url"])
                            else:
                                ok += 1
                                print(post_req.status_code, post["title"], post["url"])
    return ok, fail


if __name__ == "__main__":
    # ok, fail = test_post_api()
    # print(ok, fail)
    # https://uxplanet.org/@101
    # https://blog.magikcraft.io/@sitapati
    users = ("sitapati", "enginebai", "101", "mobiscroll", "richard.yang.uw", "tzhongg", "jon.moore", "JonDeng",
             "waymo", "quincylarson", "benjaminhardy", "jsaito", "lindacaroll", "jasonfried")
    for u in users:
        # test_user_api(u)
        ok, fail = test_posts_from_user_interest_tags(u)
        # ok, fail = test_post_api(u)
        if fail > 0:
            raise Exception(u)
        print(ok, fail)
