# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import HTMLTestReportCN
# 我下载了这个报告模板，然后放到了python\lib目录下，使用自带的就不要导入



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://192.168.1.252:8089/")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test0")
        driver.find_element_by_id("userpass").clear()
        driver.find_element_by_id("userpass").send_keys("0")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='热网监控系统'])[1]/following::span[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='楼栋计量分摊报表'])[1]/following::span[1]").click()
        driver.find_element_by_link_text(u"户费用计算").click()
        driver.find_element_by_id("select2-communitySelect-container").click() #点击搜索框
        time.sleep(2)
        driver.find_element_by_css_selector(".select2-search__field").send_keys('叶语湾') #输入内容

        time.sleep(3)
        print('选择好了')
       # driver.find_element_by_class_name('select2-results')
        print('什么')
        driver.find_element_by_xpath('//li[text()="叶语湾"]').click() #选择对象
        print('选择上去')
        time.sleep(1)

        driver.find_element_by_id("saveSeasonChargeButton").click()
        time.sleep(2)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='如已保存过季费用将会覆盖上一次季费用，确定要保存?'])[1]/following::button[1]").click()
        time.sleep(6)
        print('结束')

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

'''使用第三方的测试用例
if __name__ == "__main__":
    unittest.main()
'''
if __name__ == '__main__':
    filePath ='D:\\Report.html'       #确定生成报告的路径
    fp = open(filePath,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title=u'自动化测试报告', description='详细测试用例结果',tester=u"刘超" )
    #运行测试用例
    runner.run(UntitledTestCase('test_untitled_test_case'))
