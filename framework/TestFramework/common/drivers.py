'''
Created on Oct 11, 2017

@author: Dell lap
'''

from selenium import webdriver

class MyDriver(object):
    def __init__(self, browser="Chrome"):
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        else:
            self.driver = webdriver.Firefox()
             
    def get(self, url):
        self.driver.get(url)
    
    def find_element(self,locator, value):
        try:
            return self.driver.find_element(locator, value)
        except Exception as err:
            print "Couldnot find element",err
            self.quit()
            
    def quit(self):
        self.driver.quit()
    
    def title(self):
        return self.driver.title            