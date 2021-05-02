import json
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
            elementData = element.find_element_by_tag_name('a').get_attribute("price-catalog")
            uuid = element.find_element_by_tag_name('a').get_attribute("id")
            url = element.find_element_by_tag_name('a').get_attribute("href")

            if(len(uuid) == 0): continue

            data.append({
                'uuid': uuid,
                'title': json.loads(elementData)['Title']['neutral'],
                'description': json.loads(elementData)['Description']['neutral'],
                'creator': json.loads(elementData)['DisplayProperties']['creatorName'],
                'price': json.loads(elementData)['DisplayProperties']['price'],
                'trailer': json.loads(elementData)['DisplayProperties']['videoUrl'],
                'keyart': json.loads(elementData)['Images'][0]['url'],
                'rating': {
                    'average': json.loads(elementData)['AverageRating'],
                    'total': json.loads(elementData)['TotalRatingsCount']
                },
                'url': url,
            })
        
        print(id_value + ' | Total elements searched:', len(data))
        print(id_value + ' | Generating file...')
        Utils.writeJsonFile('./data/', data_file_name, data)
        print(id_value + ' | File created.\n')
