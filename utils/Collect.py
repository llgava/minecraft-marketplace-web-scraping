import os
import json
import time
import datetime
import requests
from utils import Utils
import dotenv
dotenv.load_dotenv()

class elements():
  def __init__(self, driver_tab: str, id_value: str, data_file_name: str, ignore: bool, send_to_database: bool):
    self.driver_tab = driver_tab
    self.id_value = id_value
    self.data_file_name = data_file_name
    self.ignore = ignore
    self.send_to_database = send_to_database

    data = []

    if (ignore):
      print(id_value + ' | Ignored operation.\n')
      return

    xpathCatalog = '//*[@id="' + id_value + '"]/div'

    driver_tab.click()
    readMore = driver_tab.find_element_by_xpath('//*[@id="catalog-search"]/div[6]/div[2]/div/div/a')

    # Click on the 'LOAD MORE' button until all the elements are loaded
    print(id_value + ' | Loading elements...')
    while (len(readMore.text) > 0): readMore.click()

    elementsCatalog = driver_tab.find_elements_by_xpath(xpathCatalog)

    print(id_value + ' | Start collect catalog elements...')
    if (send_to_database): print(id_value + ' | Sending collected data to minecraft-markeplace-api database.')

    # Start to collect all elements and send to database or/and create a file with all the data
    for element in elementsCatalog:
      elementData = element.find_element_by_tag_name('a').get_attribute('price-catalog')
      uuid = element.find_element_by_tag_name('a').get_attribute('id')
      url = element.find_element_by_tag_name('a').get_attribute('href')

      if (len(uuid) == 0): continue
      if (send_to_database):

        # Send the data to database
        requests.post(os.environ.get("API_URL") + data_file_name, headers={"Authorization": os.environ.get("BEARER_TOKEN")}, data=
        {
          "uuid": uuid,
          "title": json.loads(elementData)["Title"]["neutral"],
          "description": json.loads(elementData)["Description"]["neutral"],
          "creator": json.loads(elementData)["DisplayProperties"]["creatorName"],
          "price": json.loads(elementData)["DisplayProperties"]["price"],
          "trailer": json.loads(elementData)["DisplayProperties"]["videoUrl"],
          "keyart": json.loads(elementData)["Images"][0]["url"],
          "rating": {
              "average": json.loads(elementData)["AverageRating"],
              "total": json.loads(elementData)["TotalRatingsCount"]
          },
          "url": url
        })

        # Create a file with all the data
        data.append(
        {
          "uuid": uuid,
          "title": json.loads(elementData)["Title"]["neutral"],
          "description": json.loads(elementData)["Description"]["neutral"],
          "creator": json.loads(elementData)["DisplayProperties"]["creatorName"],
          "price": json.loads(elementData)["DisplayProperties"]["price"],
          "trailer": json.loads(elementData)["DisplayProperties"]["videoUrl"],
          "keyart": json.loads(elementData)["Images"][0]["url"],
          "rating": {
              "average": json.loads(elementData)["AverageRating"],
              "total": json.loads(elementData)["TotalRatingsCount"]
          },
          "url": url
        })

    # Save the file and finish the proccess
    print(id_value + ' | Total elements searched:', len(data))
    print(id_value + ' | Generating file...')
    Utils.writeJsonFile('./data/', data_file_name, data)
    print(id_value + ' | File created.\n')
