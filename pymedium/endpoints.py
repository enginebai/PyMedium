#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json

from flask import Flask, jsonify, Response, request
import requests

ROOT_URL = "https://medium.com/"
ESCAPE_CHARACTERS = "])}while(1);</x>"
ACCEPT_HEADER = {"Accept": "application/json"}

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!!"


@app.route("/<username>", methods=["GET"])
def get_user_posts(username, count=10):
    return send_request(ROOT_URL + "@{0}/latest".format(username), param={"count": count}, parse_function=parse_user)


@app.route("/top")
def get_top_posts():
    return send_request(ROOT_URL + "browse/top")


@app.route("/tags/<tag_name>", methods=["GET"])
def get_top_posts_by_tag(tag_name):
    return send_request(ROOT_URL + "tag/{tag}".format(tag=tag_name))


@app.route("/tags/<tag_name>/latest", methods=["GET"])
def get_latest_posts_by_tag(tag_name):
    return send_request(ROOT_URL + "tag/{tag}/latest".format(tag=tag_name))


def send_request(url, headers=ACCEPT_HEADER, param=None, parse_function=None):
    req = requests.get(url, headers=headers, params=param)
    if req.status_code == requests.codes.ok:
        model_dict = parse_function(json.loads(req.text.replace(ESCAPE_CHARACTERS, "").strip()))
        return jsonify(model_dict)
    else:
        return Response(status=req.status_code)


def parse_user(payload):
    user_dict = payload["payload"]["user"]
    user_id = user_dict["userId"]
    username = user_dict["username"]
    display_name = user_dict["name"]
    avatar = user_dict["imageId"]
    bio = user_dict["bio"]
    twitter_name = user_dict["twitterScreenName"]
    facebook_name = user_dict["facebookAccountId"]

    user_meta_dict = payload["payload"]["userMeta"]
    interest_tags = user_meta_dict["interestTags"]
    author_tags = user_meta_dict["authorTags"]

    ref_dict = payload["payload"]["references"]
    publications = ref_dict["Collection"]

    stats_dict = ref_dict["SocialStats"][user_id]
    following_count = stats_dict["usersFollowedCount"]
    followby_count = stats_dict["usersFollowedByCount"]

    print("{id}, {name}, {display_name}, {avatar}\n{bio}\n{twitter}, {facebook}, {following}, {follower}"
          .format(id=user_id,
                  name=username,
                  display_name=display_name,
                  avatar=avatar,
                  bio=bio,
                  twitter=twitter_name,
                  facebook=facebook_name,
                  following=following_count,
                  follower=followby_count))
    return publications


def parse_post(payload):
    pass


@app.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    pass


if __name__ == "__main__":
    get_user_posts("enginebai")
