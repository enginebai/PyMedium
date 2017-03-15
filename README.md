# PyMedium - Unofficial Medium API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![PyMedium](https://raw.githubusercontent.com/enginebai/PyMedium/master/art/graphic.png)

*PyMedium* is an unofficial Medium API. It provides developers to access to user, post list and detail information from [Medium](
https://medium.com/) website. This is a read-only API to Medium, you can customize this API to fit your requirements and deploy on your own server.

## Installation
Before running PyMedium API, you have to clone the code from this repository, install requirements at first.

```shell
$ git clone git@github.com:enginebai/PyMedium.git
$ cd PyMedium
$ pip install -r requirements.txt
```

Then download web driver to `driver` folder from [Selenium](http://selenium-python.readthedocs.io/) or via the command-line with `curl` (update `{VERSION}` with the latest version code and `{OS` with your server operating system.

```shell
$ mkdir driver | cd driver
$ curl -O https://chromedriver.storage.googleapis.com/{VERSION}/chromedriver_{OS}.zip
$ unzip chromedriver_{OS}.zip
```

## Usage
To run this API application, use the `flask` command as same as [Flask Quickstart](http://flask.pocoo.org/docs/0.12/quickstart/)

```shell
$ export FLASK_APP=./pymedium/api.py
$ export FLASK_DEBUG=1 ## if you run in debug mode.
$ flask run
 * Running on http://localhost:5000/
```

## Documentation

### Users
`GET /{username}`

#### Response
```json
{
  "avatar": "1*Y7zH0UM975YmchIO86uIGA.jpeg",
  "bio": "Mixtape of developer, designer and startup. Cofounder and developer of DualCores Studio. Follow my technical blog: http://enginebai.logdown.com/",
  "display_name": "Engine Bai",
  "facebook": "789985027713671",
  "followedby_count": 442,
  "following_count": 238,
  "publications": [
    {
      "description": "Stories from the mix of designer and developer. 設計與工程的交織，混搭激盪出不同的想像。",
      "follower_count": 300,
      "image": {
        "image_id": "1*DLixNgsMpK5B74na3EDucQ.png",
        "original_height": 591,
        "original_width": 591,
        "url": "https://cdn-images-1.medium.com/fit/t/591/591/1*DLixNgsMpK5B74na3EDucQ.png"
      },
      "logo": {
        "image_id": "1*DLixNgsMpK5B74na3EDucQ.png",
        "original_height": 591,
        "original_width": 591,
        "url": "https://cdn-images-1.medium.com/fit/t/591/591/1*DLixNgsMpK5B74na3EDucQ.png"
      },
      "name": "DualCores Studio",
      "publication_id": "275e26e7c1b2",
      "unique_slug": "dualcores-studio"
    }
  ],
  "twitter": "enginebai",
  "user_id": "3301d32a6bba",
  "username": "enginebai"
}
```

### Post
* `GET /{username}/posts`
* `GET /top`
* `GET /tag/{tag}`
* `GET /tag/{tag}/latest`

#### Parameters
|Name   |Type   |Description   |
|---|---|---|
|n   |integer   |The count of posts to return.   |

#### Response
```json
[
  {
    "image_count": 14,
    "post_date": 1478533474858,
    "post_id": "99a3d86df228",
    "preview_image": {
      "image_id": "1*zhnQJhNzp-Oal1-GU1EUKw.png",
      "original_height": 412,
      "original_width": 608,
      "url": "https://cdn-images-1.medium.com/fit/t/608/412/1*zhnQJhNzp-Oal1-GU1EUKw.png"
    },
    "read_time": 7.74811320754717,
    "recommend_count": 351,
    "response_count": 10,
    "title": "Make an android custom view, publish and open source.",
    "unique_slug": "make-an-android-custom-view-publish-and-open-source-99a3d86df228",
    "url": "https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228",
    "word_count": 1669
  }
]```

### Post detail
`GET /post`

#### Parameters
|Name   |Type   |Description   |
|---|---|---|
|u   |string   |The post url to parse content.   |
|format   |string   |(optional) The format of response, the value could be `text`, `html`, `md`, `json`, default is `text`.   |

#### Response
```
## Simple text, json, html, markdown format
```


## Issues
Feel free to submit bug reports or feature requests and make sure you read the contribution guideline before opening any issue.


## Contributing
1. Check the open/close issues or open a fresh issue for feature request or bug report with different labels (`feature`/`bug`).
2. Fork this [repository](https://github.com/enginebai/PyMedium) on GitHub to start customizing on master or new branch.
3. Write a test which shows that the feature works as expected or the bug was fixeed.
4. Send a pull request and wait for code review.

[Read more on contributing](./CONTRIBUTING.md).

License
-------

Copyright (c) 2017 Engine Bai
Licensed under the [MIT license](http://opensource.org/licenses/MIT).
