from utils import Utils, Collect
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.minecraft.net/en-us/catalog"

# webdriver
# To run the webdrive in background add this
# inside Firefox webdriver: options=option
option = Options()
option.headless = True
browser = webdriver.Firefox(options=option)

# Search element in the HTML
browser.get(url)
skinPacksTab = browser.find_element_by_link_text('SKIN PACKS')
texturePacksTab = browser.find_element_by_link_text('TEXTURE PACKS')
mashUpPacksTab = browser.find_element_by_link_text('MASH-UP PACKS')
adventureMapsTab = browser.find_element_by_link_text('ADVENTURE MAPS')
miniGamesTab = browser.find_element_by_link_text('MINI GAMES')
survivalSpawnsTab = browser.find_element_by_link_text('SURVIVAL SPAWNS')

# Collect from every category
Collect.elements(skinPacksTab, 'skinpack', 'skin-packs', False)
Collect.elements(texturePacksTab, 'resourcepack', 'texture-packs', False)
Collect.elements(mashUpPacksTab, 'mashup', 'mash-up-packs', False)
Collect.elements(adventureMapsTab, 'adventure_world', 'adventure-maps', False)
Collect.elements(miniGamesTab, 'mini_game_world', 'mini-games', False)
Collect.elements(survivalSpawnsTab, 'survival_spawn_world',
                 'survival-packs', False)

# Close Firefox
browser.quit()
