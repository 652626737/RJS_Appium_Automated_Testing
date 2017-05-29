# -*- coding:utf-8 -*-



from selenium.common.exceptions import NoSuchElementException

from Libraries import paths
from Libraries import excle
from Libraries import commons
from Libraries import Logs
from appium import webdriver
from Scripts import xiangfa_Installment
from Scripts import xiangfa_Draft_BillPushingProcess
from Scripts import xiangfa_OfficialRecord
from Scripts import xiangfa_Draft_DraftRecord
from Libraries import resolution
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
    driver.implicitly_wait(30)
    print("开始启动APP，请耐心等待。。。")

    #commons._time_ini_()
    #paths.path('1.txt')._parent_path_ini_()
    resolution.abst(1028,1960,50,50,driver).abst_y()
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
    xiangfa_Draft_DraftRecord.DraftRecord(casepath, logpath, picpath, apppath, timestap, driver).CheckDraftRecord()

    # 开始录单操作
    xiangfa_Draft_BillPushingProcess.BillProcess(casepath, logpath, picpath, apppath, timestap, driver).PushingProcess()
    # 开始推单操作
    xiangfa_OfficialRecord.OfficialRecord(casepath, logpath, picpath, apppath, timestap, driver).DraftOfficialRecord()










