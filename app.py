from selenium import webdriver
import time
import pandas as pd
import json
import numpy as np
from selenium.webdriver.chrome.options import Options


print("Starting webScraper: \n> app.py");
options = Options()
options.page_load_strategy = 'normal'
# driver = webdriver.Chrome('./chromedriver_linux64');
driver = webdriver.Chrome(options=options)
base_url = 'https://teamcolorcodes.com/ncaa-color-codes/';
driver.get(base_url);

ar = [
  {"teamName": "Baylor Bears", "link": "https://teamcolorcodes.com/baylor-bears-color-codes/"}
]

for i in range(2,26+2):
    j = 1
    while True:
      try:
        elem_x_path = f'//*[@id="genesis-content"]/article/div/p[{i}]/a[{j}]'
        elem = driver.find_element_by_xpath(elem_x_path)    
        if elem is not None:
          link = elem.get_attribute('href');
          teamName = elem.text
          print('got', teamName, link);
          ar.append({ 'teamName': teamName, 'link': link})
        j+=1
      except:
        j=1
        i+=1
        break;

print('\n\nno of teams: length ar => ', len(ar), "\n\n")
# ar = ar[0:3]

report = {}
for idx,ob in enumerate(ar):
  
  link = ob['link'];
  teamName = ob['teamName'];
  print('\n');
  print('-'*50);
  print('\n',teamName, '==>\n', 'link', link)
  report[teamName] = {}
  report[teamName]['link'] = link
  report[teamName]['teamName'] = teamName
  report[teamName]['teamAliases'] = [teamName, *teamName.split(' ')]
  driver.get(link)
  # time.sleep(2)
  try:
    teamImg = ''
    elems = driver.find_elements_by_tag_name('img');
    if elems is not None:
      elem = elems[0]
      teamImg = elem.get_attribute('src')
    report[teamName]['teamImg'] = teamImg
    print('teamImg', teamImg);
  except: report[teamName]['teamImg'] = ""
  try:
    color1_x_path = '/html/body/div[1]/div/div/main/article/div/div[1]'
    elem = driver.find_element_by_xpath(color1_x_path);
    text = elem.get_attribute("innerText")
    text = text.replace('\n', ' ').split(' ').filter
    text = filter(text, )
    color1 = color1[0: -1]
    report[teamName]['color1'] = color1
    print('color1', color1)
  except: report[teamName]['color1'] = ""
  try:
    color2_x_path = '/html/body/div[1]/div/div/main/article/div/div[2]'
    elem = driver.find_element_by_xpath(color2_x_path);
    text = elem.get_attribute("innerText")
    color2 = text.split('\n')[2].split(' ')[-1]
    color2 = color2[0: -1]
    report[teamName]['color2'] = color2
    print('color2', color2)
  except: report[teamName]['color2'] = ""

driver.quit()

with open(f'dump.json', 'w') as f:
            json.dump(report, f)
print("Done...")

print("End\n\n\n");
