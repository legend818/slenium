
from selenium import webdriver
from time import sleep

#打开谷歌浏览器
driver=webdriver.Chrome()
#设置浏览器窗口大小
driver.set_window_size(1080,800)
#设置全局操作超时时间
driver.implicitly_wait(10)
#打开网址
driver.get("https://www.12306.cn/index")

sleep(3)

driver.find_element_by_css_selector("#J-header-login > a:nth-child(1)").click()
print("切换到登陆页面成功")
sleep(1)
driver.find_element_by_link_text("账号登录").click()
sleep(3)
#输入用户名
driver.find_element_by_id('J-userName').send_keys("legend818")
#输入密码
driver.find_element_by_id('J-password').send_keys("94137344lc")
#验证码不会，这里需要手动输入操作
sleep(10)
driver.find_element_by_name("g_href").click()

print("车票预定界面")
#出发地选择
driver.find_element_by_id('fromStationText').click()
driver.find_element_by_css_selector('#ul_list1 > li:nth-child(9)').click()
#driver.find_element_by_css_selector(u'[titlle=广州]').click()
print("出发地完成")
sleep(2)
#目的地选择
driver.find_element_by_id('toStationText').click()
driver.find_element_by_xpath('//*[@id="ul_list1"]/li[1]').click()
print("目的地完成")
sleep(2)
#选择出发日期
driver.find_element_by_id('train_date').click()
sleep(2)
driver.find_element_by_css_selector('body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(13) > div').click()
#driver.find_element_by_css_selector('body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(13) > div').click()
driver.find_element_by_css_selector('body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(17) > div').click()

print("选择日期")

sleep(2)
#查询
driver.find_element_by_id('search_one').click()
print("查询结束")
sleep(2)
print('开始查询')
driver.switch_to_window(driver.window_handles[1])
# 数字1代表第一个
# 这些方法都被编辑器划伤了一条横线，但是方法还是可以正常使用，只是目前的pycharm不推荐你继续这样使用了（有新的方法可以替代它）
#这个是因为新页面打开，存在找不到新页面的元素，所以使用了上面的方法
#循环刷票

while True:
    try:

        driver.find_element_by_id('query_ticket').click()
        e = driver.find_element_by_xpath('//*[@id="ZE_6k0000D92200"]/div')
        e.click()
        if e.text in [u"无","--"]:
            print("nono")
            sleep(1)
        else:
            print("yes")
    except:
        pass

