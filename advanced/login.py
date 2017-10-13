'''
Created on Oct 13, 2017

@author: Dell lap
'''
from drivers import driver
import time
driver.get("http://localhost/mystore/admin")

login = driver.find_element_by_id('input-username')
password = driver.find_element_by_id('input-password')
button = driver.find_element_by_xpath('//button')

login.send_keys("admin")
password.send_keys("admin")
button.click()

time.sleep(10)
driver.quit()
