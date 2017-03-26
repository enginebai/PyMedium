#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json
import unittest

import requests

LOCAL_HOST = "http://localhost:5000/"


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        print("Request top posts...")
        self.top_req = requests.get(LOCAL_HOST + "top")
        print("Request user profile...")
        self.user_req = requests.get(LOCAL_HOST + "@enginebai")
        print("Request user posts...")
        self.user_post_req = requests.get(LOCAL_HOST + "@enginebai/posts")
        print("Request one user post...")
        self.user_one_post_req = requests.get(LOCAL_HOST + "@enginebai/posts?n=1")
        print("Request tag top posts...")
        self.tag_top_req = requests.get(LOCAL_HOST + "tags/android")
        print("Request tag latest posts...")
        self.tag_latest_req = requests.get(LOCAL_HOST + "tags/android/latest")
        print("Request post detail...")
        self.post_detail_req = requests.get(LOCAL_HOST + "post?u={url}".format(
            url="https://medium.com/dualcores-studio/python-x-%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2-c30ffda0ad78"))
        print("Request publication profile...")
        self.publication_req = requests.get(LOCAL_HOST + "dualcores-studio")
        print("Request publication profile with custom URL...")
        self.publication_req_custom_url = requests.get(LOCAL_HOST + "ux-planet")
        print("Request publication posts with custom URL...")
        self.publication_post_req_custom_url = requests.get(LOCAL_HOST + "ux-planet/posts")

    def test_apis_ok(self):
        self.assertEqual(self.top_req.status_code, 200)
        self.assertEqual(self.user_req.status_code, 200)
        self.assertEqual(self.user_post_req.status_code, 200)
        self.assertEqual(self.user_one_post_req.status_code, 200)
        self.assertEqual(self.tag_top_req.status_code, 200)
        self.assertEqual(self.tag_latest_req.status_code, 200)
        self.assertEqual(self.post_detail_req.status_code, 200)
        self.assertEqual(self.publication_req.status_code, 200)
        self.assertEqual(self.publication_req_custom_url.status_code, 200)
        self.assertEqual(self.publication_post_req_custom_url.status_code, 200)


class ApiResponseCase(unittest.TestCase):

    def setUp(self):
        print("Request user profile and publication...")
        self.user_req = requests.get(LOCAL_HOST + "@enginebai")
        self.pub_req = requests.get(LOCAL_HOST + "dualcores-studio")

    def test_user_api(self):
        user_dict = json.loads(self.user_req.text)
        self.assertIn("username", user_dict.keys())
        self.assertEqual(user_dict["username"], "enginebai")

    def test_publication_api(self):
        publication_dict = json.loads(self.pub_req.text)
        self.assertIn("url", publication_dict)
        self.assertEqual(publication_dict["url"], "https://medium.com/dualcores-studio")


if __name__ == "__main__":
    test_classes = [ApiTestCase, ApiResponseCase]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    full_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner()
    results = runner.run(full_suite)
