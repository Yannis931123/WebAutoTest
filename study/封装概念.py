"""
单下划线：表示protected，受保护的成员，这类成员被视为仅供内部家族使用，允许类本身和子类进行访问，但实际上它可以被外部代码访问
双下划线：表示private，私有成员，只能在类内部访问，子类和外部类都无法访问
首尾双下划线：表示特殊的方法
"""


class Dog():
    # 首尾双线划线 ——> 特殊方法
    def __init__(self, name, age):
        # 双下划线开头 ——> private修饰，只能在类内访问
        self.__name = name
        # 单下划线开头 ——> protected修饰，在类内与子类才能访问
        self._age = age

    # 单下划线开头 ——> protected修饰，在类内与子类才能访问
    def _fun1(self):
        print('这是被protected所修饰的方法')

    # 双下划线开头 ——> private修饰，在类内才能访问
    def __fun2(self):
        print('这是被private所修饰的方法')


# 这里是类外了
dog = Dog('大白', 5)
print(dog._age)
# print(dog.__name)
dog._fun1()
# dog.__fun2()
# 和上面一样，直接去访问的话，就会报错，
# 但是我们可以使用 对象.__dir()__ 或者 dir(对象) 先去查看所有的属性与方法
# 然后通过其中的"属性"与"方法名"去调用真正的属性与方法
# print(dog.__dir__())
# print(dir(dog))

print(dog._Dog__name)
dog._Dog__fun2()
