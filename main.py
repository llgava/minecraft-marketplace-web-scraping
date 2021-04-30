import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.minecraft.net/en-us/catalog"

option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)

""" procura o elemento """
element = driver.find_element_by_xpath(
    '//*[@id="Most Popular all"]/div/div/div[2]/div/categorydata/div[3]')
html = element.get_attribute('outerHTML')


title = element.find_element_by_tag_name('h4').text
creator = element.find_element_by_class_name('creator').text
price = element.find_element_by_tag_name('div').find_element_by_css_selector('p:not(.ng-hide)').text
keyart = element.find_element_by_tag_name('img').get_attribute("bn-lazy-src")

print('TITLE: ', title)
print('CREATOR:', creator)
print('PRICE:', price)
print('KEYART:', keyart)

element.click()

driver.quit()
