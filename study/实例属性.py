class Dog():
    # 类属性
    sort = '中华田园犬'

    # 初始化对象的方法（构造方法）——>每个对象在创建时，都会调用它
    # 如果这里的name与age不使用"self."的话，就是一个局部变量了，而不再是实例变量
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    # 静态方法 ——>静态方法中不能出现与实例相关的属性或者方法，静态方法一般是起到函数的作用，用来执行什么样的功能
    @staticmethod
    def bark():
        print('这是一个静态方法，里面不能出现与实例相关的属性或者方法')

    # 类方法 ——>类方法中必须有一个参数，这个参数通常命名为cls,类方法通常用来操作与类相关的属性
    @classmethod
    def sort(cls):
        print('这是一个类方法，里面也不能出现与实例相关的属性或者方法')

    # 实例方法
    def roll(self):
        print(f'{self.name}正在地上打滚~')


# 实例化一个对象
# 实例属性与实例方法是通过对象去调用的 ——>对象.属性名()、对象.方法名()
dog_bai = Dog('大白', 5)  # 需要传入参数构造对象(__init__)
dog_bai.roll()

# 类属性、类方法、静态方法等都是通过类名去调用的 ——>类名.方法名()
Dog.bark()
Dog.sort()
