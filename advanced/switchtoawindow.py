'''
Created on Oct 12, 2017

@author: Dell lap
'''
'''
Created on Oct 11, 2017
@author: Dell lap
'''

from drivers import driver
import time
driver.get("http://localhost/seleniumtrials/formelements.html")
# get the current window handle

print driver.title

#get all the handles
primary_handle = driver.current_window_handle
print primary_handle


driver.find_element_by_xpath("//button[text()='Try it']").click()

afterclick = driver.current_window_handle
print afterclick

handles = driver.window_handles
#switch to the newly created handle
for handle in handles:
    if handle != primary_handle:
        driver.switch_to.window(handle)
        driver.maximize_window()
        time.sleep(5)
        driver.close()

driver.switch_to.window(primary_handle)
time.sleep(5)
driver.find_element_by_partial_link_text('alert').click()
alert = driver.switch_to.alert

print alert.text
time.sleep(5)
alert.accept()

driver.quit()
