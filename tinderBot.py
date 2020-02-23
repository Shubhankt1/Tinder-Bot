import json
from time import sleep
from selenium import webdriver
from cryptography.fernet import Fernet

class TinderBot():
    def __init__(self):
        self.myDriver = webdriver.Chrome('/usr/local/bin/chromedriver_linux64/chromedriver')
    
    def login(self, eid, pw):
        self.myDriver.get('https://tinder.com')
        sleep(5)
        fb_login = self.myDriver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[2]/button')
        fb_login.click()
        base_window = self.myDriver.window_handles[0]
        sleep(2)
        self.myDriver.switch_to_window(self.myDriver.window_handles[1])
        emailID = self.myDriver.find_element_by_xpath('//*[@id="email"]')
        emailID.send_keys(eid)
        passw = self.myDriver.find_element_by_xpath('//*[@id="pass"]')
        passw.send_keys(pw)
        login_but = self.myDriver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_but.click()
        sleep(2)
        self.myDriver.switch_to_window(base_window)
        allow_but = self.myDriver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_but.click()
        sleep(2)
        enable_notif = self.myDriver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_notif.click()
        sleep(3)
        self.autoSwipe()

    def like(self):
        like_but = self.myDriver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_but.click()

    def dislike(self):
        dislike_but = self.myDriver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_but.click()
    
    def autoSwipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    out_of_likes = self.myDriver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[1]')
                    out_of_likes.click()
                    self.myDriver.quit()
                except Exception:
                    sleep(5)

    def startSwipe(self):
        with open('cred.config') as config:
            Config = json.load(config)
        eid = Config["username"]
        key = Config["key"]
        cipher_suite = Fernet(key)
        pw = bytes(cipher_suite.decrypt(Config["pwHash"].encode())).decode("utf-8")
        self.login(eid,pw)