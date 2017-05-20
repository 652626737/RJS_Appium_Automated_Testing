# -*- coding:utf-8 -*-

"""
联系人/直系亲属信息页面

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
from Scripts import xiangfa_Draft_PersonalInfo

class RelativiesInfo():
    '''登录后跳转到联系人信息页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)



        # case执行和代码开发过程中试用关键字驱动 Auto_mlrc_RelativiesInfo_006，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_RelativiesInfo_006', "").searche_parameter_excel())
        print(paramstr)


        # # 如果存在参数，需要根据
        self.relatives_name = commons._str_chuli_(paramstr, ',')[0]
        self.relatives_phone = commons._str_chuli_(paramstr, ',')[1]
        self.work_unit = commons._str_chuli_(paramstr, ',')[2]
        self.et_info = commons._str_chuli_(paramstr, ',')[3]




    def InputRelativiesInfo(self):
        print('—————————————————————————————联系人信息页面载入中，请稍后————————————————————————————')
        rsl = excle.excels(self.x, 'Auto_mlrc_RelativiesInfo_006', "").searche_pth_excel()
        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/relatives_name_edit")
        print("开始输入姓名")
        el.clear()
        el.click()
        el.send_keys(self.relatives_name)
        self.driver.hide_keyboard()
        print("姓名输入完成")

        print("开始输入联系电话")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/relatives_phone_edit")
        el.clear()
        el.click()
        el.send_keys(self.relatives_phone)
        print("联系电话输入完成")

        print("开始输入工作单位")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/work_unit_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_info")
        el.clear()
        el.click()
        el.send_keys(self.work_unit)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("工作单位输入完成")

        print("开始选择是否知晓贷款")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/known_loan_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()

        # 往上翻动
        self.driver.swipe(380, 1000, 380, 800)
        self.driver.implicitly_wait(1000)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("是否知晓贷款已选择")
        sleep(3)

        print("开始填写备注。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/relative_remark_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_info")
        el.clear()
        el.click()
        el.send_keys(self.et_info)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("备注填写完成")
        sleep(3)


        self.driver.find_element_by_id("com.rjs.ddjr:id/draft_save").click()
        sleep(3)
        print("——————————————————————————草稿录单模块，联系人信息页面已保存！——————————————————")

        try:
            # 评审修改时间2017/5/4
            # 加入检查点，并最终判断case执行的结果是通过还是不通过
            self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.HomeActivity')

            # 去掉升级，点击【工作台】按钮，进入草稿录单页面
            # el = self.driver.find_element_by_id("android:id/button2")
            # el.click()
            sleep(1)
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/main_btn_message")
            el.click()
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft")
            el.click()
            sleep(1)
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
            self.driver.find_element_by_id("com.rjs.ddjr:id/draft_relatives")
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_relatives_progress")
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
            sleep(10)



        except:
            info = str(sys.exc_info())
            Logs.logs(self.y, self.z, info)._writ_file()