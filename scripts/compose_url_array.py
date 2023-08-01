import time
from openpyxl import Workbook
import re
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


def get_pages_links():
    options = webdriver.ChromeOptions() 
    options.add_argument('--headless')

    service = ChromeService(executable_path=ChromeDriverManager().install())
    with webdriver.Chrome(service=service, options=options) as driver:  


        url = "https://www.lnr.fr/"

        driver.get(url)

        top_14_href = driver.find_elements(By.XPATH,'//div[@class="small-6 columns text-center"][1]/a[1]')[0]
        pro_d2_href = driver.find_elements(By.XPATH,'//div[@class="small-6 columns text-center"][2]/a[1]')[0]
        cookie_btn = driver.find_elements(By.XPATH,'//span[@class="didomi-continue-without-agreeing"]')

        top_14_link = top_14_href.get_attribute("href")
        pro_d2_link = pro_d2_href.get_attribute("href")

        # Don't accept cookie
        cookie_btn[0].click()

        # TOP 14 page
        top_14_href.click() # Go to top 14 page
        players_href = driver.find_elements(By.XPATH,'//nav[@class="top-bar subnav sticky-nav"]/section/ul[@class="right"]/li[7]/a')[0]
        # Open players page
        players_href.click()

        # Select filter by team
        alphabetical_filter_href = driver.find_elements(By.XPATH,'//dl/dd[2]/a')[0]
        alphabetical_filter_href.click()

        # Link from A to Z
        letters_filter_href = driver.find_elements(By.XPATH,'//div[@class="view"][1]//ul[@class="type-letters"]/li')
        print(len(letters_filter_href))

        links = []
        for curr_letter_link in letters_filter_href:
            curr_letter_link.click()

            # Wait 2 seconds between each letters
            time.sleep(2)

            players_card_href_list = driver.find_elements(By.XPATH,'//ul[@class="fluid-block-grid-7 player-list vs-items"]//li/a') 
            
            for player_card in players_card_href_list:
                links.append(player_card.get_attribute("href"))

        # time.sleep(360)
        driver.close()

        return links