'''
Created on Oct 11, 2017

@author: Dell lap
'''

from drivers import driver
import time
driver.get("http://localhost/seleniumtrials/formelements.html")
# get the current window handle

driver.find_element_by_xpath("//button[text()='Try it']").click()

#get all the handles

#switch to the newly created handle

# maximize and close 

# switch back to original handle
time.sleep(5)
driver.quit()
