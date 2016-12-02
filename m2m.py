#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://medium.com/dualcores-studio/make-an-android-custom-view-publish-and-open-source-99a3d86df228#.jh09xxid3'
# driver_path = os.path.join(os.getcwd(), "chromedriver")
# driver = webdriver.Chrome(driver_path)
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                          desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
# desired_capabilities=DesiredCapabilities.CHROME)
driver.get(url)
assert 'android' in driver.title
h1_tags = driver.find_elements_by_tag_name('h3')
for h1 in h1_tags:
    print(h1.text)

driver.quit()
# req = requests.get(url)
# html = BeautifulSoup(req.content)
# print(html)
