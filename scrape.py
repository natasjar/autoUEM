from selenium import webdriver
import requests
import time
import os

DRIVERPATH = "D:\_DOCUMENTS\Code\chromedriver_win32\chromedriver.exe"

def img_scrape(url, filepath):    
    image_filepath = filepath + "images/"
    
    #opens driver and provides url 
    driver = webdriver.Chrome(DRIVERPATH)   
    driver.get(url)
    #wait to ensure loading
    time.sleep(2)
    
    #return list of img elements
    all_elements = driver.find_elements_by_tag_name('img')
    decorative_elements = driver.find_elements_by_css_selector('img[alt=""]')
    elements = list(set(all_elements) - set(decorative_elements))
    
    all_images = []
      
    for e in elements:
        img_alt = e.get_attribute('alt')
        if img_alt:
            alt_class = "described"
        elif not img_alt:
            alt_class = "undescribed"
    
        
        img = e.get_attribute('src')
        
        filename = image_filepath + img.split('/')[-1]
        if not os.path.exists(image_filepath):
                os.makedirs(image_filepath)
        
        #download images to images folder
        try:
            r = requests.get(img)
            #print(filename)
            with open(filename, "wb") as f:
                f.write(r.content)
            
            #included in the try so only valid get added to the filepath list
            image = {
                "filename": img.split('/')[-1],
                "alt_class": alt_class,
                "alt_text": img_alt,
                "contains_text": False,
                }
            
            all_images.append(image)
            
        except:
            print("error downloading image")
    
    for e in decorative_elements:
        img_alt = e.get_attribute('alt')
        alt_class = "decorative"
        
        img = e.get_attribute('src')
        filename = image_filepath + img.split('/')[-1]
        if not os.path.exists(image_filepath):
                os.makedirs(image_filepath)
        
        #download images to images folder
        try:
            r = requests.get(img)
            #print(filename)
            with open(filename, "wb") as f:
                f.write(r.content)
            
            #included in the try so only valid get added to the filepath list
            image = {
                "filename": img.split('/')[-1],
                "alt_class": alt_class,
                "img_alt": img_alt
                }
            
            all_images.append(image)
            
        except:
            print("error downloading image")
    #close driver
    driver.quit()
    return all_images



    

    
    