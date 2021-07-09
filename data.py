# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:07:42 2021

@author: natasja
"""
from csv import DictReader, DictWriter
fieldnames = ['email', 'url', 'unique', 'done']

#used in main (flask form)
def store_info(email,url):
    
    with open('users.csv', newline='') as f:
        reader = DictReader(f, fieldnames=fieldnames)
        unique = 0
        if reader:
            for row in reader:            
                if row['email'] == email:
                    unique = int(row['unique']) + 1
    user = {
        "email": email,
        "url": url,
        "unique": unique,
        "done": False
        }
    
    with open('users.csv', 'a', newline='') as f:
        writer = DictWriter(f, fieldnames=fieldnames)
        
        writer.writerow(user)
        f.close()
        
def get_data():
    to_scrape = []
    data = []
    with open('users.csv', newline='') as f:
        reader = DictReader(f, fieldnames=fieldnames)
        for row in reader:
            data.append(row)
            if row['done'] == "False":
                to_scrape.append(row)
                
    with open('users.csv', 'w', newline='') as f:
        writer = DictWriter(f, fieldnames=fieldnames)
        for d in data:
            d['done'] = True
            writer.writerow(d)
        f.close()
    return to_scrape
    