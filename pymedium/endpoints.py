#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import http

from flask import Flask, jsonify, Response
import requests

ROOT_URL = "https://medium.com/"
EXCEPE_STR = "])}while(1);</x>"
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!!"


@app.route("/<username>", methods=["GET"])
def get_user_posts(username, count=10):
    payload = {"count": count}
    accept_header = {"Accept": "application/json"}
    req = requests.get(ROOT_URL + "@{0}/latest".format(username),
                       headers=accept_header,
                       params=payload)
    if req.status_code == requests.codes.ok:
        req_text = req.text.replace(EXCEPE_STR, "").strip()
        response_dict = json.loads(req_text)
        post_dict = response_dict.get("payload").get("references").get("Post")
        return jsonify(post_dict)
    else:
        return Response(status=req.status_code)


@app.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    pass


@app.route("/top")
def get_top_posts():
    pass


@app.route("/tags/<tag_name>", methods=["GET"])
def get_posts_by_tag(tag_name):
    pass


if __name__ == "__main__":
    get_user_posts("enginebai")
