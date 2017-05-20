# -*- coding:utf-8 -*-


# 导入收入信息，联系人信息，车辆照片
from selenium.common.exceptions import NoSuchElementException
from Libraries import paths
from Libraries import excle
from Libraries import commons
from Libraries import Logs
from Scripts import xiangfa_Installment
from Scripts import xiangfa_Login
from Scripts import xiangfa_Draft_PersonalInfo
from Scripts import xiangfa_Draft_HouseInfo
from Scripts import xiangfa_Draft_DraftRecord
from Scripts import xiangfa_Draft_VehicleInfo
from Scripts import xiangfa_Draft_IncomeInfo
from Scripts import xiangfa_Draft_RelativiesInfo
from Scripts import xiangfa_Draft_CarPhoto
from Scripts import xiangfa_Draft_CompanyInfo
from Scripts import xiangfa_Draft_EnterpriseInfo
from Scripts import xiangfa_OfficialRecord
from appium import webdriver
from time import sleep


#定义文件路径和名称
timestap=commons._time_ini_()
casename='ddjr.xlsx'
resultname='ddjr'+timestap+'.xlsx'
logdirname='ddjr'+timestap
logname='ddjr'+timestap+'.txt'
appname='xiangfa-4.2.5-rls.apk'

casepath=  paths.path(casename)._version_path_ini_()
resultpath=  paths.path(resultname)._result_path_ini_()
logpath=  paths.path(logdirname)._log_path_ini_()
picpath=  paths.path(casename)._pic_path_ini_()
apppath= paths.path(appname)._version_path_ini_()
print(apppath)

