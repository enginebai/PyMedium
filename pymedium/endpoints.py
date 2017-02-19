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
    return send_request(ROOT_URL + "@{0}/latest".format(username), param={"count": count})


@app.route("/top")
def get_top_posts():
    return send_request(ROOT_URL + "browse/top")


@app.route("/tags/<tag_name>", methods=["GET"])
def get_top_posts_by_tag(tag_name):
    return send_request(ROOT_URL + "tag/{tag}".format(tag=tag_name),
                        parse_keys=("payload", "value"))


@app.route("/tags/<tag_name>/latest", methods=["GET"])
def get_latest_posts_by_tag(tag_name):
    return send_request(ROOT_URL + "tag/{tag}/latest".format(tag=tag_name),
                        parse_keys=("payload", "value"))


@app.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    pass


def send_request(url, headers=ACCEPT_HEADER, param=None, parse_keys=None):
    req = requests.get(url, headers=headers, params=param)
    if req.status_code == requests.codes.ok:
        if parse_keys is not None:
            post_dict = parse_post_by_keys(req.text, parse_keys)
        else:
            post_dict = parse_post(req.text)
        return jsonify(post_dict)
    else:
        return Response(status=req.status_code)


def parse_post(request_text):
    return parse_post_by_keys(request_text, ("payload", "references", "Post"))


def parse_post_by_keys(request_text, keys):
    req_text = request_text.replace(ESCAPE_CHARACTERS, "").strip()
    print(req_text)
    response_dict = json.loads(req_text)
    post_dict =response_dict
    for key in keys:
        post_dict = post_dict.get(key)
        print(post_dict)
    return post_dict


if __name__ == "__main__":
    get_user_posts("enginebai")
