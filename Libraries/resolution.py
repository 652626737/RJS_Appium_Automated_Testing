# -*- coding:utf-8 -*-

# 分辨率基准系数
a = 768
b = 1280
class abst():


# 有点类似其它高级语言的构造函数
#w为手机宽h为手机长xpt，ypt为选取点坐标
    def __init__(self,w,h,xpt,ypt):
        self.x = xpt
        self.y = ypt
        self.w = w
        self.h = h

#相对x坐标
    def abst_x(self):
        self.w =self.w /a
        self.x=self.x * self.w
        return self.x
#相对y坐标
    def abst_y(self):
        self.h =self.h /b
        self.y=self.y*self.h
        return self.y



