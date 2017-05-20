# -*- coding:utf-8 -*-


"""
企业信息页面

"""



from appium import webdriver
from time import sleep
from Libraries import excle
from Libraries import Logs
from Libraries import commons
from Libraries import snapshots
import sys


class EnterpriseInfo():
    '''登录后跳转到企业信息页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)



        # case执行和代码开发过程中试用关键字驱动 Auto_mlrc_EnterpriseInfo_008，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_EnterpriseInfo_008', "").searche_parameter_excel())
        print(paramstr)


        # 如果存在参数，需要根据参数传值
        self.enterprise_name = commons._str_chuli_(paramstr, ',')[0]
        self.et_addr = commons._str_chuli_(paramstr, ',')[1]
        self.monthly_turnover = commons._str_chuli_(paramstr, ',')[2]
        self.enterprise_phone = commons._str_chuli_(paramstr, ',')[3]



    def InputEnterpriseInfo(self):
        print('—————————————————————————————企业信息页面载入中，请稍后————————————————————————————')
        rsl = excle.excels(self.x, 'Auto_mlrc_EnterpriseInfo_008', "").searche_pth_excel()

        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))

        print("开始输入单位名称。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/enterprise_name_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_info")
        el.click()
        el.send_keys(self.enterprise_name)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("单位名称输入完成")


        print("开始输入单位地址。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/enterprise_address_text")
        el.click()
        sleep(1)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/item_content")
        el.click()
        sleep(1)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/textView")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/textView")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/textView")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_addr")
        el.click()
        el.send_keys(self.et_addr)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("单位地址输入成功")
        sleep(3)



        print("开始选择注册日期。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/registration_date_text")
        el.click()
        el = self.driver.find_element_by_id("android:id/numberpicker_input")
        el.click()

        # 分别在年月日上进行滑动选择
        self.driver.swipe(150, 980, 150, 1150)
        self.driver.swipe(150, 980, 150, 1150)
        self.driver.swipe(350, 980, 350, 1150)
        self.driver.swipe(350, 980, 350, 1150)
        self.driver.swipe(560, 980, 560, 1150)
        self.driver.swipe(560, 980, 560, 1150)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("注册日期已选择")
        sleep(3)



        print("请输入月营业额。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/monthly_turnover_edit")
        el.clear()
        el.click()
        el.send_keys(self.monthly_turnover)
        self.driver.hide_keyboard()
        print("月营业额已输入")
        sleep(3)



        print("请输入单位电话。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/enterprise_phone_edit")
        el.clear()
        el.click()
        el.send_keys(self.enterprise_phone)
        self.driver.hide_keyboard()
        print("单位电话已输入")
        sleep(3)


        print("开始选择企业资料类型。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/enterprise_information_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/rb_2")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/tv_confirm")
        el.click()

        # 开始上传企业照片
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        sleep(6)
        self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom").click()
        sleep(3)
        print("企业资料已上传")


        # 新增了央行征信报告字段
        print("开始上传央行征信报告。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/credit_report_text")
        el.click()

        # 开始上传央行征信报告照片
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        sleep(6)
        self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom").click()
        sleep(3)
        print("央行征信报告已上传")


        self.driver.find_element_by_id("com.rjs.ddjr:id/draft_save").click()
        sleep(1)
        print("——————————————————————————草稿录单模块，企业信息页面已保存！——————————————————")



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
            self.driver.find_element_by_id("com.rjs.ddjr:id/draft_enterprise")
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_enterprise_progress")
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

