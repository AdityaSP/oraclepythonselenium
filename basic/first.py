'''
Created on Oct 11, 2017

@author: Dell lap
'''
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/seleniumtrials/formelements.html")

#finding element
#find by id
element = driver.find_element_by_id('textinput')
print "Found Element with id textinput"

#find by name

element = driver.find_element_by_name('singlebutton')
print "Found Element with name singlebutton"

#find by xpath

xpath_list = [
    '/html/body/p[2]',
    "/html/body/form[contains(@class, 'form-horizontal')]/fieldset/div[contains(@class, 'form-group')][1]/div[contains(@class, 'col-md-4')]/input[@id='textinput']",
    "//input[@id='textinput']",
    "//button[@class='btn btn-primary']",
    "//button[contains(@class,'btn') and contains(@class, 'btn-primary')]",
    "//button[text() = 'Try it']",
    "//*[contains(text() , 'started')]",
    "//input[@id='radios-3']//parent::label//preceding-sibling::label[1]/input",
    "//input[@id='radios-0']//parent::label//following-sibling::label[1]/input",
    "//input[@id='radios-3']/../preceding::label",
    "//input[@id='radios-3']/../following::label",
    "//input[@id='radios-3']/../descendant::input",
    "//input[@id='radios-0']//parent::label//following-sibling::label[1]/input",
    "//input[@id='radios-3']//parent::label//preceding-sibling::label[1]/input"
    ]

for xpath in xpath_list :
    element = driver.find_element_by_xpath(xpath)
    print "found element for " , xpath


# find by link text

element = driver.find_element_by_link_text('Print')
print "found element with link text "

# find by partial link text
element = driver.find_element_by_partial_link_text('Pri')
print "found element with partial link text "

# find by class name
element = driver.find_element_by_class_name('btn-primary')
print "found element by class name "

# find by tag name
element = driver.find_element_by_tag_name('p')
print "found element by tagname p: " , element.text


# generic find element
driver.find_element(value='textinput')

from selenium.webdriver.common.by import By
driver.find_element(by=By.NAME, value='singlebutton')

# browser interactions

# maximize a windows

# get the title

# get the current url

# refresh

# A second refresh

# back

# forward

# page_source

# close

# quit
