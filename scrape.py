from selenium import webdriver
import requests
import time
import detection
from csv import DictReader
import os

DRIVERPATH = "D:\_DOCUMENTS\Code\chromedriver_win32\chromedriver.exe"
ls = []

def get_data():
    fieldnames = ['email', 'url', 'unique']
    with open('users.csv', newline='') as f:
        reader = DictReader(f, fieldnames=fieldnames)
        for user in reader:   
            img_scrape(user)
   
def img_scrape(user):
    email = user['email']
    email_stripped = ''.join(e for e in email if e.isalnum())
    userfolder = email_stripped + user['unique']
    url = user['url']
    #opens driver and provides url 
    driver = webdriver.Chrome(DRIVERPATH)   
    driver.get(url)
    #wait to ensure loading
    time.sleep(5)
    
    #return list of img elements
    elements = driver.find_elements_by_tag_name('img')
    for e in elements:
        img = e.get_attribute('src')
        
        filepath = r"images/" + userfolder + "/" 
        filename = filepath + img.split('/')[-1]
        
        #download images to images folder
        try:
            r = requests.get(img)
            if not os.path.exists(filepath):
                os.makedirs(filepath)
                
            with open(filename, "wb") as f:
                f.write(r.content)
            
            ls.append((filename, e.get_attribute('alt')))
            
        except:
            print("error downloading image")
    #close driver
    print(ls)
    driver.quit()
    

if __name__ == '__main__':
    get_data()
    
    for l in ls:
        print(l[1])
        try:
            detection.detect_text(l[0])
        except:
            print("error analysing image")