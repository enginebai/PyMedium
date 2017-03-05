#!/usr/bin/python
# -*- coding: utf8 -*-
from enum import Enum

__author__ = 'enginebai'


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        self.username = username

    @property
    def display_name(self):
        return self.display_name

    @display_name.setter
    def display_name(self, name):
        self.display_name = name

    @property
    def avatar(self):
        return self.avatar

    @avatar.setter
    def avatar(self, avatar):
        self.avatar = avatar

    @property
    def bio(self):
        return self.bio()

    @bio.setter
    def bio(self, bio):
        self.bio = bio

    @property
    def twitter(self):
        return self.twitter

    @twitter.setter
    def twitter(self, twitter):
        self.twitter = twitter

    @property
    def facebook(self):
        return self.facebook

    @facebook.setter
    def facebook(self, facebook):
        self.facebook = facebook

    @property
    def publications(self):
        return self.publications

    @publications.setter
    def publications(self, publications):
        self.publications = publications

    @property
    def following_count(self):
        return self.following_count

    @following_count.setter
    def following_count(self, count):
        self.following_count = count

    @property
    def followedby_count(self):
        return self.followedby_count

    @followedby_count.setter
    def followedby_count(self, count):
        self.followedby_count = count

    @property
    def interest_tags(self):
        return self.interest_tags

    @interest_tags.setter
    def interest_tags(self, tags):
        self.interest_tags = tags

    @property
    def author_tags(self):
        return self.author_tags

    @author_tags.setter
    def author_tags(self, tags):
        self.author_tags = tags


class Post:
    def __init__(self, post_id):
        self.post_id = post_id

    @property
    def unique_slug(self):
        return self.unique_slug

    @unique_slug.setter
    def unique_slug(self, slug):
        self.unique_slug = slug

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, title):
        self.title = title

    @property
    def post_date(self):
        return self.post_date

    @post_date.setter
    def post_date(self, date):
        self.post_date = date

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, url):
        self.url = url

    @property
    def recommend_count(self):
        return self.recommend_count

    @recommend_count.setter
    def recommend_count(self, count):
        self.recommend_count = count

    @property
    def response_count(self):
        return self.response_count

    @response_count.setter
    def response_count(self, count):
        self.response_count = count

    @property
    def read_time(self):
        return self.read_time

    @read_time.setter
    def read_time(self, time):
        self.read_time = time

    @property
    def word_count(self):
        return self.word_count

    @word_count.setter
    def word_count(self, count):
        self.word_count = count

    @property
    def image_count(self):
        return self.image_count

    @image_count.setter
    def image_count(self, count):
        self.image_count = count

    @property
    def preview_image(self):
        return self.preview_image

    @preview_image.setter
    def preview_image(self, image):
        self.preview_image = image

    @property
    def post_tags(self):
        return self.post_tags

    @post_tags.setter
    def post_tags(self, tags):
        self.post_tags = tags


class Publication:
    def __init__(self, publication_id):
        self.publication_id = publication_id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def unique_slug(self):
        return self.unique_slug

    @unique_slug.setter
    def unique_slug(self, slug):
        self.unique_slug = slug

    @property
    def creator_user_id(self):
        return self.creator_user_id

    @creator_user_id.setter
    def creator_user_id(self, user_id):
        self.creator_user_id = user_id

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.description = description

    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, image):
        self.image = image

    @property
    def logo(self):
        return self.logo

    @logo.setter
    def logo(self, logo):
        self.logo = logo

    @property
    def follower_count(self):
        return self.follower_count

    @follower_count.setter
    def follower_count(self, count):
        self.follower_count = count


class Tag:
    @property
    def unique_slug(self):
        return self.unique_slug

    @unique_slug.setter
    def unique_slug(self, slug):
        self.unique_slug = slug

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def post_count(self):
        return self.post_count

    @post_count.setter
    def post_count(self, count):
        self.post_count = count

    @property
    def follower_count(self):
        return self.follower_count

    @follower_count.setter
    def follower_count(self, count):
        self.follower_count = count

    @property
    def image(self):
        return self.image

    @image.setter
    def image(self, image):
        self.image = image


class Image:
    def __init__(self, image_id):
        self.image_id = image_id

    @property
    def original_height(self):
        return self.original_height

    @original_height.setter
    def original_height(self, height):
        self.original_height = height

    @property
    def original_width(self):
        return self.original_width

    @original_width.setter
    def original_width(self, width):
        self.original_width = width

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, url):
        self.url = url


class OutputFormat(Enum):
    PLAIN_TEXT = "text"
    JSON = "json"
    HTML = "html"
    MARKDOWN = "md"
