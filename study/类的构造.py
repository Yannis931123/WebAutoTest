class Person:  # 定义类名用pascal命名方法（大驼峰CuteCat）#Person是类名
    # 类的构造方法，用于（初始化）对象，类似于属性:人的属性有名字和年龄  init是构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类的方法，就是这个类所可以被使用的方法，说明书:人会说你好
    def say_hello(self):  # say_hello是实例方法
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# 创建 Person 类的实例
# 创建实例的时候，括号里是构造函数的参数
person1 = Person("Alice", 30)  # 创建实例的时候，Alice作为name的参数，30作为age的参数
person2 = Person("Bob", 25)

# 调用实例的方法（用对象.方法来调用）
person1.say_hello()  # 调用了实例的方法：调用了person1这个实例的say_hello方法
person2.say_hello()


# 对象（实例）可以作为参数使用，参数间不尽相同
# 类 是创建对象的模板（结构）
# 对象 是类的实例（实际的例子）
# 调用实例的方法 （用实例.方法名来进行调用）（用的时候可以带上这个类中的属性）
# 获取对象的属性（用对象也就是实例.属性名来获取）

class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):  # 构造函数用于构造class本身的属性
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print("喵" * self.age)

    def think(self, content):
        print(f"小猫{self.name}在思考{content}...")


cat1 = CuteCat("JoJo", 2, "橙色")  # 通过class后面加括号调用init构造函数来 创建实例cat1 并且为对应属性进行赋值
cat1.think("现在去抓沙发还是去撕纸箱")  # 实例.方法名(参数)

print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")
