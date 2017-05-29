# -*- coding:utf-8 -*-

"""
正式录单页面

"""



from appium import webdriver
from time import sleep
from Libraries import excle
from Libraries import Logs
from Libraries import commons
from Libraries import snapshots
import sys
from selenium.common.exceptions import NoSuchElementException


class OfficialRecord():

    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)


    def DraftOfficialRecord(self):

        print("-----------------------------开始正式推单------------------------------")
        self.driver.find_element_by_id("com.rjs.ddjr:id/official_record").click()
        self.driver.implicitly_wait(2)

        # 个人信息模块
        print("个人信息页面，点击下一步")
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        self.driver.implicitly_wait(2)

        # 房产信息模块
        print("房产信息页面，点击下一步")
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        self.driver.implicitly_wait(2)

        # 车辆信息模块
        print("车辆信息页面，点击下一步")
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        self.driver.implicitly_wait(2)

        # 公司信息/ 企业信息/ 收入信息模块
        print("公司/企业/收入信息页面，点击下一步")
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        self.driver.implicitly_wait(2)

        # 联系人信息/父母子女信息模块
        print("联系人信息/父母子女信息信息页面，点击下一步")
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        self.driver.implicitly_wait(2)

        # 车辆照片信息模块
        print("车辆照片信息页面，点击下一步")
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        self.driver.implicitly_wait(2)

        # 提交单子
        print("开始提交单子")
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_submit").click()
        self.driver.implicitly_wait(3)
        print("--------------------------------推单成功------------------------------")







