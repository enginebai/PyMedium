# M2M - the Medium & Markdown conversion tool

[![License](https://img.shields.io/badge/license-Apache%202-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
> Download badge

* **What** is m2m? It is a tool to help you convert medium article into markdown format file. It can be used to backup your medium articles or just synchronize your medium to several blog platform.
* **Why** is m2m? For those people who have several blog platforms, it's a real pain :weary: to write your same article again and again or copy/paste and change the format separately to different platform. The m2m is here to solve this problem, once you complete your new medium article, you just use it to export to markdown and import your article. 

> Screenshot


## Installation

```shell
$ pip install m2m
```

## Setup
> Download selenium driver and start it.

## Usage
From medium to markdown:

```shell
$ m2m http://medium.com/enginebai/blog1 ./output/blog1.md
```



## Supported medium format
* Title `<h1>` = None
* Head1 `<h3>` = ## Head1
* Head2 `<h4>` = ### Head2
* Plain text `<p>` = Just text
* Quote `<blockquote>` = > Quote
* Bold `<strong>` = **Bold**
* Italic `<em>` = _Italic_
* Bulleted list `<ul><li></li></ul>` = * Item
* Ordered list `<ol><li></li><ol>` = 1. Item
* Separator `<hr>` = ----
* Code block `<pre>` = ```here is code.```
* Inline Code `<code>` = `code`
* Link `<a>` = [comment text](link)
* Image `<img>` = ![comment text](https://cdn-images-1.medium.com/max/280/1*hTcF28wQFIR9Sv0jfKTRNQ.png)
* Image comment = `<figcaption class="imageCaption"/>`
* Gist = `<div class="iframeContainer"><iframe`


> License
> 