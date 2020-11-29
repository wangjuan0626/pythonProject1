"""
抽象基类（定义各种方法而不是做具体实现的类）的应用场景
1、检查某个类中是否含有某种方法
2、需要强调某个子类必须实现某些方法
"""
#abc模块 abc.py  不要以abc为模板名称
class Demo(object):
    def __init__(self,li):
        self.li=li

    def __len__(self):
        return len(self.li)

l=["C","凌云","111"]
d=Demo(l)
print(d)            #返回demo类的地址
print(len(d))       #会触发__len__(self.li)的魔法方法   所以返回3

#如何判断demo中含有__len__魔法方法
print(hasattr(d,"__len__"))  #判断d的内部是否含有__len__  返回值为bool类型

#导入抽象基类中的sized类
from collections.abc import Sized
#判断d是否是sized这个类
print(isinstance(d,Sized))    #true说明d是sized类型

"""
可以通过判断d是否是sized的子类
然后进一步判断d这个对象类是否含有__len__方法
"""