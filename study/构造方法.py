"""
构造方法
"""

"""
__init__()方法，被称为构造方法，在创建类的对象时，会自动执行，在创建类对象的时候，会将传入的参数自动传递给__init__()方法。
__init__()方法可以有参数，也可以没有参数，当__init__()方法没有参数时，创建对象时不需要传递参数，当__init__()方法有参数时，创建对象时必须传递参数。
__init__()方法的作用：完成对象的初始化，可以理解成在创建对象时，自动调用执行的初始化操作。
在面向对象的编程中，类（Class）是创建对象的蓝图或模板，它定义了对象应有的属性和方法。
而对象（Object）或类的实例（Instance）则是根据类创建的具体个体，它拥有类中定义的属性和方法，并且可以有自己的状态（即属性值）。
"""
class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        # print("创建一个构造方法："+name+", "+str(age)+", "+str(tel))


stu = Student("xiaoming", 20, 12345678901)
print(stu.name)
print(stu.age)
print(stu.tel)

"""
__str__字符串方法：将类对象转化为字符串
"""


def __str__(self):
    return f"name:{self.name},age:{self.age}"


"""
__lt__比较大小，（不支持等于）
"""


class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("创建一个构造方法：" + name + ", " + str(age) + ", " + str(tel))

    def __lt__(self, other):
        return self.age < other.age


stu1 = Student("xiaoming", 20, 12345678901)
stu2 = Student("xioahong", 40, 12345678901)
print(stu1 > stu2)

"""
__le__(self, other)比较大小，（支持包含等于，但不支持==）
__eq__(self, other)比较大小，（支持包含等于，但不支持==）
"""


class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("创建一个构造方法：" + name + ", " + str(age) + ", " + str(tel))

    def __str__(self):  # 先把类对象转化为字符串
        return f"name:{self.name},age:{self.age}"

    def __le__(self, other):
        return self.age <= other.age


stu1 = Student("xiaoming", 20, 12345678901)
stu2 = Student("xioahong", 40, 12345678901)
print(stu1 >= stu2)
print(stu1 <= stu2)

"""
__le__(self, other)比较是否相等
"""


class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("创建一个构造方法：" + name + ", " + str(age) + ", " + str(tel))

    def __str__(self):
        return f"name:{self.name},age:{self.age}"

    def __eq__(self, other):
        return self.age <= other.age


stu1 = Student("xiaoming", 40, 12345678901)
stu2 = Student("xioahong", 20, 12345678901)
stu3 = Student("nihao", 20, 12345678901)
print(stu1 == stu2)
print(stu3 == stu2)