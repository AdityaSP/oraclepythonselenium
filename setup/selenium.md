## Setup Selenium

#### - Step 1
Update pip
cd to the directory where python is installed. In my case its installed in "D:\sw\Python27\Scripts" and execute update for pip
``` sh

> cd D:\sw\Python27\Scripts
> python -m pip install -U pip setuptools

```
---

#### - Step 2
Install Selenium. While staying in the same Scripts directory as above, execute the below
``` sh

> pip install selenium

```
---

#### - Step 3
Verification. To make sure that Selenium is installed try the below command
``` sh

> pip show selenium

```
---

#### - Step 4
Webdrivers installation
Selenium requires WebDrivers to be installed. Download them from the below locations

| Browser | Webdriver link |
| ------ | ------ |
| Chrome | https://sites.google.com/a/chromium.org/chromedriver/downloads |
| Firefox | https://github.com/mozilla/geckodriver/releases |

#### - Step 5
Extract and add to path
Extract the downloaded webdrivers and store them in any location. Note the directory
Add the directory to PATH
> Right click on "This PC" -> Properties -> Advanced System Settings -> Environment Variables -> Edit Path in both System and User variables section
---

#### - Step 6
Verification
Close all your cmd prompt windows and open a fresh command prompt. type the below command and the web driver path should be visible as a part of PATH entry
``` sh

> echo %PATH%

```
