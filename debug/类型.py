# 区分函数的操作目数，是从erlang习来的习惯
from .常量 import *

静态方法 = staticmethod

class 单目函数:
    # def __init__(此, 描述):
    #   此.__repr__ = 描述
    
    def __call__(此,参数): 略

class 无参函数:
    def __call__(此): 略

数=略
串=str
列=list
典=dict

列.附 = 列.append

class 可遍历: 略

class 列表(可遍历): 略