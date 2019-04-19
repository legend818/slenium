# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time, re



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.12306.cn/index/")
        time.sleep(2)
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_link_text(u"账号登录").click()
        driver.find_element_by_id("J-userName").click()
        driver.find_element_by_id("J-userName").clear()
        driver.find_element_by_id("J-userName").send_keys("legend818")
        driver.find_element_by_id("J-password").click()
        driver.find_element_by_id("J-password").clear()
        driver.find_element_by_id("J-password").send_keys("94137344lc")
        time.sleep(10)
        # driver.find_element_by_id("J-loginImg").click()
        # driver.find_element_by_id("J-login").click()
        driver.find_element_by_link_text(u"首页").click()
        driver.find_element_by_id("fromStationText").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=isStudentDan | ]]

        driver.find_element_by_css_selector('#ul_list1 > li:nth-child(9)').click()

        print("出发地完成")
        time.sleep(2)
        # 目的地选择
        driver.find_element_by_id('toStationText').click()
        driver.find_element_by_xpath('//*[@id="ul_list1"]/li[1]').click()

        driver.find_element_by_id("query_ticket").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
