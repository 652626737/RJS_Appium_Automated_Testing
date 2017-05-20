# -*- coding:utf-8 -*-

"""
草稿列表页面

"""


from appium import webdriver
from time import sleep
from Libraries import excle
from Libraries import Logs
import sys
from selenium.common.exceptions import NoSuchElementException
from Scripts.xiangfa_Login import XiangfaLogin
from Libraries import snapshots
from Libraries import commons


class DraftRecord():
    '''登录后跳转到个人页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver = driver
        print(self.n)
        self.driver.implicitly_wait(1000)

        # 先进行登录操作，修改APPLogin为XianfaLogin后，去掉APPLogin()方法
        XiangfaLogin(self.x, self.y, self.m, self.n, self.z,self.driver).login()

        self.driver.start_activity("com.rjs.ddjr", "com.rjs.ddjr.cheyidai.draft.view.DraftRecordActivity")
        sleep(8)

    def CheckDraftRecord(self):
        self.driver.find_element_by_id("com.rjs.ddjr:id/cheyidai_tab").click()
        sleep(1)


