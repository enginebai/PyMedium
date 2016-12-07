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
        # text = strip_space(tag.text)
        # print(i, tag.name, '[NONE]' if len(text) == 0 else text)
        md = to_markdown(tag)
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


def to_markdown(medium_tag):
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
                    # print(child.name, child)
        return plain_text
    elif medium_tag.name == 'figure':
        img_tag = medium_tag.find('img', class_='progressiveMedia-image')
        if img_tag is not None and img_tag.has_attr('data-src'):
            figcaption_tag = medium_tag.find('figcaption')
            if figcaption_tag is not None:
                return '![{0}]({1})'.format(strip_space(figcaption_tag.text),
                                            img_tag['data-src'])
            else:
                return '![]({})'.format(img_tag['data-src'])
    elif medium_tag.name == 'blockquote':
        return '> {}'.format(strip_space(medium_tag.text))
    elif medium_tag.name == 'ul':
        li_tags = medium_tag.find_all('li')
        # use newline to join several item lines
        list_text = '\n'.join(['* {}'.format(strip_space(li.text)) for li in li_tags])
        return list_text
    elif medium_tag.name == 'ol':
        li_tags = medium_tag.find_all('li')
        # use newline to join several item lines
        list_text = '\n'.join(['{0}. {1}'.format(i + 1, strip_space(li_tags[i].text))
                               for i in range(len(li_tags))])
        return list_text
    else:
        return None


if __name__ == '__main__':
    # url = 'https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228#.jh09xxid3'
    url = 'https://medium.com/@enginebai/this-is-title-115e6d7a89a1#.8ejqpawfi'
    medium2markdown(url)
