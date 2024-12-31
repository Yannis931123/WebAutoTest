"""
我们在实例化一个对象时，会先去调用构造方法（init 方法）给对象的属性进行初始化赋值，
如果一个类没有构造方法，但是由于这个类是默认继承自object类，因此会调用object类中默认的 init 方法，
但如果这个类继承了其他类，就会先在其他类中去搜索这个方法，如果有则调用；
反之，则还是去调用object类的。 而在上面的代码中，Animal 类是有 init 方法，因此会去调用Animal 类的。
"""


class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f'我叫{self.name},今年{self.age},性别是{self.gender}')


class Father(Person):
    def __init__(self, name, age, gender):
        # 可以直接调用父类的初始化方法
        super().__init__(name, age, gender)
        # 下面这种方式是错误的
        # super().name = name
        # super().age = age
        # super().gender = gender
        # 下面的方式也行，但是不推荐
        # self.name = name
        # self.age = age
        # self.gender = gender


class Mother(Person):
    def __init__(self, name, age, gender):
        # 可以直接调用父类的初始化方法
        super().__init__(name, age, gender)
        # 下面这种方式是错误的
        # super().name = name
        # super().age = age
        # super().gender = gender
        # 下面的方式也行，但是不推荐
        # self.name = name
        # self.age = age
        # self.gender = gender


class Son(Father, Mother):
    def __init__(self, name, age, gender):
        # 可以直接调用父类的初始化方法
        super().__init__(name, age, gender)
        # 默认是按照父类在Son()中的顺序来查找的，这里是Father类定义声明在前，因此这里调用的就是 Father 类的 init 方法
        # 如果想要指定某个类的 init 方法的话，就需要使用 类名.init() 方法
        # Mother.__init__(self, name, age, gender)

        # 下面这种方式是错误的
        # super().name = name
        # super().age = age
        # super().gender = gender
        # 下面的方式也行，但是不推荐
        # self.name = name
        # self.age = age
        # self.gender = gender


father = Father('A', 40, '男')
mother = Mother('B', 35, '女')
son = Son('C', 10, '男')

father.show()
mother.show()
son.show()