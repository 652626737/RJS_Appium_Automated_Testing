# -*- coding:utf-8 -*-





import sys
from appium import webdriver
from time import sleep
from Libraries import excle
from Libraries import commons
from Libraries import Logs
from Libraries import snapshots
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class XiangfaLogin():
    '''账户登录'''
    #评审修改时间2017/5/4
    #case定义规范，至少需要试用统一的定义casepath,logpath和timestap
    def __init__(self,casepath,logpath,picpath,apppath,timestap,driverkey):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver = driverkey

        #desired_caps['appPackage'] = 'com.rjs.ddjr'
        #desired_caps['appActivity'] = 'com.rjs.ddjr.publicmodel.view.LoginActivity'

        # 评审修改时间2017/5/4
        #路径需要使用相对路径，避免绝对路径

        # 进行登录操作
        print("——————————————————————————————即将进行用户登录操作——————————————————————————————————")

        self.driver.start_activity('com.rjs.ddjr','com.rjs.ddjr.publicmodel.view.LoginActivity')
        # sleep(6)


        # 评审修改时间2017/5/4
        #case执行和代码开发过程中试用关键字驱动Auto_mlrc_login_001，同时获取用例data
        paramstr = excle.excels(self.x,'Auto_mlrc_login_001',"").searche_parameter_excel()
        print(paramstr)

        # 评审修改时间2017/5/4
        #如果存在参数，需要根据
        self.name = commons._str_chuli_(paramstr, ',')[0]
        self.passwd = commons._str_chuli_(paramstr, ',')[1]


    def login(self):
        rsl = excle.excels(self.x, 'Auto_mlrc_login_001', "").searche_pth_excel()

        # 评审修改时间2017 / 5 / 4
        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))

        el_account = self.driver.find_element_by_id('com.rjs.ddjr:id/login_phone')
        el_account.click()
        el_account.send_keys(self.name)
        print('手机号输入成功')
        el_password = self.driver.find_element_by_id('com.rjs.ddjr:id/login_password')
        el_password.click()
        el_password.send_keys(self.passwd)
        print('密码输入成功')
        self.driver.hide_keyboard()
        el_login = self.driver.find_element_by_id('com.rjs.ddjr:id/login_commit')
        el_login.click()

        # 登录成功后
        print('——————————————————————————————登录成功————————————————————————————————')


        # 评审修改时间2017/5/4
        # 加入检查点，并最终判断case执行的结果是通过还是不通过
        self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.HomeActivity')
        # sleep(10)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/main_btn_myset")
        el.click()

        try:
            # 查找手机号，判断是否为登录账户
            el = self.driver.find_element_by_id('com.rjs.ddjr:id/head_phone')
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/head_layout")
            el.click()
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/person_phone")
            print(el.text)
            if el.text == "13063835945":
                flag = 'P'
            if el.text != "13063835945":
                flag = 'F'
            # 评审修改时间2017/5/4
            print(flag)

            # 将结果写入到case和log日志中
            logstr = str(self.driver.get_log("logcat"))
            excle.excels(self.x, self.z, flag).write_excel(rsl, 10)
            Logs.logs(self.y, self.z, flag)._writ_file()
            Logs.logs(self.y, 'logcat', logstr)._writ_file()

            excle.excels(self.x, self.z, pic).write_excel(2, 11)


        except:
            info = str(sys.exc_info())
            Logs.logs(self.y, self.z, info)._writ_file()



