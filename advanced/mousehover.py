'''
Created on Oct 12, 2017

@author: Dell lap
'''
from drivers import driver
from selenium.webdriver import ActionChains
import time
driver.get("http://localhost/mystore")
# get desktop element
# //a[contains(text(), 'Desktops')]
desktop = driver.find_element_by_xpath("//a[contains(text(), 'Desktops')]")
# create actions
action= ActionChains(driver)
# move to the element => mouse move != mouse click
action.move_to_element(desktop)
action.perform()
action.click(driver.find_element_by_partial_link_text("PC"))
action.perform()
#perform()
# perform is necessary

time.sleep(5)
driver.quit()
