class CacheBase(object):
    def dele(self):
        #pass
        raise NotImplementedError

    def crea(self):
        raise NotImplementedError

class RedisBase(CacheBase):
    """
    1、子类如果不重写  父类方法访问时直接抛出异常
    """

    def crea(self):
        print("create")

r=RedisBase()
r.crea()
#r.dele() #子类未重写  直接抛出异常


import abc
#注意：不是直接继承object 而是继承abc.ABCMeta
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dele(self):
        pass

    def crea(self):
        pass

class RedisBase(CacheBase):
    def crea(self):
        pass

r=RedisBase()
"""
抽象基类：实例化检测的时候
主动抛出异常：调用时才会检测
"""
