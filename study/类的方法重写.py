"""
当子类继承父类时，子类就拥有了父类中的 公有成员、方法和受保护的成员、方法。
如果我们对父类中有些成员不满意的话，子类就可以重新定义成员。
同理，方法也是如此，但是重新定义方法麻烦了，那有什么办法呢？方法重写，即 偷梁换柱，表面上这个方法还是原来的方法，但是其内部实现的结构早就发生变化了。

**重写的要求：方法名必须一样，至于方法的返回值类型，参数列表、访问权限这些可以不一样***
"""


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃食物，补充体力')


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # 由于Animal类的eat方法只是随便说在吃啥，并不具体，
    # 但我们想要打印出具体的食物，因此可以重写（外壳不变，核心变化）
    def eat(self):
        print(f'{self.name}正在吃狗粮~')


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


dog = Dog('大白', 5)
# 子类重写父类的方法之后，父类再去调用eat方法，就不再是调用父类的，而是自己的
dog.eat()

cat = Cat('小白', 3)
# 子类没有重写父类的eat方法，因此还是去调用父类的eat方法
cat.eat()
