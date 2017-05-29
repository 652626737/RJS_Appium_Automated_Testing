# -*- coding:utf-8 -*-

"""
车辆照片页面

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

class CarPhoto():
    '''登录后跳转到联系人信息页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)



        # case执行和代码开发过程中试用关键字驱动 Auto_mlrc_CarPhoto_007，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_CarPhoto_007', "").searche_parameter_excel())
        print(paramstr)


        # 如果存在参数，需要进行参数化




    def InputCarPhotoInfo(self):
        print('—————————————————————————————车辆照片页面载入中，请稍后————————————————————————————')
        rsl = excle.excels(self.x, 'Auto_mlrc_CarPhoto_007', "").searche_pth_excel()
        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))

        # # 车主与车辆照片
        # print("开始上传车主与车辆照片。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("车主与车辆照片上传成功")
        #
        # # 车前45度照
        # print("开始上传车前45度照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("车前45度照上传成功")
        #
        # # 正后照
        # print("开始上传正后照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("正后照上传成功")
        #
        #
        # ########################################### 往上滑动一次,每次只划过三个###################################
        # self.driver.swipe(400, 1088, 400, 260)
        #
        #
        #
        # # 后尾厢照
        # print("开始上传后尾厢照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("后尾厢照上传成功")
        #
        # # 主驾门叶照
        # print("开始上传主驾门叶照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("主驾门叶照上传成功")
        #
        # # 主驾驶侧照
        # print("开始上传主驾驶侧照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("主驾驶侧照上传成功")
        #
        #
        # ########################################### 往上滑动一次,每次只划过三个###################################
        # self.driver.swipe(400, 1022, 400, 143)
        #
        #
        # # 主驾驶正照
        # print("开始上传主驾驶正照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("主驾驶正照上传成功")
        #
        # # 左方向盘照
        # print("开始上传左方向盘照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("左方向盘照上传成功")
        #
        # # 右方向盘照
        # print("开始上传右方向盘照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("右方向盘照上传成功")
        #
        #
        #
        # ########################################### 往上滑动一次,每次只划过三个###################################
        # self.driver.swipe(400, 1022, 400, 143)
        #
        #
        # # 后内饰照
        # print("开始上传后内饰照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("后内饰照上传成功")
        #
        # # 仪表盘照
        # print("开始上传仪表盘照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("仪表盘照上传成功")
        #
        # # 铭牌照
        # print("开始上传铭牌照。。。。。")
        # self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        # sleep(3)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        # sleep(2)
        # self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        # sleep(6)
        # print("铭牌照上传成功")
        #
        # self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        # sleep(3)
        # print("——————————————————————————草稿录单模块，车辆照片信息页面已保存！——————————————————")



        #################################################################################     使用以下新的代码   ################################################################################


        # 车主与车辆照片
        print("开始上传车主与车辆照片")
        self.driver.find_element_by_id("com.rjs.ddjr:id/car0").click()
    #    sleep(2)
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()
     #   sleep(6)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
      #  sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
       # sleep(6)
        print("车主与车辆照片上传成功")


        ########### 往上滑动一次##########
        self.driver.swipe(400, 502, 400, 142)


        # 车前45度照
        print("开始上传车前45度照")
        self.driver.find_element_by_id("com.rjs.ddjr:id/car1").click()
        #sleep(2)
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("车前45度照上传成功")



        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 141)

        # 正后照
        print("开始上传正后照")
        self.driver.find_element_by_id("com.rjs.ddjr:id/car2").click()
        #sleep(2)
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("正后照上传成功")


        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 143)


        # 后尾厢照
        print("开始上传后尾厢照")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/car3").click()
        # sleep(2)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()

        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("后尾厢照上传成功")


        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 143)




        # 主驾门叶照
        print("开始上传主驾门叶照")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/car4").click()
        # sleep(2)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()

        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("主驾门叶照上传成功")


        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 141)


        # 主驾驶侧照
        print("开始上传主驾驶侧照")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/car5").click()
        # sleep(2)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()

        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("主驾驶侧照上传成功")


        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 148)



        # 主驾驶正照
        print("开始上传主驾驶正照")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/car6").click()
        # sleep(2)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()

        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
       # sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("主驾驶正照上传成功")



        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 138)



        # 左方向盘照
        print("开始上传左方向盘照")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/car7").click()
        # sleep(2)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()

        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("左方向盘照上传成功")


        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 141)


        # 右方向盘照
        print("开始上传右方向盘照")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/car8").click()
        # sleep(2)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/iv_car").click()

        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("右方向盘照上传成功")



        ########### 往上滑动一次##########
        self.driver.swipe(400, 434, 400, 141)


        # 后内饰照
        print("开始上传后内饰照。。。。。")
        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("后内饰照上传成功")


        # 仪表盘照
        print("开始上传仪表盘照。。。。。")
        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("仪表盘照上传成功")


        # 铭牌照
        print("开始上传铭牌照。。。。。")
        self.driver.find_element_by_xpath("//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
        #sleep(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        #sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        #sleep(6)
        print("铭牌照上传成功")

        self.driver.find_element_by_id("com.rjs.ddjr:id/tv_next").click()
        #sleep(3)
        print("——————————————————————————草稿录单模块，车辆照片信息页面已保存！——————————————————")

        # 评审修改时间2017/5/4
        # 加入检查点，并最终判断case执行的结果是通过还是不通过
        self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.HomeActivity')
        #sleep(6)




        try:
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/main_btn_message")
            el.click()
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft")
            el.click()
#            sleep(1)
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
            self.driver.find_element_by_id("com.rjs.ddjr:id/draft_car_photo")
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_car_photo_progress")
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
 #           sleep(10)


        except:
            info = str(sys.exc_info())
            Logs.logs(self.y, self.z, info)._writ_file()
