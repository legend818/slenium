from selenium import webdriver
import unittest,time

class login():

    def browserstart(self,url):
        self.driver = webdriver.Firefox()
        time.sleep(1)
        browse = self.driver.get(url)


    def login(self,uname,psw):
        usname = self.driver.find_element_by_id('username').send_keys(uname)
        psword = self.driver.find_element_by_id('userpass').send_keys(psw)
        submit = self.driver.find_element_by_id('loginBtn').click()
        time.sleep(2)
        quitbu = self.driver.find_element_by_class_name('caret').click()
        quitqu = self.driver.find_element_by_id('loginExit').click()

    def logout(self):
        self.quitbu = self.driver.find_element_by_class_name('caret').click()
        self.quitqu = self.driver.find_element_by_id('loginExit').click()

t = login()
t.browserstart('http://192.168.1.252:8089')
t.login('kk','8')

