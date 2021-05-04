from selenium import webdriver
import requests
import time
import detection

DRIVERPATH = "D:\_DOCUMENTS\Code\chromedriver_win32\chromedriver.exe"
ls = []
def img_scrape(url):
    driver = webdriver.Chrome(DRIVERPATH)   
    driver.get(url)
    time.sleep(5)
    elements = driver.find_elements_by_tag_name('img')
    for e in elements:
        img = e.get_attribute('src')
        print(e.get_attribute ('alt'))
        filename = r"images/" + img.split('/')[-1]
        ls.append(filename)
        r = requests.get(img)
        with open(filename, "wb") as f:
            f.write(r.content)
    driver.quit()
    detection.detect_text(ls)
