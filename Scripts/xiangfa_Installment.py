# -*- coding:utf-8 -*-
from appium import webdriver
from time import sleep
from Scripts import xiangfa_Login
from Libraries import excle
from Libraries import Logs
import sys
from selenium.common.exceptions import NoSuchElementException

#from Appium_Automated_Testing.XiangFa.xiangfa_Login import APPLogin


class Installment():
    '''安装享发金融APK'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x=casepath
        self.y=logpath
        self.z=timestap
        self.m=picpath
        self.n=apppath
        self.driver=driver
        print(self.n)
        #xiangfa_Login.APPLogin(self.x, self.y, self.m, self.n, self.z,self.driver).login()

        self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.GuideActivity')
        self.driver.implicitly_wait(1000)
        sleep(20)

        self.driver.swipe(1000, 500, 0, 500)
        sleep(6)
        self.driver.swipe(1000, 500, 0, 500)
        sleep(6)
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/index_finish')
        el.click()
        sleep(6)
