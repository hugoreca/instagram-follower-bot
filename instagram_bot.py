from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

BINARY_LOCATION = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
options = Options()
options.binary_location = BINARY_LOCATION

class InstaBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options, executable_path=CHROME_DRIVER_PATH)

    def login(self, ig_url, ig_user, ig_pwd):
        self.driver.get(ig_url)
        time.sleep(2)
        self.user = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.user.send_keys(ig_user)
        self.pwd = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.pwd.send_keys(ig_pwd)
        self.login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        self.login_button.click()
        time.sleep(4)
        self.not_now_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        self.not_now_button.click()
        time.sleep(2)
        self.not_now_button2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        self.not_now_button2.click()
        time.sleep(2)




    def find_followers(self, similar_account):
        self.search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        self.search.send_keys(similar_account)
        time.sleep(2)
        self.account_location = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        self.account_location.click()
        time.sleep(4)


    def follow(self):
        self.followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        self.followers.click()
        time.sleep(2)
        self.modal = self.driver.find_element_by_css_selector('.isgrP')

        for i in range(30):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.modal)
            time.sleep(.8)


        self.followers = self.driver.find_elements_by_css_selector('.wo9IH .uu6c_ .Pkbci button')
        for self.button in self.followers:
            try:
                self.button.click()
                time.sleep(.8) #será qué es tan rápido que no agarra el pedo? 🤔

            except ElementClickInterceptedException:
                time.sleep(.6)
                self.cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                self.cancel_button.click()
                time.sleep(.5)

            finally:
                time.sleep(1)




