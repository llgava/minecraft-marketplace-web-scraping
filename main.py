from utils import Utils, Collect
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.minecraft.net/en-us/catalog"

# webdriver
# To run in background add this options inside Firefox webdriver: options=option
option = Options()
option.headless = True
browser = webdriver.Firefox(options=option)

# search element
browser.get(url)
skinPacksTab = browser.find_element_by_link_text('SKIN PACKS')
texturePacksTab = browser.find_element_by_link_text('TEXTURE PACKS')
mashUpPacksTab = browser.find_element_by_link_text('MASH-UP PACKS')
adventureMapsTab = browser.find_element_by_link_text('ADVENTURE MAPS')
miniGamesTab = browser.find_element_by_link_text('MINI GAMES')
survivalSpawnsTab = browser.find_element_by_link_text('SURVIVAL SPAWNS')

# Collect.Execute(skinPacksTab, 'skinpack', 'skin-pack')
Collect.Execute(texturePacksTab, 'resourcepack', 'texture-pack')

# close firefox
browser.quit()
