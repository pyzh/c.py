import functools as fn
import collections as co
from .常量 import *
from .类型 import *

打印=print
#打印.__repr__ = lambda x: 打印<-print

列=range

#数列=列
def 数列(起=1, 止, 步进=1):
    偏移量=止+1
    return 列(起, 偏移量, 步进)

def 如果(条件, 为真, 为否):
    return 为真 if 条件 else 为否

def 循环(条件, 主体:无参函数, 附加:单目函数=略):
    结果=略
    while 条件:
        结果=主体()
    else:
        if 附加 != 略: 
            附加()
            #附加(结果)
    return 结果

def 遍历(对象集, 主体:单目函数, 附加:单目函数=略):
    结果 = []
    for i in 对象集:
       列表.附加(结果, 单目函数(i))
    else:
        单目函数(结果)

    return 结果

loop=循环

参 = fn.partial

若 = 参(如果, 为否=略)

有序字典 = co.OrderedDict