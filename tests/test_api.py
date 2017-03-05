#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json
import unittest

import requests

ROOT = "http://localhost:5000/"


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        print("Request top posts...")
        self.top_req = requests.get(ROOT + "top")
        print("Request user profile...")
        self.user_req = requests.get(ROOT + "enginebai")
        print("Request user posts...")
        self.user_post_req = requests.get(ROOT + "enginebai/posts")
        print("Request one user post...")
        self.user_one_post_req = requests.get(ROOT + "enginebai/posts?n=1")
        print("Request tag top posts...")
        self.tag_top_req = requests.get(ROOT + "tags/android")
        print("Request tag latest posts...")
        self.tag_latest_req = requests.get(ROOT + "tags/android/latest")

    def test_apis_ok(self):
        self.assertEqual(self.top_req.status_code, 200)
        self.assertEqual(self.user_req.status_code, 200)
        self.assertEqual(self.user_post_req.status_code, 200)
        self.assertEqual(self.user_one_post_req.status_code, 200)
        self.assertEqual(self.tag_top_req.status_code, 200)
        self.assertEqual(self.tag_latest_req.status_code, 200)


class ApiResponseCase(unittest.TestCase):

    def setUp(self):
        print("Request user profile...")
        self.user_req = requests.get(ROOT + "enginebai")

    def test_user_api(self):
        user_dict = json.loads(self.user_req.text)
        self.assertIn("username", user_dict.keys())
        self.assertEqual(user_dict["username"], "enginebai")


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
