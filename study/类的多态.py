"""
Python中的多态与Java、C++不同，Python中的多态只需要满足有该方法，然后让不同的对象去调用即可
而 Java 中的多态需要满足三个条件：向上转型（父类引用指向子类对象）、子类重写父类的方法、向上转型的父类调用该方法（被重写的方法）
这时就不再是调用父类的方法，而是调用子类的方法
但 Python中，只要这两个类有相同的方法，当两者赋值给同一个对象时，去调用同一个方法就会表现出不同的行为。

其实，多态就是表层对象一样，内部实际的对象不一样，那么在调用同一个方法时，虽然看似是这个表层的对象所调用的，但实际是内部的对象所调用并执行的。
"""


class Animal():
    def eat(self):
        print('正在吃东西')


class Person():
    def eat(self):
        print('正在干饭')


class Dog():
    def eat(self):
        print('正在吃狗粮')


class Cat():
    def eat(self):
        print('正在吃猫粮')


# 定义一个函数，传入obj对象，并调用该对象的eat方法
def eat(obj):
    obj.eat()


# 方法得通过类或者对象去"."调用，而函数是直接传参调用，不要弄混了
eat(Animal())  # 这里需要传入对象，即:类名()
eat(Person())
eat(Dog())
eat(Cat())
