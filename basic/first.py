from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.google.com")

chromeDriver = webdriver.Chrome()
chromeDriver.get("http://www.google.com")
