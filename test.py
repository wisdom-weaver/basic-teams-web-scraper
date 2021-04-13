from selenium import webdriver


opts = webdriver.ChromeOptions()
opts.add_argument('headless')
browser = webdriver.Chrome(options=opts)
try:
    browser.get('https://www.google.com')
    html = browser.page_source
    print(html[:100])
    browser.quit()
except:
    browser.quit()
    raise
