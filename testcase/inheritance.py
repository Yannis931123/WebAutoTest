class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eye = 2

    def breathe(self):
        print(self.name + "在呼吸")

    def poop(self):
        print(self.name + "在排便")


class Human(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)#调用父类的构造函数，继承父类的所有属性
        self.has_tail = False

    def read(self):
        print(self.name + "在阅读")


class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True

    def scrath_sofa(self):
        print(self.name + "在抓沙发")


cat1 = Cat("JoJo", "男")
print(cat1.name)
cat1.poop()
