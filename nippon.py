from selenium import webdriver
import time
import pandas as pd
import json
import numpy as np
from selenium.webdriver.chrome.options import Options
import re 

print("Starting webScraper: \n> app.py");
options = Options()
options.page_load_strategy = 'normal'
# driver = webdriver.Chrome('./chromedriver_linux64');
driver = webdriver.Chrome(options=options)

base_url = "https://www.sportslogos.net/teams/list_by_league/75/Nippon_Professional_Baseball/Japanese_NPB/logos/";
driver.get(base_url);

ar = [

]
print('\n\nno of teams: length ar => ', len(ar), "\n\n")

def get_ea_link_xpath(index):
  return f"//*[@id=\"team\"]/ul/li[{index}]/a" 

def get_ea_img_xpath(index):
  return f"//*[@id=\"team\"]/ul/li[{index}]/a/img" 

report = {}

for idx in range(12, 13):
  try:
    a_elem = driver.find_element_by_xpath(get_ea_link_xpath(idx))
    if a_elem is None : continue
    teamName = a_elem.get_attribute('title').replace(' Logos', '')
    print('> ',teamName)

    teamImg = ""
    try:
      img_elem = driver.find_element_by_xpath(get_ea_img_xpath(idx))
      if img_elem is not None :
        teamImg = img_elem.get_attribute('src')
    except: pass

    report[teamName] = {
      "teamName": teamName,
      "teamImg": teamImg,
      "teamAliases": [teamName, *teamName.split(' ')],
      "color1": "",
      "color2": "",
    }
  except: pass
  
driver.quit()

with open(f'dump.json', 'w') as f:
            json.dump(report, f)
print("Done...")

print("End\n\n\n");