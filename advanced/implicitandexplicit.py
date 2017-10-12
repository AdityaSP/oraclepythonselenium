'''
Created on Oct 12, 2017

@author: Dell lap
'''
from drivers import driver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
# open make mytrip
driver.get("https://www.makemytrip.com/")

# implicit wait

# autocompletion from new delhi
#//input[@id='hp-widget__sfrom
#//div[contains(@class, 'locationFilter autocomplete_from')]//span[contains(text(),'New Delhi')]

# enter Kolkata
#//input[@id='hp-widget__sTo']
#//div[contains(@class, 'locationFilter autocomplete_to')]//span[contains(text(),'Mumbai')]

# select depart date
#//div[contains(@class, 'dateFilter hasDatepicker')]/div[contains(@class, 'ui-datepicker-inline ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all ui-datepicker-multi ui-datepicker-multi-2')]/div[contains(@class, 'ui-datepicker-group ui-datepicker-group-first')]/table[contains(@class, 'ui-datepicker-calendar')]//a[text()='28']

# click on search
# searchBtn

# click on 1 stop
# stops_1_dep

time.sleep(10)
driver.quit()
