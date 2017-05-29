#! usr/bin/python
#coding=utf-8
#2017/5/4-AUTHOR-JOE
import xlrd
import xlwt
from xlutils.copy import copy
import os
import shutil

class excels():
    def __init__(self, xdpth, name, flag):
        self.x = xdpth
        self.y = name
        self.z = flag

    def read_excel(self):
        # 打开文件
        if os.path.exists(self.x )==True:
         data = xlrd.open_workbook(self.x )
        #读取excle
         table = data.sheet_by_name('Sheet2')
         cell_A1 = str(table.cell(1, 1).value)
         cell_C4 = table.cell(1, 2).value
         print(cell_A1)
         print(cell_C4)
        else:
            print('Not found excel!')
            return False

    def create_excel(self):
        # 创建exlce
        if os.path.exists(self.x )!=True:
            filename = xlwt.Workbook()
            sheet = filename.add_sheet("my_sheet")
            filename.save(self.x )
        else:
            print('exist same excel!')
            return False

    def copy_excel(self):
        # 复制exlce
        destPath=os.getcwd()+'\\Result\\'+'ddjr'+self.y+'.xlsx'
        #print(1111)
        if os.path.exists(self.x )==True:
            shutil.copy(self.x ,destPath )
        else:
            print('not found excel!')
            return False

    def write_excel(self,i,j):
        # 复制exlce
        destPath=os.getcwd()+'\\Result\\'+'ddjr'+self.y+'.xlsx'
        if os.path.exists(destPath )==True:
           data = xlrd.open_workbook(destPath)
           # 读取excle
           wb = copy(data)
           sheet1 = wb.get_sheet(1)
           sheet1.write(i, j, self.z)
           wb.save(destPath)

        else:
            print('not found excel!')
            return False

    def searche_parameter_excel(self):
        # 打开文件
        if os.path.exists(self.x )==True:
         data = xlrd.open_workbook(self.x )
        #读取excle
         table = data.sheet_by_name('Sheet1')
         nrows = table.nrows
      #   ncols = table.ncols
    #查找关键字所在位置
         for i in range(nrows):
             cell_value = table.cell_value(i, 1)
             if self.y in str(cell_value):
                 outputs = str(table.cell(i, 6).value)
                 return outputs
        else:
            print('Not found excel!')
            return False

    def searche_pth_excel(self):
            # 打开文件
            if os.path.exists(self.x) == True:
                data = xlrd.open_workbook(self.x)
                # 读取excle
                table = data.sheet_by_name('Sheet1')
                nrows = table.nrows
                #   ncols = table.ncols
                # 查找关键字所在位置
                for i in range(nrows):
                    cell_value = table.cell_value(i, 1)
                    if self.y in str(cell_value):
                        outputs = i
                        return outputs
            else:
                print('Not found excel!')
                return False

