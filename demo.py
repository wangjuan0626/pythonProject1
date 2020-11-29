#a=[1,2]
#b=[2,3]
#c=(5,6)
#d="abc"

#a.extend(b)
#a.extend(c)
#a.extend(d)
#print(a)

class cat(object):
    def info(self):
        print("It is a cat!")

class dog(object):
    def info(self):
        print("It is a dog!")

class duck(object):
    def info(self):
        print("It is a duck!")

animal_list=[cat,dog,duck]#变量
for animal in animal_list:
    animal().info()

"""
鸭子类型 在运行之前，cat，dog，都是在列表里面，当作变量
当运行时，加上()调用info（）才明确cat是一个类
"""
