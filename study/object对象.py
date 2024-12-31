"""
前面我们学习类和对象以及面向对象的三大特征。
类和对象还是很好理解的，在Python中一切皆是对象，而类是创建对象的模版，创建对象的过程，也被称为"类的实例化"，因为类从一个飘无虚渺的概念，变为了一个实实在在的、看得见摸得着（可以去访问方法与属性）的对象，因此就叫实例化。
紧接着我们又学习了面向对象编程的三大特征，封装、继承、多态。
封装主要是体现在类的属性与方法带有访问权限了，并且外部在调用该方法时，不需要知道底层是如何实现的，相当于隐藏了内部的细节。
继承是对共性的一个抽取（猫和狗，抽象成动物）主要是实现了代码的复用（动物类有了姓名、年龄这些属性之后，子类可以直接用，而不用再去定义）。
继承之中有一个知识点是方法重写，即子类定义了一个与父类同名的方法，就称子类的方法为重写的方法。
多态是描述不同的对象在面对同一件事情时，所表现出的行为不同，而Python中的多态要和其他语言区分开来，这里的多态只要两个类的对象都有同一个方法，
那么当把这些对象封装一下（使用 obj = A/B），然后再去调用这个方法，就会表现出不同的行为。
这其实也很好理解，虽然表面上看起来是同一个对象在调用同一个方法，但其底层根本就是不同的对象，自然调用同一个方法时，所表现出行为就不同了。
"""


# object类是所有类的直接父类或者间接父类，那么这些类肯定都是会拥有object类中所有共有与受保护的属性、方法
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我的名字是{self.name},今年{self.age}岁')


# 类名() --> 这就是在实例化一个对象，并且会自动调用init方法，构造对象
person = Person('小明', '18')
print(dir(person))


# __init__ 是构造方法，当实例化一个对象时，会自动调用该方法，创建对象时手动调用，用于初始化对象属性值
# __str__ 是一个魔术方法，当使用print打印对象时，会自动调用该方法，该方法返回一个字符串，用于描述对象
# __new__ 是一个魔术方法，当实例化一个对象时，会自动调用该方法，该方法返回一个对象，用于创建对象
# __add__() 是重载运算符，当使用 + 运算符时，会自动调用该方法
# __sub__() 是重载运算符，当使用 - 运算符时，会自动调用该方法
# __lt__() 是重载运算符，当使用 < 运算符时，会自动调用该方法
# __le__() 是重载运算符，当使用 <= 运算符时，会自动调用该方法
# __eq__() 是重载运算符，当使用 == 运算符时，会自动调用该方法
# __ne__() 是重载运算符，当使用 != 运算符时，会自动调用该方法
# __gt__() 是重载运算符，当使用 > 运算符时，会自动调用该方法
# __ge__() 是重载运算符，当使用 >= 运算符时，会自动调用该方法
# __del__() 是析构方法，当对象被销毁时，会自动调用该方法
# 注意：
# 1、在创建对象时，new方法一定是最先执行的，这个方法是在申请一块内存空间给我们创建的对象使用，后续的 init 方法也是基于内存空间去构建对象的。
# 2、init 方法，这里手动调用是指我们需要去手动实例化一个对象，而在实例化对象的过程中就会去调用这个方法，因此就称为手动调用 init 方法。

class Person():
    def __new__(cls, *args, **kwargs):
        print('new方法执行了')
        # 我们这里只是想去打印语句，其余的所有操作都是依靠父类的
        # 这是在创建一个对象实例，得返回创建的结果

        # 如果不return创建的对象，那么最终person就是None
        return super().__new__(cls)

    def __init__(self, name, age):
        print('init方法执行了')
        self.name = name
        self.age = age

    def show(self):
        print(f'我的名字是{self.name},今年{self.age}岁')

    # 重写 str 方法 （不重写该方法会直接打印出对象在内存中的地址）
    def __str__(self):
        # 这里返回的一定得是一个str对象
        return f'姓名:{self.name},年龄:{self.age}'


# 类名() --> 这就是在实例化一个对象，并且会自动调用init方法，构造对象
person = Person('小明', '18')
print(person.__str__())
print(person)


# 特殊属性	描述
# obj.__dict__	对象的属性字典
# obj.__class__	对象所属的类
# class.__bases__	类的父类元组
# class.__base__	类的首个父类（括号内的第一个）
# class.__mro__	类的层次结构
# class.__subclasses__()	类的子类列表

class A():
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


a = A()
b = B()
c = C('c', 1)

print('对象的属性字典:')
print(a.__dict__)
print(b.__dict__)
print(c.__dict__)

print('对象所属的类:')
print(a.__class__)
print(b.__class__)
print(c.__class__)

print('类的父元组:')
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)

print('类的父类:')
print(A.__base__)
print(B.__base__)
print(C.__base__)

print('类的层次结构:')
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)

print('类的子类列表')
print(A.__subclasses__())
print(B.__subclasses__())
print(C.__subclasses__())

# (<class 'object'>,) 元组只有一个元素时，后面必须跟着","
# (<class '__main__.A'>, <class '__main__.B'>) 当类的父类不只是object时，父类元组中就不会显示出object类
# <class '__main__.A'> 首个父类
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>) 从本级到括号内每一级，object类一定在最后出现