if __name__=="__main__":
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '21'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['app'] = apppath
    desired_caps['newCommandTimeout'] = '600'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("开始启动APP，请耐心等待。。。")

    #commons._time_ini_()
    #paths.path('1.txt')._parent_path_ini_()
    #resolution.abst(1028,1960,50,50).abst_y()
    #excle.excels(casepath,timestap).read_excel()
    #excle.excels(resultname,timestap).create_excel()
    #备份自动化测试用例
    excle.excels(casepath,timestap,"").copy_excel()
    #excle.excels(resultname,timestap).write_excel()
    #Logs.logs(casepath,timestap)._creat_folder()
    #Logs.logs(casepath,timestap)._creat_file()
    #Logs.logs(casepath,timestap)._writ_file()

    #logstr=str(Case1.case())
    #创建执行临时日志目录
    Logs.logs(casepath,timestap,"")._creat_folder()
    # 创建执行临时日志文件
    Logs.logs(casepath,timestap,"")._creat_file()
    #Logs.logs(logpath,'logcat',logstr)._writ_file()
    #Logs.logs(logpath, timestap, 'pass')._writ_file()
    #xiangfa_Draft_PersonalInfo.PersonalInfo(13063835945,123456)
    #xiangfa_Draft_PersonalInfo.PersonalInfo(13063835945, 123456).InputPersonalInfo()
    #执行case
    #xiangfa_Login.APPLogin(casepath,logpath,picpath,apppath, timestap,driver).login()

    # xiangfa_Installment.Installment(casepath, logpath, picpath, apppath, timestap, driver)
    # driver.quit()




    # 修改了启动逻辑，首先进入草稿列表，然后分为两种情况进行录单：第一种是单子，直接进入单子中进行录单；另一种是没有单子，需要先进行创建单子再进行录单

    # ###################################### 存在单子记录，直接开始录房产信息##########################################

    xiangfa_Draft_DraftRecord.DraftRecord(casepath,logpath,picpath,apppath,timestap,driver).CheckDraftRecord()
    driver.find_element_by_id("com.rjs.ddjr:id/draft_layout")
    print("在草稿列表页中，成功找到已存在的草稿单子。。。。。")
    el = driver.find_element_by_id("com.rjs.ddjr:id/draft_item_name")
    el.click()
    print("已找到该单子的单子名称，点击名字进入草稿录单页面。。。。。")


    # 从草稿单子中进入房产信息页面
    driver.find_element_by_id("com.rjs.ddjr:id/draft_house").click()
    sleep(3)
    print("点击房产信息按钮，进入房产信息详情页中。。。。。")
    print("————————————————————————————开始对房产信息页面进行录单操作——————————————————————————")
    xiangfa_Draft_HouseInfo.HouseInfo(casepath, logpath, picpath, apppath, timestap, driver).InputHouseInfo()
    print("——————————————————————————————房产信息页面，录单完成！—————————————————————————————")


    #
    # ##############################################################################################################
    #
    #
    #
    #
    # print("———————————————————————————返回上一级，进入草稿录单列表页———————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿单子中进入车辆信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_vehicle").click()
    # sleep(3)
    # print("点击车辆信息按钮，进入车辆信息详情页中。。。。。")
    # xiangfa_Draft_VehicleInfo.VehicleInfo(casepath, logpath, picpath, apppath, timestap, driver).InputVehicleInfo()
    # print("—————————————————————————————车辆信息页面，录单完成！————————————————————————————")
    # sleep(3)

    # ##############################################################################################################
    #
    #
    #
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")

    # 从草稿录单页面中，点击联系人按钮，进入联系人信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_relatives").click()
    # sleep(3)
    # print("点击联系人信息按钮，进入联系人信息详情页中。。。。。")
    # xiangfa_Draft_RelativiesInfo.RelativiesInfo(casepath, logpath, picpath, apppath, timestap, driver).InputRelativiesInfo()
    # print("—————————————————————————————联系人信息页面，录单完成！————————————————————————————")
    # sleep(3)

    # ##############################################################################################################
    #
    #
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")

    # 从草稿录单页面中，点击车辆照片按钮，进入车辆照片信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_car_photo").click()
    # sleep(3)
    # print("点击车辆照片信息按钮，进入车辆照片信息详情页中。。。。。")
    # xiangfa_Draft_CarPhoto.CarPhoto(casepath, logpath, picpath, apppath, timestap, driver).InputCarPhotoInfo()
    # print("—————————————————————————————车辆照片信息页面，录单完成！————————————————————————————")
    # sleep(3)
    # # #
    #
    # ##############################################################################################################
    #


    # 当职业身份为第一种：企业股东时，才执行这段代码
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")

    # 从草稿录单页面中，点击企业信息按钮，进入企业信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_enterprise").click()
    # sleep(3)
    # print("点击企业信息按钮，进入企业信息详情页中。。。。。")
    # xiangfa_Draft_EnterpriseInfo.EnterpriseInfo(casepath, logpath, picpath, apppath, timestap, driver).InputEnterpriseInfo()
    # print("—————————————————————————————企业信息页面，录单完成！————————————————————————————")
    # sleep(3)

    #
    # ##############################################################################################################
    #
    #

    # # 当职业身份为第二种：受薪人士时，才执行这段代码
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿录单页面中，点击公司信息按钮，进入公司信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_company").click()
    # sleep(3)
    # print("点击公司信息按钮，进入公司信息详情页中。。。。。")
    # xiangfa_Draft_CompanyInfo.CompanyInfo(casepath, logpath, picpath, apppath, timestap, driver).InputCompanyInfo()
    # print("—————————————————————————————公司信息页面，录单完成！————————————————————————————")
    # sleep(3)


    ##############################################################################################################


    # #  当职业身份为第三种：自雇人士时，才执行这段代码
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿单子中进入收入信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_income").click()
    # sleep(3)
    # print("点击收入信息按钮，进入收入信息详情页中。。。。。")
    # xiangfa_Draft_IncomeInfo.IncomeInfo(casepath, logpath, picpath, apppath, timestap, driver).InputIncomeInfo()
    # print("—————————————————————————————收入信息页面，录单完成！————————————————————————————")
    # sleep(3)


    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout")
    # print("在草稿列表页中，成功找到已存在的草稿单子。。。。。")
    # el = driver.find_element_by_id("com.rjs.ddjr:id/draft_item_name")
    # el.click()
    # print("已找到该单子的单子名称，点击名字进入草稿录单页面。。。。。")
    #
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # xiangfa_OfficialRecord.OfficialRecord(casepath,logpath,picpath,apppath,timestap,driver).DraftOfficialRecord()



    ############################ 没有单子记录，重新创建一个单子##########################################
    ############################ 没有单子记录，重新创建一个单子##########################################
    ############################ 没有单子记录，重新创建一个单子##########################################
    ############################ 没有单子记录，重新创建一个单子##########################################
    ############################ 没有单子记录，重新创建一个单子##########################################
    ############################ 没有单子记录，重新创建一个单子##########################################




    # print("—————————————————————————————开始进入草稿录单列表页—————————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    #
    # print("——————————————————————找不到任何单子记录，则开始新建一个草稿单子———————————————————")
    # driver.find_element_by_id("com.rjs.ddjr:id/add_draft").click()
    # print("跳转到草稿录单详情页。。。。。")
    # sleep(3)
    #
    # # 从草稿单子中进入个人信息详情页
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_personal").click()
    # print("点击个人信息按钮，进入个人信息详情页中。。。。。")
    # sleep(3)
    # print("——————————————————————————————开始创建个人信息页面—————————————————————————————")
    # xiangfa_Draft_PersonalInfo.PersonalInfo(casepath, logpath, picpath, apppath, timestap, driver).InputPersonalInfo()
    # print("——————————————————————————————个人信息页面，录单完成！——————————————————————————")
    # sleep(3)
    # #

    #
    # #############################################################################################################
    #
    #

    #
    # print("——————————————————————————返回上一级，进入草稿录单列表页————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿单子中进入房产信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_house").click()
    # sleep(3)
    # print("点击房产信息按钮，进入房产信息详情页中。。。。。")
    # xiangfa_Draft_HouseInfo.HouseInfo(casepath, logpath, picpath, apppath, timestap, driver).InputHouseInfo()
    # print("————————————————————————————房产信息页面，录单完成！———————————————————————————")
    # sleep(3)

    #
    #
    #
    # #############################################################################################################
    #
    #
    #
    # print("———————————————————————————返回上一级，进入草稿录单列表页———————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿单子中进入车辆信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_vehicle").click()
    # sleep(3)
    # print("点击车辆信息按钮，进入车辆信息详情页中。。。。。")
    # xiangfa_Draft_VehicleInfo.VehicleInfo(casepath, logpath, picpath, apppath, timestap, driver).InputVehicleInfo()
    # print("—————————————————————————————车辆信息页面，录单完成！————————————————————————————")
    # sleep(3)



    ##############################################################################################################


    # # 当职业身份为第一种企业股东时，才执行这段代码
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿录单页面中，点击企业信息按钮，进入企业信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_enterprise").click()
    # sleep(3)
    # print("点击企业信息按钮，进入企业信息详情页中。。。。。")
    # xiangfa_Draft_EnterpriseInfo.EnterpriseInfo(casepath, logpath, picpath, apppath, timestap, driver).InputEnterpriseInfo()
    # print("—————————————————————————————企业信息页面，录单完成！————————————————————————————")
    # sleep(3)
    #
    #
    #
    # ##############################################################################################################
    #
    #
    # # 当职业身份为第二种：受薪人士时，才执行这段代码
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿录单页面中，点击公司信息按钮，进入公司信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_company").click()
    # sleep(3)
    # print("点击公司信息按钮，进入公司信息详情页中。。。。。")
    # xiangfa_Draft_CompanyInfo.CompanyInfo(casepath, logpath, picpath, apppath, timestap, driver).InputCompanyInfo()
    # print("—————————————————————————————公司信息页面，录单完成！————————————————————————————")
    # sleep(3)




    #############################################################################################################

    #
    #
    # # 当职业身份为第三种自雇人士时，才执行这段代码
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿单子中进入收入信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_income").click()
    # sleep(3)
    # print("点击收入信息按钮，进入收入信息详情页中。。。。。")
    # xiangfa_Draft_IncomeInfo.IncomeInfo(casepath, logpath, picpath, apppath, timestap, driver).InputIncomeInfo()
    # print("—————————————————————————————收入信息页面，录单完成！————————————————————————————")
    # sleep(3)



    #
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿单子中进入联系人信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_relatives").click()
    # sleep(3)
    # print("点击联系人信息按钮，进入联系人信息详情页中。。。。。")
    # xiangfa_Draft_RelativiesInfo.RelativiesInfo(casepath, logpath, picpath, apppath, timestap, driver).InputRelativiesInfo()
    # print("—————————————————————————————联系人信息页面，录单完成！————————————————————————————")
    # sleep(3)
    #
    # #
    # # #############################################################################################################
    # #
    # #
    # #
    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout").click()
    # print("即将跳转到草稿录单详情页。。。。。")
    #
    # # 从草稿录单页面中，点击车辆照片按钮，进入车辆照片信息页面
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_car_photo").click()
    # sleep(3)
    # print("点击车辆照片信息按钮，进入车辆照片信息详情页中。。。。。")
    # xiangfa_Draft_CarPhoto.CarPhoto(casepath, logpath, picpath, apppath, timestap, driver).InputCarPhotoInfo()
    # print("—————————————————————————————车辆照片信息页面，录单完成！————————————————————————————")
    # sleep(3)




    # print("——————————————————————————返回上一级，进入草稿录单列表页——————————————————————————")
    # xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()
    # driver.find_element_by_id("com.rjs.ddjr:id/draft_layout")
    # print("在草稿列表页中，成功找到已存在的草稿单子。。。。。")
    # el = driver.find_element_by_id("com.rjs.ddjr:id/draft_item_name")
    # el.click()
    # print("已找到该单子的单子名称，点击名字进入草稿录单页面。。。。。")

    xiangfa_OfficialRecord.OfficialRecord(casepath,logpath,picpath,apppath,timestap,driver).DraftOfficialRecord()




