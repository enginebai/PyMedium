#!/usr/bin/python
# -*- encoding: utf-8 -*-
import requests
import json

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


if __name__ == "__main__":
    ok, fail = test_post_api()
    print(ok, fail)
    # https://uxplanet.org/@101
    # https://blog.magikcraft.io/@sitapati
    users = ("sitapati", "enginebai", "101", "mobiscroll", "richard.yang.uw", "tzhongg", "jon.moore", "JonDeng",
             "waymo", "quincylarson", "benjaminhardy", "jsaito", "lindacaroll", "jasonfried")
    for u in users:
        test_user_api(u)
        ok, fail = test_post_api(u)
        if fail > 0:
            raise Exception(u)
        print(ok, fail)
