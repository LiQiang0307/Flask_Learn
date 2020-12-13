"""
谈谈你对面向对象的理解：
# -按照属性和功能进行划分
-封装：
    -将同一类方法分为一类:方法封装到类中
    -将方法中共同的参数封装到对象中：把共用的值封装到对象中。

    情况：
        a.
            def index(a1,a2,a3,a4,a5,a6):
                pass
            #用类实现
            class Foo(object):
                    def __init__(self,a1,a2,a3,a4,a5,a6):
                        self.a1=a1
                        self.a2=a2
                        self.a3=a3
                        self.a4=a4
                        self.a5=a5,
                        self.a6=a6
            #这样index只需接收一个对象就可以，避免那么多参数
            def index(obj):
                pass
        b. 给了一些值，将数据加工 :django 自定义分页
            class Foo(object):
                    def __init__(self,a1,a2,a3,a4,a5,a6):
                        self.a1=a1
                        self.a2=a2
                        self.a3=a3
                        self.a4=a4
                        self.a5=a5,
                        self.a6=a6
                    def 金条（self）：
                        return self.a1+self.a2
                    def 手表（self）：
                        return self.a1+self.a7
"""

class A(object):
    def __init__(self):
        self.age1=123
class B(object):
    def __init__(self):
        self.age1=123
        self.a=A()
class C(object):
    def __init__(self):
        self.age1=123
        self.b=B()
class D(object):
    def __init__(self):
        self.age1=123
        self.c=C()






class Foo(object):
    pass


class File:
    """
    把a1，a2，a3，a4都封装到对象self 中
    """
    def __init__(self,a1,a2,a3,a4):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.a4=a4

    def file_add(self):
        pass

    def file_del(self):
        pass

    def file_update(self):
        pass

    def file_fetch(self):
        pass