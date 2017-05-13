#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import json

import requests
from flask import Flask, jsonify, Response, request
from selenium import webdriver
from pymedium.parser import parse_user, parse_publication, parse_post, parse_post_detail
from pymedium.model import OutputFormat
import pymedium.constant as const

app = Flask(__name__)
driver = webdriver.Chrome("driver/chromedriver")


@app.route("/<name>", methods=["GET"])
def get_user_or_publication_profile(name):
    if name.startswith("@"):
        parse_function = parse_user
    else:
        parse_function = parse_publication
    return send_request(const.ROOT_URL + "{0}/latest".format(name), parse_function=parse_function)


@app.route("/<name>/posts", methods=["GET"])
def get_user_or_publication_posts(name):
    if name.startswith("@"):
        count = get_count_parameter()
        return process_post_request(const.ROOT_URL + "{0}/latest?limit={count}".format(name, count=count))
    else:
        return process_post_request(const.ROOT_URL + name)


@app.route("/top")
def get_top_posts():
    count = get_count_parameter()
    return process_post_request(const.ROOT_URL + "browse/top?limit={count}".format(count=count))


@app.route("/tags/<tag_name>", methods=["GET"])
def get_top_posts_by_tag(tag_name):
    count = get_count_parameter()
    return process_post_request(const.ROOT_URL + "tag/{tag}?limit={count}".format(tag=tag_name, count=count))


@app.route("/tags/<tag_name>/latest", methods=["GET"])
def get_latest_posts_by_tag(tag_name):
    count = get_count_parameter()
    return process_post_request(const.ROOT_URL + "tag/{tag}/latest?limit={count}".format(tag=tag_name, count=count))


def send_request(url, headers=const.ACCEPT_HEADER, param=None, parse_function=None):
    req = requests.get(url, headers=headers, params=param)
    print(url, req.status_code)
    if req.status_code == requests.codes.ok:
        if parse_function is None:
            parse_function = parse_post
        model_dict = parse_function(json.loads(req.text.replace(const.ESCAPE_CHARACTERS, "").strip()), return_dict=True)
        return jsonify(model_dict)
    else:
        return Response(status=req.status_code)


def process_post_request(url):
    return send_request(url, parse_function=parse_post)


def get_count_parameter():
    return request.args.get("n", const.COUNT)


@app.route("/post", methods=["GET"])
def get_post():
    url = request.args.get("u", "")
    print(url)
    output_format = request.args.get("format", OutputFormat.PLAIN_TEXT.value)
    if not output_format:
        output_format = OutputFormat.PLAIN_TEXT.value
    if url:
        detail_str = parse_post_detail(url, output_format, driver)
        status_code = 200
        mime_type = "text/html"
        if output_format == OutputFormat.JSON.value:
            if detail_str is None:
                status_code = 404
            else:
                detail_str = detail_str.replace(const.ESCAPE_CHARACTERS, "")
            mime_type = "application/json"
        return Response(response=detail_str,
                        status=status_code,
                        mimetype=mime_type)
    else:
        return Response(status=400)
