from selenium import webdriver
import urllib.request

from alternat.generation import Generator
generator = Generator()

DRIVERPATH = "D:\_DOCUMENTS\Code\chromedriver_win32\chromedriver.exe"

def img_scrape(url):
    driver = webdriver.Chrome(DRIVERPATH)
    driver.get(url) #insert website
    
    elements = driver.find_elements_by_tag_name('img')
    for e in elements:
        img = url + e.get_attribute('src')
        print(e.get_attribute ('alt'))
        
        filename = img.split('/')[-1]
        urllib.request.urlretrieve(img, filename)
        
def generate(img):
    generator.generate_alt_text_from_file(img, "results")
    



