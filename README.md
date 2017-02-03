# M2M - the Medium & Markdown conversion tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![](https://raw.githubusercontent.com/enginebai/m2m/master/art/graphic.png)

The `m2m` is a tool to help you convert medium article into markdown format file. It can be used to backup your medium articles or just synchronize your medium to other several blog platforms.

**Why** is `m2m`? For those people who have several blog platforms, it's a real pain :weary: to write your same article again and again or copy/paste and change the format separately to different platforms. The `m2m` is here to solve this problem, once you complete your new medium article, you just use it to export to markdown and import your article to those platforms. 


## Installation

```shell
$ pip install m2m
```

## Setup
> Download selenium driver and start it.

## Usage
### Medium CLI Tool:

* You can convert from medium to markdown file by default:

```shell
$ m2m http://medium.com/enginebai/blog1 ./output/blog1.md
```

* Or export to markdown file with default article title:

```shell
$ m2m http://medium.com/enginebai/blog1
```

#### Medium GET API:

* Now you can get 

## Supported medium format
The most common format of text on medium is supported by `m2m`, however, medium provides rich embed content more than `m2m` can support, just make sure your **embed contents** are not missing after conversion yet or you can append the link manually.

The following is supported format:

* Plain text.
* Header1, header2.
* Bold, italic.
* Link, embed link.
* Quote.
* Separator.
* Ordered and bulleted list.
* Image 
* Inline code, code block, gist.

> The full list you can check on [wiki](https://github.com/enginebai/m2m/wiki/Medium-supported-format-demo) page. 

## License

        The MIT License (MIT)

        Copyright © 2016 Engine Bai.

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in
        all copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
        THE SOFTWARE.
