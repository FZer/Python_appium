# -*- coding=utf-8 -*-
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common import actions

import time

desired_cap = {
  "platformName": "Android",
  "deviceName": "OPPO R11",
  "appPackage": "com.tencent.mm",
  "appActivity": "com.tencent.mm.ui.LauncherUI",
  "platformVersion": "5.1.1",
  "automationName": "UiAutomator2",
  "noReset": False
}
driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', desired_capabilities=desired_cap)
time.sleep(4)
TouchAction(driver).tap(x=139, y=1173).perform()
time.sleep(3)
TouchAction(driver).tap(x=244, y=570).perform()
time.sleep(2)
driver.find_element_by_android_uiautomator('text("请填写微信号/QQ号/邮箱")').send_keys("kler007")
time.sleep(2)
TouchAction(driver).tap(x=255, y=455).perform()
time.sleep(2)
passwd_id = driver.find_elements_by_id('com.tencent.mm:id/bhn')
time.sleep(2)
print(passwd_id)
passwd_id[1].send_keys("123@kler")  # 密码输入框没有唯一标签熟悉
# driver.keyevent(36)
#actions.sendKeys("123@kler").perform()#web页面使用，这里无法生效
time.sleep(3)
driver.find_element_by_android_uiautomator('text("登录")').click()
time.sleep(3)

#git第一次修改测试