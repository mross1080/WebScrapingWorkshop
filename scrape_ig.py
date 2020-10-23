from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os

from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


taggee_class = "_hli"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path=DRIVER_BIN)

# Begin Template Code

driver.get('https://www.instagram.com/accounts/login/?hl=en')

print("Opened instagram")

sleep(1)

username_box = driver.find_element_by_name('username')
username_box.send_keys("mr5144@nyu.edu")
print("Email Id entered")

password_box = driver.find_element_by_name('password')
password_box.send_keys("clouds4Carol!")
print("Password entered")
#

login_box = driver.find_elements(By.XPATH, '//button')[1]
login_box.click()
#
sleep(1)

hashtag = "babyyoda"
hashtag_url = "https://www.instagram.com/explore/tags/{}/?hl=en".format(hashtag)

print("Opening {}".format(hashtag_url))
sleep(4)
driver.get(hashtag_url)
sleep(1)
print("Browsing Photos for Hashtag {}".format(hashtag))

sleep(.5)


outF = open("{}photourls.txt".format(hashtag), "w")


while True:
    page_elements = driver.find_elements(By.XPATH, '//img')
    print("{} many elements on the page ".format(len(page_elements)))

    # Scroll to next area of page and load in new images
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(1)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(new_height)


    try:
        soup_a = BeautifulSoup(driver.page_source, "html.parser")
        for link in soup_a.find_all('img'):
            # link.get('href') gets the href/url out of the a element
            print(link.get('src'))
            outF.write(link.get('src'))
            outF.write("\n")
        last_src_current_page = page_elements[-1].get_property("src")
        print(last_src_current_page)


    except Exception as e:
        print(e)


sleep(1)
print("starting iteration ")





