# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from testingpo.register import Register


class Login():
    def __init__(self,driver: WebDriver):
        self.driver=driver
        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()

    def scanf(self):
        pass
    def goto_register(self):
        #click register
        return Register(self.driver)
