#!/usr/bin/python
# -*- coding: utf8 -*-
from .model import User, Post, Publication, Tag, Image

__author__ = 'enginebai'

ROOT_URL = "https://medium.com/"


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
    ref_dict = payload["payload"]["references"]

    # interest_tags = user_meta_dict["interestTags"]
    # user.interest_tags = parse_tags(interest_tags)
    # author_tags = user_meta_dict["authorTags"]
    # user.author_tags = parse_tags(author_tags)

    publication_ids = user_meta_dict["collectionIds"]
    if publication_ids is not None and len(publication_ids) > 0:
        publication_list = []
        for pub_id in publication_ids:
            publication_dict = ref_dict["Collection"][pub_id]
            publication = Publication(pub_id)
            publication.name = publication_dict["name"]
            publication.unique_slug = publication_dict["slug"]
            publication.description = publication_dict["description"]
            image_dict = publication_dict["image"]
            publication.image = parse_images(image_dict)
            logo_dict = publication_dict["logo"]
            publication.logo = parse_images(logo_dict)
            publication.follower_count = publication_dict["metadata"]["followerCount"]
            publication_list.append(publication.__dict__)
        user.publications = publication_list

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
    return user.__dict__


def parse_post(payload):
    return parse_post_detail(payload, ("payload", "references", "Post"))


def parse_post_detail(payload, post_detail_keys):
    print(payload)
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
        # post_tags = virtual_dict["tags"]
        # post.post_tags = parse_tags(post_tags)

        post.unique_slug = unique_slug
        post.title = title
        post.post_date = post_date
        post.url = url
        post.recommend_count = recommend_count
        post.response_count = response_count
        post.read_time = read_time
        post.word_count = word_count
        post.image_count = image_count
        post.preview_image = parse_images(preview_image)

        # print("{id}, {title}".format(id=post_id, title=title))
        # print("{recommend}, {response}, {read}".format(
        # recommend=recommend_count, response=response_count, read=read_time))
        return post.__dict__

    post_list = []
    # payload -> references -> Post
    print(post_list_payload)
    if type(post_list_payload) is dict:
        for post_id in post_list_payload.keys():
            post_dict = post_list_payload.get(post_id)
            post_list.append(parse_post_dict(post_dict))
    # payload -> value
    elif type(post_list_payload) is list:
        for post_dict in post_list_payload:
            post_list.append(parse_post_dict(post_dict))
    return post_list


def parse_tags(tags_list_dict):
    if tags_list_dict is not None and len(tags_list_dict) > 0:
        tags_list = []
        for tag_dict in tags_list_dict:
            tag = Tag()
            tag.unique_slug = tag_dict["slug"]
            tag.name = tag_dict["name"]
            tag.post_count = tag_dict["postCount"]
            metadata_dict = tag_dict["metadata"]
            if metadata_dict is not None:
                tag.follower_count = metadata_dict["followerCount"]
            tags_list.append(tag.__dict__)
        return tags_list


def parse_images(image_dict):
    if image_dict is not None:
        image = Image(image_dict["imageId"] if "imageId" in image_dict else image_dict["id"])
        image.original_width = image_dict["originalWidth"]
        image.original_height = image_dict["originalHeight"]
        image.url = u"https://cdn-images-1.medium.com/fit/t/{width}/{height}/{id}"\
            .format(width=image.original_width,
                    height=image.original_height,
                    id=image.image_id)
        return image.__dict__
