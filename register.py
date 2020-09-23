# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

class Register():
    def __init__(self,driver: WebDriver):
        self.driver=driver
    def register(self):
        #send contents
        #click element
        sleep(2)
        self.driver.find_element(By.ID,"corp_name").send_keys("hihihi")
        self.driver.find_element(By.ID,'manager_name').send_keys("dahuanggou")
        sleep(3)
        pass

