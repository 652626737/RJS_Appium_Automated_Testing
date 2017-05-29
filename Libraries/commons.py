#! usr/bin/python
#coding=utf-8
#2017/5/4-AUTHOR-JOE
import time

#字符串处理
def _str_chuli_(str,sign):
    # 或者
    s = str
    _str_chuli_=s.split(',')
    return _str_chuli_


#时间戳

def _time_ini_():
    return time.strftime('%Y%m%d_%H%I%S',time.localtime(time.time()))



