# -*- coding:utf-8 -*-

"""
录单流程说明

"""




from Scripts import xiangfa_Draft_HouseInfo, xiangfa_Draft_EnterpriseInfo, xiangfa_Draft_CompanyInfo, \
    xiangfa_OfficialRecord
from Scripts import xiangfa_Draft_PersonalInfo
from Scripts import xiangfa_Draft_DraftRecord
from Scripts import xiangfa_Draft_VehicleInfo
from Scripts import xiangfa_Draft_IncomeInfo
from Scripts import xiangfa_Draft_RelativiesInfo
from Scripts import xiangfa_Draft_CarPhoto
from time import sleep
from appium import webdriver


class BillProcess():

    """录单流程说明"""

    def __init__(self, casepath, logpath, picpath, apppath, timestap, driver):
        self.x = casepath
        self.y = logpath
        self.z = timestap
        self.m = picpath
        self.n = apppath
        self.driver = driver
        print(self.n)




    def PushingProcess(self):
        '''存在单子则直接进入，否则首先新建一个单子'''

        # # 从草稿单子中进入个人信息详情页
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_personal").click()
        # print("点击个人信息按钮，进入个人信息详情页中。。。。。")
        # self.driver.implicitly_wait(6)
        # xiangfa_Draft_PersonalInfo.PersonalInfo(self.x, self.y, self.z, self.m, self.n, self.driver).InputPersonalInfo()
        # print("——————————————————————————————个人信息页面，录单完成！——————————————————————————")
        # self.driver.implicitly_wait(6)
        #
        #
        # # 从草稿单子中进入房产信息页面
        # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
        # xiangfa_Draft_DraftRecord.DraftRecord(self.x, self.y, self.z, self.m, self.n, self.driver).CheckDraftRecord()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
        # print("即将跳转到草稿录单详情页。。。。。")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_house").click()
        # self.driver.implicitly_wait(6)
        # print("点击房产信息按钮，进入房产信息详情页中。。。。。")
        # xiangfa_Draft_HouseInfo.HouseInfo(self.x, self.y, self.z, self.m, self.n, self.driver).InputHouseInfo()
        # print("————————————————————————————房产信息页面，录单完成！———————————————————————————")
        # self.driver.implicitly_wait(6)


        # 从草稿单子中进入车辆信息页面
        # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
        # xiangfa_Draft_DraftRecord.DraftRecord(self.x, self.y, self.z, self.m, self.n, self.driver).CheckDraftRecord()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
        # print("即将跳转到草稿录单详情页。。。。。")
        self.driver.find_element_by_id("com.rjs.ddjr:id/draft_vehicle").click()
        self.driver.implicitly_wait(6)
        print("点击车辆信息按钮，进入车辆信息详情页中。。。。。")
        xiangfa_Draft_VehicleInfo.VehicleInfo(self.x, self.y, self.z, self.m, self.n, self.driver).InputVehicleInfo()
        print("—————————————————————————————车辆信息页面，录单完成！————————————————————————————")
        self.driver.implicitly_wait(6)


        # # 当职业身份为第一种企业股东时，进入企业信息页面
        # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
        # xiangfa_Draft_DraftRecord.DraftRecord(self.x, self.y, self.z, self.m, self.n, self.driver).CheckDraftRecord()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
        # print("即将跳转到草稿录单详情页。。。。。")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_enterprise").click()
        # sleep(3)
        # print("点击企业信息按钮，进入企业信息详情页中。。。。。")
        # xiangfa_Draft_EnterpriseInfo.EnterpriseInfo(self.x, self.y, self.z, self.m, self.n, self.driver).InputEnterpriseInfo()
        # print("—————————————————————————————企业信息页面，录单完成！————————————————————————————")
        # sleep(3)
        #
        #
        # # 当职业身份为第二种：受薪人士时，进入公司信息页面
        # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
        # xiangfa_Draft_DraftRecord.DraftRecord(self.x, self.y, self.z, self.m, self.n, self.driver).CheckDraftRecord()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
        # print("即将跳转到草稿录单详情页。。。。。")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_company").click()
        # sleep(3)
        # print("点击公司信息按钮，进入公司信息详情页中。。。。。")
        # xiangfa_Draft_CompanyInfo.CompanyInfo(self.x, self.y, self.z, self.m, self.n, self.driver).InputCompanyInfo()
        # print("—————————————————————————————公司信息页面，录单完成！————————————————————————————")
        # sleep(3)


        # 当职业身份为第三种自雇人士时，进入收入信息页面
        # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
        # xiangfa_Draft_DraftRecord.DraftRecord(self.x, self.y, self.z, self.m, self.n, self.driver).CheckDraftRecord()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
        # print("即将跳转到草稿录单详情页。。。。。")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_income").click()
        # self.driver.implicitly_wait(6)
        # print("点击收入信息按钮，进入收入信息详情页中。。。。。")
        # xiangfa_Draft_IncomeInfo.IncomeInfo(self.x, self.y, self.z, self.m, self.n, self.driver).InputIncomeInfo()
        # print("—————————————————————————————收入信息页面，录单完成！————————————————————————————")
        # self.driver.implicitly_wait(6)
        #

        # 从草稿单子中进入联系人信息页面
        # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
        # xiangfa_Draft_DraftRecord.DraftRecord(self.x, self.y, self.z, self.m, self.n, self.driver).CheckDraftRecord()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
        # print("即将跳转到草稿录单详情页。。。。。")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_relatives").click()
        # self.driver.implicitly_wait(6)
        # print("点击联系人信息按钮，进入联系人信息详情页中。。。。。")
        # xiangfa_Draft_RelativiesInfo.RelativiesInfo(self.x, self.y, self.z, self.m, self.n, self.driver).InputRelativiesInfo()
        # print("—————————————————————————————联系人信息页面，录单完成！————————————————————————————")
        # self.driver.implicitly_wait(6)

        # 从草稿录单页面中，点击车辆照片按钮，进入车辆照片信息页面
        # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
        # xiangfa_Draft_DraftRecord.DraftRecord(self.x, self.y, self.z, self.m, self.n, self.driver).CheckDraftRecord()
        # sleep(3)
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
        # print("即将跳转到草稿录单详情页。。。。。")
        # self.driver.find_element_by_id("com.rjs.ddjr:id/draft_car_photo").click()
        # self.driver.implicitly_wait(6)
        # print("点击车辆照片信息按钮，进入车辆照片信息详情页中。。。。。")
        # xiangfa_Draft_CarPhoto.CarPhoto(self.x, self.y, self.z, self.m, self.n, self.driver).InputCarPhotoInfo()
        # print("—————————————————————————————车辆照片信息页面，录单完成！————————————————————————————")
        # self.driver.implicitly_wait(6)


        # 开始正式录单
        print("开始正式录单。。。。。")
        xiangfa_OfficialRecord.OfficialRecord(self.x, self.y, self.z, self.m, self.n, self.driver).DraftOfficialRecord()