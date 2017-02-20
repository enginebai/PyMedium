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
def get_user_profile(username):
    return send_request(ROOT_URL + "@{0}/latest".format(username), parse_function=parse_user)


@app.route("/<username>/posts", methods=["GET"])
def get_user_posts(username, count=10):
    return send_request(ROOT_URL + "@{0}/latest".format(username), parse_function=parse_post)


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
    post_list_dict = payload["payload"]["references"]["Post"]
    post_list = []
    for post_id in post_list_dict.keys():
        post_dict = post_list_dict.get(post_id)
        title = post_dict["title"]
        subtitle = post_dict["content"]["subtitle"]
        post_date = post_dict["createdAt"]
        publication_id = post_dict["approvedHomeCollectionId"]

        # TODO: url

        virtual_dict = post_dict["virtuals"]
        recommend_count = virtual_dict["recommends"]
        response_count = virtual_dict["responsesCreatedCount"]
        read_time = virtual_dict["readingTime"]
        word_count = virtual_dict["wordCount"]
        image_count = virtual_dict["imageCount"]
        preview_image = virtual_dict["previewImage"]
        post_tags = virtual_dict["tags"]

        pagination = payload["payload"]["paging"]

        print("{id}, {title}, {subtitle}, {date}\n{recommend}, {response}, {read}, {word}, {image}"
              .format(id=post_id, title=title, subtitle=subtitle, date=post_date,
                      recommend=recommend_count, response=response_count, read=read_time,
                      word=word_count, image=image_count))
        return pagination


@app.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    pass


if __name__ == "__main__":
    get_user_profile("enginebai")
