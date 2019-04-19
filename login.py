# -*- coding: utf-8 -*-
from selenium import webdriver
import time

class login():
    def setUp(self,url):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = self.driver.get(url)
        time.sleep(2)

    def test_untitled_test_case(self,usname,pwd):

        self.driver.find_element_by_id("username").click()
        self.driver.find_element_by_id("username").clear()
        uname =  self.driver.find_element_by_id("username").send_keys(usname)
       
        psword = self.driver.find_element_by_id("userpass").send_keys(pwd)
        self.driver.find_element_by_id("loginBtn").click()
        self.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='系统管理员1'])[1]/following::b[1]").click()
        self.driver.find_element_by_id("loginExit").click()



t = login()
t.setUp('http://192.168.1.252:8089')
t.test_untitled_test_case('kk','8')

