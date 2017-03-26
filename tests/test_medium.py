#!/usr/bin/python3
# -*- coding: utf8 -*-
import string
import unittest
import random

from pymedium.medium import Medium

__author__ = "Engine Bai"

class TestMedium(unittest.TestCase):
    def setUp(self):
        self.medium = Medium()

    def test_get_user(self):
        self.assertIsNotNone(self.medium.get_user_profile("enginebai"))
        self.assertIsNone(self.medium.get_user_profile(
            "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))))
        self.assertIsNotNone(self.medium.get_publication_profile("dualcores-studio"))


if __name__ == "__main__":
    unittest.main()
