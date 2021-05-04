from selenium import webdriver
import requests
import time
import detection

DRIVERPATH = "D:\_DOCUMENTS\Code\chromedriver_win32\chromedriver.exe"

def img_scrape(url):
    driver = webdriver.Chrome(DRIVERPATH)   
    driver.get(url)
    time.sleep(5)
    elements = driver.find_elements_by_tag_name('img')
    for e in elements:
        img = e.get_attribute('src')
        
        filename = r"images/" + img.split('/')[-1]
        
        r = requests.get(img)
        with open(filename, "wb") as f:
            f.write(r.content)
            
        print(e.get_attribute ('alt'))
        
        ## only example of further development once data on images collected
        if detection.detect_text(filename): print("TO DO")
        
    driver.quit()

