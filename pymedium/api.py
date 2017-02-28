#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json

from flask import Flask, jsonify, Response
import requests
from .parser import parse_user, parse_post

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
def get_user_posts(username):
    return process_post_request(ROOT_URL + "@{0}/latest".format(username))


@app.route("/top")
def get_top_posts():
    return process_post_request(ROOT_URL + "browse/top")


@app.route("/tags/<tag_name>", methods=["GET"])
def get_top_posts_by_tag(tag_name):
    return process_post_request(ROOT_URL + "tag/{tag}".format(tag=tag_name))


@app.route("/tags/<tag_name>/latest", methods=["GET"])
def get_latest_posts_by_tag(tag_name):
    return process_post_request(ROOT_URL + "tag/{tag}/latest".format(tag=tag_name))


def send_request(url, headers=ACCEPT_HEADER, param=None, parse_function=None):
    req = requests.get(url, headers=headers, params=param)
    req.encoding = "utf8"
    if req.status_code == requests.codes.ok:
        if parse_function is None:
            parse_function = parse_post
        model_dict = parse_function(json.loads(req.text.replace(ESCAPE_CHARACTERS, "").strip()))
        return jsonify(model_dict)
    else:
        return Response(status=req.status_code)


def process_post_request(url):
    return send_request(url, parse_function=parse_post)


@app.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    # TODO:
    pass


if __name__ == "__main__":
    get_user_profile("enginebai")
