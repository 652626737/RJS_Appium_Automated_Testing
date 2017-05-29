# -*- coding:utf-8 -*-



"""
车辆信息页面

"""




from appium import webdriver
from time import sleep
from Libraries import excle
from Libraries import Logs
from Libraries import commons
from Libraries import snapshots
import sys
import random
from selenium.common.exceptions import NoSuchElementException
from Scripts.xiangfa_Login import XiangfaLogin
from Scripts import xiangfa_Draft_PersonalInfo

class VehicleInfo():
    '''登录后跳转到车辆信息页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)



        # case执行和代码开发过程中试用关键字驱动Auto_mlrc_VehicleInfo_004，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_VehicleInfo_004', "").searche_parameter_excel())
        print(paramstr)


        # # 如果存在参数，需要根据
        # self.license_plate = commons._str_chuli_(paramstr, ',')[0]
        self.vehicle_identification_code = commons._str_chuli_(paramstr, ',')[0]
        self.engine_number = commons._str_chuli_(paramstr, ',')[1]
        self.vehicle_type = commons._str_chuli_(paramstr, ',')[2]
        self.purchase_price = commons._str_chuli_(paramstr, ',')[3]
        self.mortgage_number = commons._str_chuli_(paramstr, ',')[4]






    def InputVehicleInfo(self):
        print('—————————————————————————————车辆信息页面载入中，请稍后————————————————————————————')
        rsl = excle.excels(self.x, 'Auto_mlrc_VehicleInfo_004', "").searche_pth_excel()

        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))

        print('开始上传行驶证主页')
        self.driver.find_element_by_id("com.rjs.ddjr:id/driving_license_page").click()
        # self.driver.implicitly_wait(3)
        print("开始勾选图片，进行上传。。。。。")
        # self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v7.widget.RecyclerView[1]/android.widget.RelativeLayout[2]/android.widget.ImageView[2]").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(10)
        print('行驶证主页上传成功！')

        print("开始输入车牌")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/license_plate_text")
        el.click()
        # 选择代号
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/tv_1")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/tv_item_filter")
        el.click()
        # 选择字母
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/tv_2")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/tv_item_filter")
        el.click()
        # 选择号码
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_num")
        el.clear()
        el.click()

        # 随机读取车牌号，并写入到字段中
        license_random = random.randint(10000,999999)
        print(license_random)
        el.send_keys(license_random)

        self.driver.hide_keyboard()
        # 保存车牌
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("车牌号码已输入")
        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/registration_date_text")
        el.click()
        print("开始选择注册日期。。。。。")
        el = self.driver.find_element_by_id("android:id/numberpicker_input")
        el.click()

        # 往下翻动，选择年份（年份越来越小）
        self.driver.swipe(140, 1000, 140, 1160)
        # self.driver.swipe(360, 1000, 360, 1160)
        # self.driver.swipe(560, 1000, 560, 1160)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("注册日期已选择")
        self.driver.implicitly_wait(1)

        print("开始选择发证日期。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/date_of_issue_text")
        el.click()
        # self.driver.implicitly_wait(1)
        el = self.driver.find_element_by_id("android:id/numberpicker_input")
        el.click()
        # 往下翻动，选择年份（年份越来越小）
        self.driver.swipe(140, 1000, 140, 1160)
        # self.driver.swipe(360, 1000, 360, 1160)
        # self.driver.swipe(560, 1000, 560, 1160)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("发证日期已选择")
        self.driver.implicitly_wait(1)

        print('开始输入车辆识别码')
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/vehicle_identification_code_edit")
        el.clear()
        el.click()
        el.send_keys(self.vehicle_identification_code)
        self.driver.hide_keyboard()
        print('车辆识别码已输入')
        self.driver.implicitly_wait(1)

        print('开始输入发送机号码')
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/engine_number_edit")
        el.clear()
        el.click()
        el.send_keys(self.engine_number)
        self.driver.hide_keyboard()
        print('发动机号码已选择')
        self.driver.implicitly_wait(1)

        print('开始输入车辆类型')
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/vehicle_type_edit")
        el.clear()
        el.click()
        el.send_keys(self.vehicle_type)
        self.driver.hide_keyboard()
        print('车辆类型已输入')
        self.driver.implicitly_wait(1)

        # 往下滑动一次
        self.driver.swipe(300, 1000, 300, 500)
        self.driver.swipe(300, 1000, 300, 500)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/driving_vice_text")
        el.click()
        print("开始点击行驶证副页，进行上传。。。。。")
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id('com.rjs.ddjr:id/title_right_custom').click()
        print('行驶证副页上传成功！')
        self.driver.implicitly_wait(1)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/vehicle_registration_certificate_text")
        el.click()
        print("开始点击车辆登记证，进行上传。。。。。")
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id('com.rjs.ddjr:id/title_right_custom').click()
        print('车辆登记证上传成功！')
        self.driver.implicitly_wait(1)

        print("开始选择车系品牌")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/car_text")
        el.click()
        el = self.driver.find_element_by_name("AC Schnitzer")
        el.click()
        self.driver.implicitly_wait(1)
        el = self.driver.find_element_by_name("AC Schnitzer Eagle")
        el.click()
        print('车系品牌已选择')
        self.driver.implicitly_wait(1)

        print("开始选择车辆归属")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/vehicle_ownership_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()
        # # 往上滑动
        # self.driver.swipe(400, 1000, 400, 800)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print('车辆归属已选择')
        self.driver.implicitly_wait(1)

        print("开始选择购车时间")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/buying_time_text")
        el.click()
        el = self.driver.find_element_by_id("android:id/numberpicker_input")
        el.click()

        # # 往下翻动，选择年份（年份越来越小）
        # self.driver.swipe(140, 1000, 140, 1160)
        # self.driver.swipe(360, 1000, 360, 1160)
        # self.driver.swipe(560, 1000, 560, 1160)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print('购车时间已选择')
        self.driver.implicitly_wait(1)

        print("开始选择初次登记时间")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/initial_registration_time_text")
        el.click()
        el = self.driver.find_element_by_id("android:id/numberpicker_input")
        el.click()

        # # 往下翻动，选择年份（年份越来越小）
        # self.driver.swipe(140, 1000, 140, 1160)
        # self.driver.swipe(360, 1000, 360, 1160)
        # self.driver.swipe(560, 1000, 560, 1160)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print('初次登记时间已选择')
        self.driver.implicitly_wait(1)

        print("输入购买价格")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/purchase_price_edit")
        el.clear()
        el.click()
        el.send_keys(self.purchase_price)
        self.driver.hide_keyboard()
        print("购买价格输入完成")
        self.driver.implicitly_wait(1)

        print("输入一年内抵押次数")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/mortgage_number_edit")
        el.clear()
        el.click()
        el.send_keys(self.mortgage_number)
        self.driver.hide_keyboard()
        print("一年内抵押次数输入完成")
        self.driver.implicitly_wait(1)

        print("开始选择交强险保单合同")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/contract_of_insurance_text")
        el.click()
        print("开始点击交强险保单合同，进行上传。。。。。")
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id('com.rjs.ddjr:id/title_right_custom').click()
        print('交强险保单合同上传成功！')
        self.driver.implicitly_wait(1)

        print("开始选择商业险保单合同")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/commercial_insurance_contract_text")
        el.click()
        print("开始点击商业险保单合同，进行上传。。。。。")
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id('com.rjs.ddjr:id/title_right_custom').click()
        print('商业险保单合同上传成功！')
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_id("com.rjs.ddjr:id/next_step").click()
        # self.driver.implicitly_wait(1)
        print("——————————————————————————草稿录单模块，车辆信息页面已保存！——————————————————")

        # # 评审修改时间2017/5/4
        # # 加入检查点，并最终判断case执行的结果是通过还是不通过
        # self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.HomeActivity')
        # sleep(6)


        #
        # try:
        #     el = self.driver.find_element_by_id("com.rjs.ddjr:id/main_btn_message")
        #     el.click()
        #     el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft")
        #     el.click()
        #     sleep(1)
        #     el = self.driver.find_element_by_id("com.rjs.ddjr:id/cheyidai_tab")
        #     el.click()
        #     el = self.driver.find_element_by_id('com.rjs.ddjr:id/draft_item_name')
        #     print(el.text)
        #     if el.text == "suzhoutest":
        #         flag = 'P'
        #     if el.text != "suzhoutest":
        #         flag = 'F'
        #     print(flag)
        #
        #
        #     el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout")
        #     el.click()
        #     self.driver.find_element_by_id("com.rjs.ddjr:id/draft_vehicle")
        #     el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_vehicle_progress")
        #     print(el.text)
        #     if el.text == "完成:100％":
        #         flag = "P"
        #     if el.text != "完成:100％":
        #         flag = "F"
        #     print(flag)
        #
        #
        #     # 将结果写入到case和log日志中
        #     logstr = str(self.driver.get_log("logcat"))
        #     excle.excels(self.x, self.z, flag).write_excel(rsl, 10)
        #     Logs.logs(self.y, self.z, flag)._writ_file()
        #     Logs.logs(self.y, 'logcat', logstr)._writ_file()
        #
        #     excle.excels(self.x, self.z, pic).write_excel(2, 11)
        #     sleep(10)
        #
        #
        #
        #
        # except:
        #     info = str(sys.exc_info())
        #     Logs.logs(self.y, self.z, info)._writ_file()









