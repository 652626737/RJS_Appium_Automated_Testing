#! usr/bin/python
#coding=utf-8
#2017/5/4-AUTHOR-JOE
import os
import time
class logs():

    def __init__(self,xpath, name, message):
        self.x= xpath
        self.y = name
        self.z = message
    def _creat_folder(self):
         #创建目录

        if os.path.exists(self.x )==True:
            destPath = os.getcwd() + '\\Logs\\' + 'ddjr' +  self.y
            os.mkdir(destPath)
        else:
            print('not found excel!')
            return False

    def _creat_file(self):
         #创建txt
        destPath = os.getcwd() + '\\Logs\\' + 'ddjr' + self.y
        if os.path.exists(destPath)==True:
            full_path = destPath +'\\'+ self.y + '.txt'
            file = open(full_path, 'w')
            file.write("Logcat start!======\n")
            file.close()
            full_path = destPath +'\\logcat.txt'
            file = open(full_path, 'w')
            file.write("Logcat start!======\n")
            file.close()
        else:
            print('not found folder!')
            return False

    def _writ_file(self):
         #写txt
        destPath = self.x+'\\'+self.y+'.txt'
        if os.path.exists(destPath)==True:
		#解决存储编码问题
            file = open(destPath, 'a',encoding="utf-8")
            times=time.strftime('%Y-%m-%d_%H:%I:%S', time.localtime(time.time()))
            flag=str(times+" This Case Excute Result:"+self.z)
            file.writelines("=================================================\n")
            file.writelines(flag)
            file.writelines("\n")
            file.writelines("=================================================\n")
            file.close()
        else:
            print('not found file!')
            return False



