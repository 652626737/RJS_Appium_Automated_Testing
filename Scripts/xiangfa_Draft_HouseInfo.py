# -*- coding:utf-8 -*-


"""
房产信息页面

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

class HouseInfo():
    '''登录后跳转到房产信息页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)



        # case执行和代码开发过程中试用关键字驱动Auto_mlrc_HouseInfo_003，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_HouseInfo_003', "").searche_parameter_excel())
        print(paramstr)


        # 如果存在参数，需要根据参数传值




    def InputHouseInfo(self):
        print('—————————————————————————————房产信息页面载入中，请稍后————————————————————————————')
        rsl = excle.excels(self.x, 'Auto_mlrc_HouseInfo_003', "").searche_pth_excel()

        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))

        # 选择是，显示其他字段并进行输入
        print('开始选择本人名下是否有本地商品房')
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/has_house_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()
        # sleep(3)

        # print("本人名下是否有房：是")
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        # el.click()
        # print("本人名下有住房")
        # sleep(3)
        #
        # print("开始输入房产地址。。。。。")
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/house_address_text")
        # el.click()
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/cb_asCardAddr")
        # el.click()
        # print("房产地址输入成功")
        # sleep(3)
        #
        # print("开始选择房产状态。。。。。")
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/house_status_text")
        # el.click()
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/cb_asCardAddr")
        # el.click()
        #
        # # 往上滑动
        # self.driver.swipe(400, 1000, 400, 900)
        # sleep(3)
        #
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        # el.click()
        # print("房产状态已选择")
        # sleep(3)
        #
        # print("开始勾选房产资料类型。。。。。")
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/house_images_text")
        # el.click()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/rb_2").click()
        # self.driver.find_element_by_id("com.rjs.ddjr:id/tv_confirm").click()
        # sleep(3)
        # print("开始点击房产图片，进行上传。。。。。")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print('房产照片上传成功！')
        #
        # self.driver.find_element_by_id("com.rjs.ddjr:id/info_auth_layout").click()
        # self.driver.swipe(400,100,400,800)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom").click()
        # self.driver.implicitly_wait(1000)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/next_step").click()
        # sleep(1)
        # print("——————————————————————————草稿录单模块，房产信息页面已保存！——————————————————")




        # 选择否，直接保存该页面
        self.driver.swipe(400, 1000, 400, 800)
        print("本人名下是否有房：否")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("本人名下没有住房")
        self.driver.find_element_by_id("com.rjs.ddjr:id/next_step").click()
        #sleep(3)
        print("——————————————————————————草稿录单模块，房产信息页面已保存！——————————————————")

        # 评审修改时间2017/5/4
        # 加入检查点，并最终判断case执行的结果是通过还是不通过
        self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.HomeActivity')
        #sleep(6)




        try:
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/main_btn_message")
            el.click()
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft")
            el.click()
           # sleep(1)
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
            self.driver.find_element_by_id("com.rjs.ddjr:id/draft_house")
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_house_progress")
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

