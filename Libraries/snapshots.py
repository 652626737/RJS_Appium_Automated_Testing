# -*- coding:utf-8 -*-

import os
from appium import webdriver

class captrue():
    def __init__(self, xdpth, name):
        self.x = xdpth
        self.y = name
  #截屏存储
    def _capture_creen_ini_(self,driver):
        # 以下为启动driver，以及定位元素和操作元素的一些用例操作

        destPath =self.x+self.y+'.jpg'
        # 创建exlce
        if os.path.exists(destPath)!=True:
            driver.get_screenshot_as_file(destPath)
            return destPath
        else:
            print('exist same picture!')
            return False
        driver.quit()
