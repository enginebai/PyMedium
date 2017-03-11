#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import http
import json

import requests
from flask import Flask, jsonify, Response, request
from pymedium.parser import parse_user, parse_post, parse_post_detail
from pymedium.model import OutputFormat

ROOT_URL = "https://medium.com/"
ESCAPE_CHARACTERS = "])}while(1);</x>"
ACCEPT_HEADER = {"Accept": "application/json"}
COUNT = 10

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello!!"


@app.route("/<username>", methods=["GET"])
def get_user_profile(username):
    return send_request(ROOT_URL + "@{0}/latest".format(username), parse_function=parse_user)


@app.route("/<username>/posts", methods=["GET"])
def get_user_posts(username):
    count = request.args.get("n", COUNT)
    return process_post_request(ROOT_URL + "@{0}/latest?limit={count}".format(username, count=count))


@app.route("/top")
def get_top_posts():
    count = request.args.get("n", COUNT)
    return process_post_request(ROOT_URL + "browse/top?limit={count}".format(count=count))


@app.route("/tags/<tag_name>", methods=["GET"])
def get_top_posts_by_tag(tag_name):
    count = request.args.get("n", COUNT)
    return process_post_request(ROOT_URL + "tag/{tag}?limit={count}".format(tag=tag_name, count=count))


@app.route("/tags/<tag_name>/latest", methods=["GET"])
def get_latest_posts_by_tag(tag_name):
    count = request.args.get("n", COUNT)
    return process_post_request(ROOT_URL + "tag/{tag}/latest?limit={count}".format(tag=tag_name, count=count))


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


@app.route("/post", methods=["GET"])
def get_post():
    url = request.args.get("u", "")
    print(url)
    output_format = request.args.get("format", OutputFormat.PLAIN_TEXT.value)
    if url:
        return parse_post_detail(url, output_format)
    else:
        return Response(status=400)
