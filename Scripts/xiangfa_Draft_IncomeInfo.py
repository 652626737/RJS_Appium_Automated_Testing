# -*- coding:utf-8 -*-

"""
收入信息页面

"""




from appium import webdriver
from time import sleep
from Libraries import excle
from Libraries import Logs
from Libraries import commons
from Libraries import snapshots
import sys
from selenium.common.exceptions import NoSuchElementException
from Scripts.xiangfa_Login import XiangfaLogin
from Scripts import xiangfa_Draft_PersonalInfo, xiangfa_Draft_DraftRecord


class IncomeInfo():
    '''登录后跳转到收入信息页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)



        # case执行和代码开发过程中试用关键字驱动 Auto_mlrc_IncomeInfo_005，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_IncomeInfo_005', "").searche_parameter_excel())
        print(paramstr)


        # # 如果存在参数，需要进行参数化
        self.income_source = commons._str_chuli_(paramstr, ',')[0]
        self.monthly_income = commons._str_chuli_(paramstr, ',')[1]



    def InputIncomeInfo(self):
        print('—————————————————————————————收入信息页面载入中，请稍后————————————————————————————')
        rsl = excle.excels(self.x, 'Auto_mlrc_IncomeInfo_005', "").searche_pth_excel()
        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))

        print("开始输入收入来源")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/income_source_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_info")
        el.clear()
        el.click()
        el.send_keys(self.income_source)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("收入来源已输入")

        print("开始输入每月收入")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/monthly_income_edit")
        el.clear()
        el.click()
        el.send_keys(self.monthly_income)
        self.driver.hide_keyboard()
        print("每月收入已输入")

        print("开始选择收入类型")
        self.driver.find_element_by_id("com.rjs.ddjr:id/income_certificate_text").click()
        # self.driver.implicitly_wait(1)
        self.driver.find_element_by_id("com.rjs.ddjr:id/rb_1").click()
        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_confirm").click()
        print("开始上传收入证明")
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id('com.rjs.ddjr:id/title_right_custom').click()
        print('收入证明上传成功！')

        print("开始上传央行征信报告")
        self.driver.find_element_by_id("com.rjs.ddjr:id/credit_report_text").click()
        # self.driver.implicitly_wait(1)
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id('com.rjs.ddjr:id/title_right_custom').click()
        print('央行征信报告上传成功！')

        self.driver.find_element_by_id("com.rjs.ddjr:id/draft_save").click()
        # self.driver.implicitly_wait(2)
        print("——————————————————————————草稿录单模块，收入信息页面已保存！——————————————————")

        # 评审修改时间2017/5/4
        # 加入检查点，并最终判断case执行的结果是通过还是不通过
        self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.HomeActivity')
      #  sleep(6)

        try:
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/main_btn_message")
            el.click()
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft")
            el.click()
            self.driver.implicitly_wait(1)
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/cheyidai_tab")
            el.click()
            el = self.driver.find_element_by_id('com.rjs.ddjr:id/draft_item_name')
            print(el.text)
            if el.text == "suzhoutest":
                flag = 'P'
            if el.text != "suzhoutest":
                flag = 'F'
            print(flag)



            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout")
            el.click()
            self.driver.find_element_by_id("com.rjs.ddjr:id/draft_income")
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_income_progress")
            print(el.text)
            if el.text == "完成:100％":
                flag = "P"
            if el.text != "完成:100％":
                flag = "F"
            print(flag)

            # 将结果写入到case和log日志中
            logstr = str(self.driver.get_log("logcat"))
            excle.excels(self.x, self.z, flag).write_excel(rsl, 10)
            Logs.logs(self.y, self.z, flag)._writ_file()
            Logs.logs(self.y, 'logcat', logstr)._writ_file()

            excle.excels(self.x, self.z, pic).write_excel(2, 11)
            #sleep(10)


        except:
            info = str(sys.exc_info())
            Logs.logs(self.y, self.z, info)._writ_file()