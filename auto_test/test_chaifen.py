# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

split_dir = r'D:\importFile\新型农村社会养老保险.docx'
split_article_name = '新型农村社会养老保险'


class TestNotice:

    def __init__(self):
        self.vars = {}
        self.driver = webdriver.Chrome()
        self.handles = self.driver.window_handles

    def execute(self):
        self.test_login()
        self.test_split()

    # 用户登录
    def test_login(self):
        self.driver.get("http://172.16.9.43:7440/kbaseui-std/main.do")
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "j_username").send_keys("amos")
        self.driver.find_element(By.ID, "j_password").click()
        self.driver.find_element(By.ID, "j_password").send_keys("000000")
        self.driver.find_element(By.ID, "btnOk").click()
        qa_label = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, "kbsTabHome")))
        print("找到" + qa_label.text + "，登录成功")
        assert "首页" == qa_label.text

    # 首页测试

    # 文档拆分
    def test_split(self):
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a/label[.='拆分']").click()
        time.sleep(4)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//div[.='拆分']/../div/iframe"))
        self.driver.find_element_by_id("filebox_file_id_1").send_keys(split_dir)
        time.sleep(8)
        self.driver.find_element_by_xpath("//span/span[.='上传']").click()
        # self.driver.find_element_by_xpath("//a[@name='btnUpload'][@type='upload']").click()
        time.sleep(5)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(2)

        # noinspection PyBroadException
        try:
            self.driver.find_element_by_xpath(
                "//input[@id='articleName'][@value='" + split_article_name + "']").is_displayed()
            print("文档拆分成功")
        except:
            print("文档拆分失败")
        self.driver.close()
        self.handles = self.driver.window_handles
        self.driver.switch_to.window(self.handles[0])
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath(
            "//span/a[@class='layui-layer-ico layui-layer-close layui-layer-close1']").click()
        time.sleep(2)


# 执行入口
TestNotice().execute()
