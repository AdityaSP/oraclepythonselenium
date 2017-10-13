'''
Created on Oct 13, 2017

@author: Dell lap
'''
import json
from selenium.webdriver.common.by import By

class Base(object):
    
    def get_config(self, fpath):
        fh = open(fpath)
        self.config = json.loads(fh.read())
        
    def get_locator(self, name):
        if self.config[name][0] == "ID":
            t = (By.ID, self.config[name][1])
            return t
        elif self.config[name][0] == "XPATH" :
            t = (By.XPATH, self.config[name][1])
            return t