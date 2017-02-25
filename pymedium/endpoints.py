#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json

from flask import Flask, jsonify, Response
import requests

from .model import Post, User

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
    return send_request(ROOT_URL + "@{0}/latest".format(username), parse_function=parse_post)


@app.route("/top")
def get_top_posts():
    return send_request(ROOT_URL + "browse/top", parse_function=parse_post)


@app.route("/tags/<tag_name>", methods=["GET"])
def get_top_posts_by_tag(tag_name):
    return send_request(ROOT_URL + "tag/{tag}".format(tag=tag_name),
                        parse_function=parse_post_from_search_by_tags)


@app.route("/tags/<tag_name>/latest", methods=["GET"])
def get_latest_posts_by_tag(tag_name):
    return send_request(ROOT_URL + "tag/{tag}/latest".format(tag=tag_name),
                        parse_function=parse_post_from_search_by_tags)


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


def parse_user(payload):
    user_dict = payload["payload"]["user"]
    user_id = user_dict["userId"]
    user = User(user_id)
    username = user_dict["username"]
    display_name = user_dict["name"]
    avatar = user_dict["imageId"]
    bio = user_dict["bio"]
    twitter_name = user_dict["twitterScreenName"]
    facebook_id = user_dict["facebookAccountId"]

    user_meta_dict = payload["payload"]["userMeta"]
    interest_tags = user_meta_dict["interestTags"]
    author_tags = user_meta_dict["authorTags"]
    publication_ids = user_meta_dict["collectionIds"]

    ref_dict = payload["payload"]["references"]
    publications = ref_dict["Collection"]

    # TODO: parse publication information

    stats_dict = ref_dict["SocialStats"][user_id]
    following_count = stats_dict["usersFollowedCount"]
    followby_count = stats_dict["usersFollowedByCount"]

    user.user_id = user_id
    user.username = username
    user.display_name = display_name
    user.avatar = avatar
    user.bio = bio
    user.twitter = twitter_name
    user.facebook = facebook_id
    user.following_count = following_count
    user.followedby_count = followby_count
    user.interest_tags = interest_tags
    user.author_tags = author_tags
    user.publications = publications
    return user.__dict__


def parse_post_from_search_by_tags(payload):
    return parse_post_detail(payload, ("payload", "value"))


def parse_post(payload):
    return parse_post_detail(payload, ("payload", "references", "Post"))


def parse_post_detail(payload, post_detail_keys):
    if post_detail_keys is None:
        return
    post_list_payload = payload
    for key in post_detail_keys:
        post_list_payload = post_list_payload.get(key)

    def parse_post_dict(post_dict):
        post_id = post_dict["id"]
        post = Post(post_id)
        unique_slug = post_dict["uniqueSlug"]
        title = post_dict["title"]
        post_date = post_dict["createdAt"]

        # print(post_date)
        publication_id = post_dict["approvedHomeCollectionId"]

        url = ROOT_URL
        ref_dict = payload["payload"]["references"]
        if publication_id is not None and publication_id:
            publication_dict = ref_dict["Collection"][publication_id]
            # custom publication domain
            if "domain" in publication_dict and publication_dict["domain"]:
                url = "https://" + publication_dict["domain"]
            else:
                # simple publication
                url += publication_dict["slug"]
        else:
            # personal post, no publication
            creator_id = post_dict["creatorId"]
            username = ref_dict["User"][creator_id]["username"]
            url += "@{username}".format(username=username)
        url += u"/{path}".format(path=unique_slug)

        virtual_dict = post_dict["virtuals"]
        recommend_count = virtual_dict["recommends"]
        response_count = virtual_dict["responsesCreatedCount"]
        read_time = virtual_dict["readingTime"]
        word_count = virtual_dict["wordCount"]
        image_count = virtual_dict["imageCount"]
        preview_image = virtual_dict["previewImage"]
        post_tags = virtual_dict["tags"]

        post.unique_slug = unique_slug
        post.title = title
        post.post_date = post_date
        post.url = url
        post.recommend_count = recommend_count
        post.response_count = response_count
        post.read_time = read_time
        post.word_count = word_count
        post.image_count = image_count
        post.preview_image = preview_image
        post.post_tags = post_tags

        # print("{id}, {title}".format(id=post_id, title=title))
        # print("{recommend}, {response}, {read}".format(
        # recommend=recommend_count, response=response_count, read=read_time))
        return post.__dict__

    post_list = []
    # payload -> references -> Post
    if type(post_list_payload) is dict:
        for post_id in post_list_payload.keys():
            post_dict = post_list_payload.get(post_id)
            post_list.append(parse_post_dict(post_dict))
    # payload -> value
    elif type(post_list_payload) is list:
        for post_dict in post_list_payload:
            post_list.append(parse_post_dict(post_dict))
    return post_list


@app.route("/posts/<post_id>", methods=["GET"])
def get_post(post_id):
    pass


if __name__ == "__main__":
    get_user_profile("enginebai")
