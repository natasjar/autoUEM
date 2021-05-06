# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:07:42 2021

@author: natasja
"""
from csv import DictReader, DictWriter

def check_info(email,url):
    fieldnames = ['email', 'url', 'unique']
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
        "unique": unique
        }
    
    with open('users.csv', 'a', newline='') as f:
        writer = DictWriter(f, fieldnames=fieldnames)
        
        writer.writerow(user)
        
        f.close()