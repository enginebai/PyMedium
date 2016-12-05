#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def medium2markdown(url):
    # driver = webdriver.Chrome(driver_path)
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
    # desired_capabilities=DesiredCapabilities.CHROME)
    driver.get(url)
    # assert 'android' in driver.title
    content_tag = driver.find_element_by_class_name('postArticle-content')
    content_html = BeautifulSoup(content_tag.get_attribute('innerHTML'), "html.parser") \
        .find_all()
    # print(content_html)
    # output_file(content_html)

    for i in range(0, len(content_html)):
        tag = content_html[i]
        # print(i, tag.name, '[NONE]' if len(text) == 0 else text)
        md = toMarkdown(tag)
        if md is not None:
            print(i, md)
    driver.quit()


def output_file(content_html):
    with open('content.html', 'w') as f:
        f.writelines(content_html.prettify())


def strip_space(text, trim_space=True):
    text = re.sub(r'\s+', ' ', text)
    if trim_space:
        return text.strip()
    else:
        return text


def toMarkdown(medium_tag):
    text = strip_space(medium_tag.text)
    if medium_tag.name == 'h3':
        return '## {}'.format(text)
    elif medium_tag.name == 'h4':
        return '### {}'.format(text)
    elif medium_tag.name == 'p':
        ## find style, link inside a paragraph
        plain_text = ''
        for child in medium_tag.children:
            if child.name is None:
                if len(strip_space(child.string)) > 0:
                    plain_text += strip_space(child.string, False)
            else:
                content = strip_space(child.text)
                if child.name == 'strong':
                    plain_text += "**{0}**".format(content)
                elif child.name == 'em':
                    plain_text += "_{0}_ ".format(content)
                elif child.name == 'a':
                    plain_text += "[{0}]({1}) ".format(content, child['href'])
                elif child.name == 'code' or child.name == '':
                    plain_text += "`{0}`".format(content)
                    # print(child.name, child)
        return plain_text
    else:
        return None


if __name__ == '__main__':
    # url = 'https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228#.jh09xxid3'
    url = 'https://medium.com/@enginebai/this-is-title-115e6d7a89a1#.8ejqpawfi'
    medium2markdown(url)
