# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNotice:

    def __init__(self):
        self.vars = {}
        self.driver = webdriver.Chrome()
        self.handles = self.driver.window_handles

    def execute(self):
        self.test_login()

    # 用户登录
    def test_login(self):
        self.driver.get("https://www.baidu.com/")
        # self.driver.maximize_window()
        self.driver.find_element(By.ID, "kw").send_keys("中国经济开门稳来之不易")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(20)


# 执行入口
TestNotice().execute()
