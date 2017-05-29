#! usr/bin/python
#coding=utf-8
#2017/5/4-AUTHOR-JOE
# 分辨率基准系数

class abst():


# 有点类似其它高级语言的构造函数
#w为手机宽h为手机长xpt，ypt为选取点坐标
    def __init__(self,w,h,xpt,ypt,driver):
        self.x = xpt
        self.y = ypt
        self.w = w
        self.h = h
        self.driver=driver

#相对x坐标
    def abst_x(self):
        a = self.driver.get_window_size()["width"]

        self.driver.get_window_size()
        self.w =self.w /a
        self.x=self.x * self.w
        return self.x
#相对y坐标
    def abst_y(self):
        b = self.driver.get_window_size()["height"]
        self.h =self.h /b
        self.y=self.y*self.h
        return self.y



