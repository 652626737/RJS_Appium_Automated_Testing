# -*- coding:utf-8 -*-

"""
个人信息页面

"""







from appium import webdriver
from time import sleep
from Libraries import excle
from Libraries import Logs
import sys
from selenium.common.exceptions import NoSuchElementException

from Scripts import xiangfa_Draft_DraftRecord
from Scripts.xiangfa_Login import XiangfaLogin
from Libraries import snapshots
from Libraries import commons


class PersonalInfo():
    '''登录后跳转到个人页面'''


    def __init__(self,casepath,logpath,picpath,apppath,timestap,driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver = driver
        print(self.n)

        # 这段代码多余
        # XiangfaLogin(self.x, self.y, self.m, self.n, self.z,self.driver).login()

        #路径需要使用相对路径，避免绝对路径
        print("——————————————————————————————打开个人信息页面,开始录单————————————————————————")
        self.driver.start_activity("com.rjs.ddjr", "com.rjs.ddjr.cheyidai.draft.view.PersonalInfoActivity")
        self.driver.implicitly_wait(1000)

        # case执行和代码开发过程中试用关键字驱动Auto_mlrc_Personinfo_002，同时获取用例data
        paramstr = str(excle.excels(self.x, 'Auto_mlrc_Personinfo_002', "").searche_parameter_excel())
        print(paramstr)

        # 如果存在参数，需要根据
        self.loan_money = commons._str_chuli_(paramstr, ',')[0]
        self.person_name = commons._str_chuli_(paramstr, ',')[1]
        self.person_age = commons._str_chuli_(paramstr, ',')[2]
        self.identification_number = commons._str_chuli_(paramstr, ',')[3]
        self.et_addr = commons._str_chuli_(paramstr, ',')[4]
        self.person_phone = commons._str_chuli_(paramstr, ',')[5]
        self.phone_number_service_password = commons._str_chuli_(paramstr, ',')[6]
        self.home_phone = commons._str_chuli_(paramstr, ',')[7]
        self.mail_address = commons._str_chuli_(paramstr, ',')[8]
        self.qq_number = commons._str_chuli_(paramstr, ',')[9]



    def InputPersonalInfo(self):
        rsl = excle.excels(self.x, 'Auto_mlrc_Personinfo_002', "").searche_pth_excel()

        # 截图存档并写入excle
        pic = str(snapshots.captrue(self.m, self.z)._capture_creen_ini_(self.driver))

        # 输入申请金额
        print('准备输入申请金额，请稍后。。。。。')
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/loan_money_edit')
        el.click()
        el.send_keys(self.loan_money)
        print('申请金额已输入')
        sleep(3)

        # 输入申请期数
        print('准备输入申请期数，请稍后。。。。。')
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/loan_period_text')
        el.click()
        self.driver.implicitly_wait(1000)
        # el = self.driver.find_element_by_id('com.rjs.ddjr:id/wheel')
        # el.click()

        # 往上翻动
        self.driver.swipe(400, 1000, 400, 800)
        self.driver.implicitly_wait(1000)

        el = self.driver.find_element_by_id('com.rjs.ddjr:id/done')
        el.click()
        print('申请期数已选择')
        sleep(3)

        # 选择职业身份
        print('准备选择职业身份，请稍后。。。。。')
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/professional_identity_text')
        el.click()
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/wheel')
        el.click()

        # 执行第二种职业身份时，启动这段代码
        self.driver.swipe(400, 1000, 400, 900)
        self.driver.implicitly_wait(1000)

        # # 执行第三种职业身份时，启动这段代码
        # self.driver.swipe(400, 1000, 400, 800)
        # self.driver.implicitly_wait(1000)

        el = self.driver.find_element_by_id('com.rjs.ddjr:id/done')
        el.click()
        print('职业身份已选择')
        sleep(3)

        # 选择借款用途
        print('准备选择借款用途，请稍后。。。。。')
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/loan_usage_text')
        el.click()
        el = self.driver.find_element_by_name('生意往来')
        el.click()
        print('借款用途已选择')
        sleep(3)

        # 选择是否投保履约险
        print('准备选择是否投保履约险，请稍后。。。。。')
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/loan_insurace_text')
        el.click()
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/wheel')
        el.click()
        # 往上滑动
        self.driver.swipe(350, 1000, 350, 820)
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/done')
        el.click()
        print('投保履约险已选择')

        # 上传身份证正面
        print('即将上传身份证正面照，请稍后。。。。。')
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/positive_id_card')
        el.click()
        sleep(8)
        try:
            self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
            sleep(2)
            self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
            sleep(10)
            print('身份证正面照上传成功！')
        except NoSuchElementException:
            pass
        finally:
            info = str(sys.exc_info())
            Logs.logs(self.y, self.z, info)._writ_file

        # 上传身份证反面
        print('即将上传身份证反面照，请稍后。。。。。')
        el = self.driver.find_element_by_id('com.rjs.ddjr:id/id_card_back')
        el.click()
        sleep(8)
        try:
            self.driver.find_element_by_id('com.rjs.ddjr:id/cbx').click()
            sleep(2)
            self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
            print('身份证反面正在上传，请稍后...')
            sleep(10)
            print('身份证反面照上传成功！')
            # else:
            #     self.driver.find_element_by_id('com.rjs.ddjr:id/action_done').click()
            #     print('上传失败，请重新上传')
            #     sleep(6)
        except NoSuchElementException:
            pass
        finally:
            info = str(sys.exc_info())
            Logs.logs(self.y, self.z, info)._writ_file

        # 往下滑动一次
        print("开始往下滑动一次。。。。。。")
        self.driver.swipe(100, 500, 100, 100)
        sleep(3)

        print("开始输入姓名。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/person_name")
        el.clear()
        el.click()
        self.driver.implicitly_wait(100)
        el.send_keys(self.person_name)
        self.driver.hide_keyboard()
        print("姓名输入成功")
        sleep(3)

        print("开始选择性别。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/person_sex_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()
        self.driver.swipe(350, 1000, 350, 820)
        self.driver.implicitly_wait(100)
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("性别选择成功")
        sleep(3)

        # 往下滑动一次
        print("开始往下滑动一次。。。。。")
        self.driver.swipe(100, 500, 100, 100)


        print("开始输入年龄。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/person_age")
        el.clear()
        el.click()
        el.send_keys(self.person_age)
        self.driver.hide_keyboard()
        print("年龄输入成功")
        sleep(3)



        print("开始选择出生日期。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/date_of_birth_text")
        el.click()
        self.driver.implicitly_wait(100)
        el = self.driver.find_element_by_id("android:id/numberpicker_input")
        el.click()

        # 往下翻动，选择年份（年份越来越小）
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)
        self.driver.swipe(140, 900, 140, 1160)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("日期选择成功")
        sleep(3)

        print("开始输入证件号码。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/identification_number")
        el.clear()
        el.click()
        el.send_keys(self.identification_number)
        self.driver.hide_keyboard()
        print("证件号码输入完成")
        sleep(3)

        # 往下滑动一次
        print("开始往下滑动一次。。。。。。")
        self.driver.swipe(100, 500, 100, 100)

        print("开始选择身份证有效截止日期。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/valid_date_text")
        el.click()
        self.driver.implicitly_wait(100)
        el = self.driver.find_element_by_id("android:id/numberpicker_input")
        el.click()

        # 往上翻动，选择年份（年份越来越大）
        self.driver.swipe(140, 1000, 140, 880)
        self.driver.swipe(140, 1000, 140, 880)
        self.driver.swipe(140, 1000, 140, 880)
        self.driver.swipe(140, 1000, 140, 880)
        self.driver.swipe(140, 1000, 140, 880)
        self.driver.swipe(140, 1000, 140, 880)
        self.driver.swipe(140, 1000, 140, 880)
        self.driver.swipe(140, 1000, 140, 880)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("身份证有效截止日期选择完成")
        sleep(3)

        print("开始输入户籍地址。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/permanent_address_text")
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
        print("户籍地址输入成功")
        sleep(3)

        # 往下滑动一次
        print("开始往下滑动一次。。。。。")
        self.driver.swipe(100, 500, 100, 100)

        print("开始选择婚姻状态。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/marital_status_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()

        # 往上翻动
        self.driver.swipe(400, 1000, 400, 800)
        self.driver.implicitly_wait(100)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()

        print("开始输入住宅地址。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/residential_address_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/cb_asCardAddr")
        el.click()
        print("住宅地址输入成功")
        sleep(3)

        # 往下滑动一次
        print("开始往下滑动一次。。。。。。")
        self.driver.swipe(100, 500, 100, 100)


        print("开始输入移动电话。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/person_phone")
        el.clear()
        el.click()
        el.send_keys(self.person_phone)
        self.driver.hide_keyboard()
        print("移动电话输入成功")
        sleep(3)

        self.driver.swipe(100, 500, 100, 100)

        # 新版本已经取消了这几个字段
        # print("开始输入服务密码。。。。。")
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/phone_number_service_password")
        # el.clear()
        # el.click()
        # el.send_keys(self.phone_number_service_password)
        # self.driver.hide_keyboard()
        # print("服务密码输入成功")
        # sleep(3)
        #
        # print("开始输入住宅电话。。。")
        # el = self.driver.find_element_by_id("com.rjs.ddjr:id/home_phone")
        # el.clear()
        # el.click()
        # el.send_keys(self.home_phone)
        # self.driver.hide_keyboard()
        # print("住宅电话输入成功")
        # sleep(3)

        # 往下滑动一次
        print("开始往下滑动一次。。。。。")
        self.driver.swipe(100, 500, 100, 100)

        print("开始输入邮箱地址。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/mail_address")
        el.clear()
        el.click()
        el.send_keys(self.mail_address)
        self.driver.hide_keyboard()
        print("邮箱地址输入成功")
        sleep(3)

        print("开始输入微信或者QQ。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/qq_number")
        el.clear()
        el.click()
        el.send_keys(self.qq_number)
        self.driver.hide_keyboard()
        print("微信或者QQ输入成功")
        sleep(3)

        print("开始选择学历。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/education_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()

        # 往下滑动
        self.driver.swipe(350, 1000, 350, 820)
        self.driver.swipe(350, 1000, 350, 820)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("学历已选择")
        sleep(3)

        # 往下滑动一次
        print("开始往下滑动一次。。。。。")
        self.driver.swipe(100, 500, 100, 100)

        print("开始选择来本地时间。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/local_time_text")
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
        print("来本地时间已选择")
        sleep(3)

        print("开始输入起始居住时间。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/initial_residence_time_text")
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
        print("起始居住时间已选择")
        sleep(3)

        print("开始选择居住类别。。。。。")
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/residential_category_text")
        el.click()
        el = self.driver.find_element_by_id("com.rjs.ddjr:id/wheel")
        el.click()

        # 往下滑动
        self.driver.swipe(350, 1000, 350, 820)
        self.driver.swipe(350, 1000, 350, 820)

        el = self.driver.find_element_by_id("com.rjs.ddjr:id/done")
        el.click()
        print("居住类别请选择")

        print("即将保存个人信息页面。。。。。")
        sleep(2)
        self.driver.find_element_by_id('com.rjs.ddjr:id/draft_save').click()
        print("草稿录单模块，个人信息页面保存成功！")




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
            self.driver.find_element_by_id("com.rjs.ddjr:id/draft_personal")
            el = self.driver.find_element_by_id("com.rjs.ddjr:id/draft_personal_progress")
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















