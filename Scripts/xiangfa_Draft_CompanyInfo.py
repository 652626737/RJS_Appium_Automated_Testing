# -*- coding:utf-8 -*-


"""
公司信息页面

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

class CompanyInfo():
    '''登录后跳转到公司信息页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver=driver
        print(self.n)



        # case执行和代码开发过程中试用关键字驱动 Auto_mlrc_CompanyInfo_009，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_CompanyInfo_009', "").searche_parameter_excel())
        print(paramstr)


        # 如果存在参数，需要根据参数传值
        self.company_name = commons._str_chuli_(paramstr, ',')[0]
        self.et_addr = commons._str_chuli_(paramstr, ',')[1]
        self.company_mobile = commons._str_chuli_(paramstr, ',')[2]
        self.department = commons._str_chuli_(paramstr, ',')[3]
        self.monthly_income = commons._str_chuli_(paramstr, ',')[4]



    def InputCompanyInfo(self):
        print('—————————————————————————————公司信息页面载入中，请稍后————————————————————————————')
        rsl = excle.excels(self.x, 'Auto_mlrc_CompanyInfo_009', "").searche_pth_excel()

        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))


        print("请输入单位名称。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/company_name_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_info")
        el.clear()
        el.click()
        el.send_keys(self.company_name)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("单位名称已输入")
        self.driver.implicitly_wait(1)

        print("开始输入单位地址。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/company_address_text")
        el.click()
        self.driver.implicitly_wait(1)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/item_content")
        el.click()
        self.driver.implicitly_wait(1)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/textView")
        el.click()
        self.driver.implicitly_wait(2)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/textView")
        el.click()
        self.driver.implicitly_wait(2)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/textView")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_addr")
        el.click()
        el.send_keys(self.et_addr)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        print("单位地址输入成功")
        self.driver.implicitly_wait(1)


        print("开始输入单位电话。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/company_mobile_edit")
        el.clear()
        el.click()
        el.send_keys(self.company_mobile)
        self.driver.hide_keyboard()
        print("单位电话已输入")
        self.driver.implicitly_wait(1)

        print("开始选择职位。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/position_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()

        # 往上翻动
        self.driver.swipe(400, 1000, 400, 800)
        self.driver.implicitly_wait(1000)

        el = self.driver.find_element_by_id('com.rjs.ddjr:id/done')
        el.click()
        print('职位已选择')
        self.driver.implicitly_wait(1)


        print("开始输入部门。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/department_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/et_info")
        el.clear()
        el.click()
        el.send_keys(self.department)
        self.driver.hide_keyboard()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom")
        el.click()
        self.driver.implicitly_wait(1)
        print("部门已经输入")


        print("开始选择起始服务时间")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/service_time_text")
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
        print("起始服务时间已选择")
        self.driver.implicitly_wait(1)


        print("开始输入每月收入。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/monthly_income_edit")
        el.clear()
        el.click()
        el.send_keys(self.monthly_income)
        self.driver.hide_keyboard()
        print("每月收入已输入")
        self.driver.implicitly_wait(1)

        # 往上翻动
        self.driver.swipe(400, 1100, 400, 800)
        self.driver.implicitly_wait(1000)


        print("开始选择每月发薪日。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/monthly_pay_day_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")

        # 往上翻动
        self.driver.swipe(400, 1000, 400, 800)
        self.driver.implicitly_wait(1000)
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/done')
        el.click()
        print('每月发薪日已选择')
        self.driver.implicitly_wait(3)


        print("开始选择支付方式。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/payment_method_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()

        # 往上翻动
        self.driver.swipe(400, 1000, 400, 800)
        self.driver.implicitly_wait(1000)
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/done')
        el.click()
        print('支付方式已选择')
        self.driver.implicitly_wait(3)


        # 往上翻动
        self.driver.swipe(400, 1100, 400, 800)
        self.driver.implicitly_wait(1000)



        print("开始选择工作证明类型。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/work_certificate_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/rb_1")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/tv_confirm")
        el.click()

        # 开始上传工作证明照片
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom").click()
        self.driver.implicitly_wait(2)
        print("工作证明已上传")



        print("开始上传央行征信照片。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/credit_report_text")
        el.click()

        # 开始上传央行征信照片
        self.driver.find_element_by_id("com.rjs.ddjr:id/iv_pic").click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
        self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
        self.driver.implicitly_wait(6)
        self.driver.find_element_by_id("com.rjs.ddjr:id/title_right_custom").click()
        self.driver.implicitly_wait(2)
        print("央行征信照片已上传")


        self.driver.find_element_by_id("com.rjs.ddjr:id/draft_save").click()
        self.driver.implicitly_wait(1)
        print("——————————————————————————草稿录单模块，公司信息页面已保存！——————————————————")

        # 评审修改时间2017/5/4
        # 加入检查点，并最终判断case执行的结果是通过还是不通过
        self.driver.start_activity('com.rjs.ddjr', 'com.rjs.ddjr.publicmodel.view.HomeActivity')



        try:
     #       sleep(1)
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/main_btn_message")
            el.click()
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft")
            el.click()
         #   sleep(1)
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
            self.driver.find_element_by_id("com.rjs.ddjr:id/draft_company")
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_company_progress")
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
          #  sleep(10)



        except:
            info = str(sys.exc_info())
            Logs.logs(self.y, self.z, info)._writ_file()

