#!/usr/bin/python
# -*- coding: utf8 -*-
import json
import unittest
import requests

__author__ = 'enginebai'

ROOT = "http://localhost:5000/"


class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.users = (
        "sitapati", "enginebai", "101", "mobiscroll", "richard.yang.uw", "tzhongg", "jon.moore", "JonDeng",
        "waymo", "quincylarson", "benjaminhardy", "jsaito", "lindacaroll", "jasonfried")

    def test_user_api(self):
        for user in self.users:
            print("1. Requesting", user)
            url = "{}@{}".format(ROOT, user)
            req = requests.get(url)
            self.assertEqual(req.status_code, 200)

    def test_post_api(self):
        url = ROOT + "top"
        print("2. Requesting", url)
        req = requests.get(url)
        self.assertEqual(req.status_code, 200)
        response_list = json.loads(req.text)
        for post in response_list:
            print("2-1. Requesting", post["url"])
            r = requests.get(post["url"])
            self.assertEqual(r.status_code, 200)

        for user in self.users:
            url = "{}@{}/posts".format(ROOT, user)
            print("2-1. Requesting", url)
            user_req = requests.get(url)
            self.assertEqual(user_req.status_code, 200)
            response_list = json.loads(user_req.text)
            for post in response_list:
                print("2-2. Requesting", post["url"])
                r = requests.get(post["url"])
                self.assertEqual(r.status_code, 200)

    def test_post_detail(self):
        for user in self.users:
            print("3. Requesting", user)
            req = requests.get("{}@{}/posts".format(ROOT, user))
            self.assertEqual(req.status_code, 200)
            post_list = json.loads(req.text)
            for post in post_list:
                url = "{}post?u={}".format(ROOT, post["url"])
                print("3-1. Requesting", url)
                r = requests.get(url)
                self.assertEqual(r.status_code, 200)

    def test_publication_api(self):
        for user in self.users:
            print("4. Requesting", user)
            url = "{}@{}".format(ROOT, user)
            user_req = requests.get(url)
            self.assertEqual(user_req.status_code, 200)
            user_dict = json.loads(user_req.text)
            if "publications" in user_dict:
                publication_list = user_dict["publications"]
                for pub in publication_list:
                    self.assertIn("url", pub)
                    print("4-1. Requesting", pub["url"])
                    pub_req = requests.get(pub["url"])
                    self.assertEqual(pub_req.status_code, 200)


def test_post_api(username=None):
    url = ROOT + "top"
    if username is not None and username:
        url = ROOT + "@{username}/posts".format(username=username)
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
    req = requests.get("{}@{}".format(ROOT, username))
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


def test_post_detail_api(username):
    url = ROOT + "@{username}/posts".format(username=username)
    print("Test post detail API from " + url)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        post_list = json.loads(req.text)
        for post_dict in post_list:
            print("Get post detail from " + post_dict["title"], post_dict["url"])
            post_req = requests.get(ROOT + "post?u={url}".format(url=post_dict["url"]))
            if post_req.status_code != requests.codes.ok:
                raise Exception(post_dict["url"], post_req.status_code)


def regression_test():
    ok, fail = test_post_api()
    print(ok, fail)
    users = ("sitapati", "enginebai", "101", "mobiscroll", "richard.yang.uw", "tzhongg", "jon.moore", "JonDeng",
             "waymo", "quincylarson", "benjaminhardy", "jsaito", "lindacaroll", "jasonfried")
    for u in users:
        test_post_detail_api(u)
        # test_user_api(u)
        # ok, fail = test_posts_from_user_interest_tags(u)
        # ok, fail = test_post_api(u)
        # if fail > 0:
        #     raise Exception(u)
        # print(ok, fail)


if __name__ == "__main__":
    # regression_test()
    unittest.main()
