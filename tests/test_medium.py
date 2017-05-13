#!/usr/bin/python3
# -*- coding: utf8 -*-
import string
import unittest
import random

from pymedium.medium import Medium
from pymedium.model import Sort

__author__ = "Engine Bai"


class TestMedium(unittest.TestCase):
    def setUp(self):
        self.medium = Medium()

    def test_user(self):
        user = "enginebai"
        self.assertIsNotNone(self.medium.get_user_profile(user))
        self.assertIsNone(self.medium.get_user_profile(
            "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))))

    def test_publication(self):
        publication = "dualcores-studio"
        self.assertIsNotNone(self.medium.get_publication_profile(publication))
        self.assertIsNotNone(self.medium.get_publication_posts(publication))

    def test_public_posts(self):
        self.assertIsNotNone(self.medium.get_top_posts())
        self.assertIsNotNone(self.medium.get_posts_by_tag("android"))
        self.assertIsNotNone(self.medium.get_posts_by_tag("android", sort=Sort.LATEST))


if __name__ == "__main__":
    unittest.main()
