'''
Created on Oct 13, 2017

@author: Dell lap
'''
from selenium.webdriver.common.by import By
from pages.base import Base
import json
class Login(Base):
    '''
    This is a Page Object Model for Admin login page
    '''
    def __init__(self, driver):
        self.d = driver
        self.get_config(r'C:\Users\Dell lap\eclipse-workspace\TestFramework\config\admin\login.json')

    def get_username(self):
        t = self.get_locator("username")
        return self.d.find_element(*t)
    
    def get_password(self):
        t = self.get_locator("password")
        return self.d.find_element(*t)
    
    def get_loginbutton(self):
        t = self.get_locator("button")
        return self.d.find_element(*t)

    def enter_username(self, username):
        self.get_username().send_keys(username)
    def enter_password(self, password):
        self.get_password().send_keys(password)
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.get_loginbutton().click()
            
            