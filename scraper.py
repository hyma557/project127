from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/hymas/Desktop/project-128/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    plant_data = []
    for i in range(0, 420):
        soup = BeautifulSoup(browser.page_source, "html.parer")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tags.find_all("li")
            temp_list = []
             for index,li_tags in enumerate(li_tags):
                 if index == 0:
                     temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.appened(li_tag.contents[0])
                    except:
                        temp_list.append("")
            
            
scrape()
 
 



    
    
