from common.drivers import MyDriver
from pages.admin.login import Login

mydriver = MyDriver()
mydriver.get("http://localhost/mystore/admin")
loginpage = Login(mydriver)
loginpage.login("admin", "admin")

try:
    assert mydriver.title() == 'Dashboard'
except AssertionError as err:
    print "Testcase failed: ", mydriver.title()
    mydriver.quit()
    raise err
    
print "Testcase successful"       

# if driver.title == 'Dashboard':
#     print "Success"
# else:
#     raise AssertionError("Login failed")    

mydriver.quit()