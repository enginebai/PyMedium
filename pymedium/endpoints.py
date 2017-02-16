#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json

from flask import Flask, jsonify, Response
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
def get_posts_by_tag(tag_name):
    return send_request(ROOT_URL + "tag/{tag}/latest".format(tag=tag_name))


@app.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    pass


def send_request(url, headers=ACCEPT_HEADER, param=None):
    req = requests.get(url, headers=headers, params=param)
    if req.status_code == requests.codes.ok:
        post_dict = parse_post(req.text)
        return jsonify(post_dict)
    else:
        return Response(status=req.status_code)


def parse_post(request_text):
    req_text = request_text.replace(ESCAPE_CHARACTERS, "").strip()
    response_dict = json.loads(req_text)
    post_dict = response_dict.get("payload").get("references").get("Post")
    print(post_dict)
    app.logger.debug(post_dict)
    return post_dict


if __name__ == "__main__":
    get_user_posts("enginebai")
