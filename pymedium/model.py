#!/usr/bin/python
# -*- coding: utf8 -*-
from enum import Enum

__author__ = 'enginebai'


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, name):
        self._display_name = name

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        self._avatar = avatar

    @property
    def bio(self):
        return self._bio()

    @bio.setter
    def bio(self, bio):
        self._bio = bio

    @property
    def twitter(self):
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        self._twitter = twitter

    @property
    def facebook_user_id(self):
        return self._facebook_user_id

    @facebook_user_id.setter
    def facebook_user_id(self, facebook):
        self._facebook_user_id = facebook

    @property
    def publications(self):
        return self._publications

    @publications.setter
    def publications(self, publications):
        self._publications = publications

    @property
    def following_count(self):
        return self._following_count

    @following_count.setter
    def following_count(self, count):
        self._following_count = count

    @property
    def followedby_count(self):
        return self._followedby_count

    @followedby_count.setter
    def followedby_count(self, count):
        self._followedby_count = count

    @property
    def interest_tags(self):
        return self._interest_tags

    @interest_tags.setter
    def interest_tags(self, tags):
        self._interest_tags = tags

    @property
    def author_tags(self):
        return self._author_tags

    @author_tags.setter
    def author_tags(self, tags):
        self._author_tags = tags


class Post:
    def __init__(self, post_id):
        self.post_id = post_id

    # @property
    # def unique_slug(self):
    #     return self._unique_slug
    #
    # @unique_slug.setter
    # def unique_slug(self, slug):
    #     self._unique_slug = slug

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def post_date(self):
        return self._post_date

    @post_date.setter
    def post_date(self, date):
        self._post_date = date

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def recommend_count(self):
        return self._recommend_count

    @recommend_count.setter
    def recommend_count(self, count):
        self._recommend_count = count

    @property
    def response_count(self):
        return self._response_count

    @response_count.setter
    def response_count(self, count):
        self._response_count = count

    @property
    def read_time(self):
        return self._read_time

    @read_time.setter
    def read_time(self, time):
        self._read_time = time

    @property
    def word_count(self):
        return self._word_count

    @word_count.setter
    def word_count(self, count):
        self._word_count = count

    @property
    def image_count(self):
        return self._image_count

    @image_count.setter
    def image_count(self, count):
        self._image_count = count

    @property
    def preview_image(self):
        return self._preview_image

    @preview_image.setter
    def preview_image(self, image):
        self._preview_image = image

    @property
    def post_tags(self):
        return self._post_tags

    @post_tags.setter
    def post_tags(self, tags):
        self._post_tags = tags


class Publication:
    def __init__(self, publication_id):
        self.publication_id = publication_id

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, name):
        self._display_name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def creator_user_id(self):
        return self._creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, user_id):
        self._creator_user_id = user_id

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logo):
        self._logo = logo

    @property
    def follower_count(self):
        return self._follower_count

    @follower_count.setter
    def follower_count(self, count):
        self._follower_count = count

    @property
    def post_count(self):
        return self._post_count

    @post_count.setter
    def post_count(self, count):
        self._post_count = count


class Tag:
    @property
    def unique_slug(self):
        return self._unique_slug

    @unique_slug.setter
    def unique_slug(self, slug):
        self._unique_slug = slug

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def post_count(self):
        return self._post_count

    @post_count.setter
    def post_count(self, count):
        self._post_count = count

    @property
    def follower_count(self):
        return self._follower_count

    @follower_count.setter
    def follower_count(self, count):
        self._follower_count = count

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image


class Image:
    def __init__(self, image_id):
        self.image_id = image_id

    @property
    def original_height(self):
        return self._original_height

    @original_height.setter
    def original_height(self, height):
        self._original_height = height

    @property
    def original_width(self):
        return self._original_width

    @original_width.setter
    def original_width(self, width):
        self._original_width = width

    # @property
    # def url(self):
    #     return self._url
    #
    # @url.setter
    # def url(self, url):
    #     self._url = url


class OutputFormat(Enum):
    PLAIN_TEXT = "text"
    JSON = "json"
    HTML = "html"
    MARKDOWN = "md"


def to_dict(model):
    return dict((get_key(key), value)
                for key, value in model.__dict__.items()
                if not callable(value) and not key.startswith("__"))

def get_key(key):
    return key.replace("_", "", 1) if key.startswith("_") else key