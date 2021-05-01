import time
import datetime
from utils import Utils

class elements():
    def __init__(self, driver_tab: str, id_value: str, data_file_name: str, ignore: bool):
        self.driver_tab = driver_tab
        self.id_value = id_value
        self.data_file_name = data_file_name
        self.ignore = ignore

        if (ignore):
            print(id_value + ' | Ignored operation.')
            return

        xpathCatalog = '//*[@id="' + id_value + '"]/div'

        driver_tab.click()
        readMore = driver_tab.find_element_by_xpath('//*[@id="catalog-search"]/div[6]/div[2]/div/div/a')
        
        # Click on the 'LOAD MORE' button until all the elements are loaded
        print(id_value + ' | Loading elements...')
        while (len(readMore.text) > 0): readMore.click()

        elementsCatalog = driver_tab.find_elements_by_xpath(xpathCatalog)
        data = []

        print(id_value + ' | Start collect catalog elements...')
        for element in elementsCatalog:
            url = element.find_element_by_tag_name('a').get_attribute("href")
            uuid = element.find_element_by_tag_name('a').get_attribute("id")
            title = element.find_element_by_tag_name('h4').text
            creator = element.find_element_by_class_name('creator').text[3:]
            price = element.find_element_by_tag_name('div').find_element_by_css_selector('p:not(.ng-hide)').text
            keyart = element.find_element_by_tag_name('img').get_attribute("bn-lazy-src")

            if(len(uuid) == 0): continue
            if (price != 'FREE'): price = int(price)

            data.append({
                'uuid': uuid,
                'title': title,
                'creator': creator,
                'price': price,
                'url': url,
                'keyart': keyart
            })
        
        print(id_value + ' | Total elements searched:', len(data))
        print(id_value + ' | Generating file...')
        Utils.writeJsonFile('./data/', data_file_name, data)
        print(id_value + ' | File created.\n')
