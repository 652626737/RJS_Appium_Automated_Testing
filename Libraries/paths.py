# -*- coding:utf-8 -*-

import os


class path():
    def __init__(self, xdpth):
        self.x = xdpth
  #case路径
    def _version_path_ini_(self):
        self.x=os.getcwd()+'\\Version\\'+self.x
        return self.x

#result路径
    def _result_path_ini_(self):
        self.x = os.getcwd()+'\\Result\\'+self.x
        return  self.x

#log路径
    def _log_path_ini_(self):
        self.x = os.getcwd()+'\\Logs\\'+self.x
        return  self.x

        # log路径
    def _pic_path_ini_(self):
        self.x = os.getcwd() + '\\Snapshots\\'
        return self.x
#父级别路径
    def _parent_path_ini_(self):
        self.x = os.path.dirname(os.getcwd()) + '\\' + self.x
        return self.x

