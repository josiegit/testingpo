# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from testingpo.login import Login
from testingpo.register import Register
from selenium import webdriver

class Index():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        #click login
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return Login(self.driver)

    def goto_register(self):
        #click register
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return Register(self.driver)

