# -*- coding: utf-8 -*-
from selenium import webdriver
import os

driver = webdriver.Firefox()
file_path = 'file:///E:/python/selenium_newbie/checkbox1.html'
print file_path
##driver.get(file_path)

#选择页面上所有的tag name 为input的元素
##inputs = driver.find_elements_by_tag_name('input')
#然后从中过滤出type为checkbox的元素,单击勾选
##for inpu in inputs:
##    if inpu.get_attribute('type') == 'checkbox':
##        inpu.click()

#driver.quit()
