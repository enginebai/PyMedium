#/usr/bin/python
# -*- encoding: utf-8 -*-
import requests
import json


def test_user_post_api(username):
    url = "http://localhost:5000/{username}/posts".format(username=username)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        response_list = json.loads(req.text)
        for post in response_list:
            r = requests.get(post["url"])
            print(post["title"])
            print(r.status_code, post["url"])
    else:
        print(req.status_code)


if __name__ == "__main__":
    # https://uxplanet.org/@101
    # https://blog.magikcraft.io/@sitapati
    users = ("sitapati", "enginebai", "101")
    for u in users:
        test_user_post_api(u)
