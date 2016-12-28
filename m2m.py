#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import json
import requests
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

MEDIUM_ROOT = 'https://medium.com'
HTML_PARSER = "html.parser"
DEFAULT_DIR = "output"

driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)


def medium2markdown(url, md_path):
    driver.get(url)
    title_tag = driver.find_element_by_tag_name('title')
    title = BeautifulSoup(title_tag.get_attribute('innerHTML'), HTML_PARSER).text.strip()
    content_tag = driver.find_element_by_class_name('postArticle-content')
    content_html = BeautifulSoup(content_tag.get_attribute('innerHTML'), HTML_PARSER).find_all()

    if md_path is None or len(md_path) == 0:
        if not os.path.exists(DEFAULT_DIR):
            os.mkdir(DEFAULT_DIR)
        md_path = os.path.join(DEFAULT_DIR, title + ".md")
    with open(md_path, 'w') as md_file:
        for i in range(0, len(content_html)):
            tag = content_html[i]
            md = to_markdown(tag)
            if md is not None:
                print(md, file=md_file)
                print(md)


def output_file(content_html):
    with open('content.html', 'w') as f:
        f.writelines(content_html.prettify())


def strip_space(text, trim_space=True):
    text = re.sub(r'\s+', ' ', text)
    if trim_space:
        return text.strip()
    else:
        return text


def to_markdown(medium_tag):
    text = strip_space(medium_tag.text)
    if medium_tag.name == 'h3':
        return '\n## {}'.format(text)
    elif medium_tag.name == 'h4':
        return '\n### {}'.format(text)
    elif medium_tag.name == 'p':  # text paragraph
        ## find style, link inside a paragraph
        plain_text = ''
        for child in medium_tag.children:
            if child.name is None:
                if len(strip_space(child.string)) > 0:
                    plain_text += strip_space(child.string)
            else:
                content = strip_space(child.text)
                if child.name == 'strong':
                    plain_text += " **{0}** ".format(content)
                elif child.name == 'em':
                    plain_text += " _{0}_ ".format(content)
                elif child.name == 'a':
                    plain_text += " [{0}]({1}) ".format(content, child['href'])
                elif child.name == 'code' or child.name == '':
                    plain_text += " `{0}` ".format(content)
        return plain_text
    elif medium_tag.name == 'figure':  # image and comment
        img_tag = medium_tag.find('img', class_='progressiveMedia-image')
        if img_tag is not None and img_tag.has_attr('data-src'):
            figcaption_tag = medium_tag.find('figcaption')
            if figcaption_tag is not None:
                return '\n![{0}]({1})'.format(strip_space(figcaption_tag.text),
                                            img_tag['data-src'])
            else:
                return '\n![]({})'.format(img_tag['data-src'])
    elif medium_tag.name == 'blockquote':  # quote
        return '> {}\n'.format(strip_space(medium_tag.text))
    elif medium_tag.name == 'ul':
        li_tags = medium_tag.find_all('li')
        # use newline to join several item lines
        list_text = '\n'.join(['* {}'.format(strip_space(li.text)) for li in li_tags])
        return "\n" + list_text + "\n"
    elif medium_tag.name == 'ol':
        li_tags = medium_tag.find_all('li')
        # use newline to join several item lines
        list_text = '\n'.join(['{0}. {1}'.format(i + 1, strip_space(li_tags[i].text))
                               for i in range(len(li_tags))])
        return "\n" + list_text + "\n"
    elif medium_tag.name == 'pre':  # code block (not inline code or embed code)
        code_block = ''
        code_tags = medium_tag.prettify().split('<br/>')
        for i in range(len(code_tags)):
            t = BeautifulSoup(code_tags[i], HTML_PARSER)
            code = re.sub(r'\r\n(\s{10})', '', t.text).replace('\n', '')
            code_block += '{}\n'.format(code)
            # print(i, code)
        return '\n```\n{}```\n\n'.format(code_block)
    elif medium_tag.name == 'hr':
        return '\n----\n'
    elif medium_tag.name == 'iframe':
        # gist, video, github, link...etc.
        iframe_url = MEDIUM_ROOT + medium_tag['data-src']
        try:
            driver.get(iframe_url)
            iframe_content = BeautifulSoup(driver.page_source, HTML_PARSER)
            tag = iframe_content.find('div', class_='gist-meta')
            if tag is not None:
                gist_raw_link = tag.find('a', href=re.compile(r'gist.github.com(.*)/raw/'))
                if gist_raw_link is not None:
                    # print(gist_raw_link['href'])`
                    req = requests.get(gist_raw_link['href'])
                    if req.status_code == 200:
                        code_html = BeautifulSoup(req.content, HTML_PARSER)
                        return '\n```\n{}\n```\n\n'.format(code_html.prettify())
        except Exception:
            print("[ERROR] Failed to parse the embed link.")
            # print(e)

    elif medium_tag.name == 'a':
        # print(medium_tag.prettify())
        pass
    else:
        return None


def get_medium_test_urls():
    url = "https://cdnapi.pnd.gs/v2/feeds?limit=100&page=1&sort=popular&sources=medium"
    medium_req = requests.get(url)
    medium_urls = []
    if medium_req.status_code == 200:
        medium_json = json.loads(medium_req.text)
        for i in range(len(medium_json)):
            url = medium_json[i]['source']['absoluteUrl']
            medium_urls.append(url)
    return medium_urls



if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("[ERROR] Please provide either medium link or markdown file to convert.");
    else:
        arg1 = sys.argv[1]
        if arg1.lower().startswith('http'):
            if len(sys.argv) == 3:
                md_path = sys.argv[2]
            else:
                md_path = ''
            try:
                medium2markdown(arg1, md_path)
            finally:
                driver.close()

    # url = 'https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228#.jh09xxid3'
    # # url = 'https://medium.com/@enginebai/this-is-title-115e6d7a89a1#.8ejqpawfi'
    # try:
    #     # medium2markdown(url, '')
    #     urls = get_medium_test_urls()
    #     for url in urls:
    #         print(url)
    #         try:
    #             medium2markdown(url, '')
    #         except Exception as e:
    #             print(e)
    # finally:
    #     driver.close()
