from drivers import driver
from selenium.webdriver import ActionChains
import time
driver.get("http://localhost/mystore")
# get desktop element
# //a[contains(text(), 'Desktops')]
# create actions
# move to the element => mouse move != mouse click
# perform is necessary

time.sleep(5)
driver.quit()
