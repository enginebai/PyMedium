## Install
```shell
$ pip install m2m
```

## Usage
From medium to markdown:

```shell
$ m2m http://medium.com/enginebai/blog1 ./output/blog1.md
```
From markdown to medium:

```
$ m2m ./blog2.md 
```


## Medium support format
* Title `<h1>` None
* Head1 `<h3>` ## Head1
* Head2 `<h4>` ### Head2
* Plain text `<p>` Just text
* Quote `<blockquote>` > Quote
* Bold `<strong>` **Bold**
* Italic `<em>` _Italic_
* Bulleted list `<ul><li></li></ul>` * Item
* Ordered list `<ol><li></li><ol>` 1. Item
* Separator `<hr>` ----
* Code block `<pre>` ```here is code.```
* Inline Code `<code>` `code`
* Link `<a>` [comment text](link)
* Image `<img>` ![comment text](https://cdn-images-1.medium.com/max/280/1*hTcF28wQFIR9Sv0jfKTRNQ.png)
* Image comment `<figcaption class="imageCaption"/>`
* Gist `<div class="iframeContainer"><iframe`
* Video `<div class="iframeContainer"><iframe`