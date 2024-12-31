# class A():
#     pass
#
#
# a = A()
# b = a
# print(a)
# print(b)


# 按照我们在前面所学的知识，这里是创建了一个A类，并且实例化了一个对象a，最后把a赋值给了b， 但由于 a 指向的是一个对象，因此 b 也指向了 a 这个对象。
# 也就是说，a 和 b 指向了同一个对象，因此，修改 a 的属性，b 的属性也会随之改变，反之亦然。
# 用专业化的术语，b = a，称b指向了a所指向的对象，上述的过程也可以认为是拷贝。

class Person():
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我叫{self.name},今年{self.age}岁了')


dog = Dog('小狗', 3)
person1 = Person('小明', dog)
# person2 指向了 person1 所指向的对象
person2 = person1
print(f'person1.dog == person2.dog?{person1.dog == person2.dog}')
# 修改 person2 所指向的dog的属性
person2.dog.name = '大白'
# 再打印person1 与 person2 的pet
person1.dog.show()
person2.dog.show()
# 可以看到，person1 和 person2 的pet属性都发生了改变，说明person1 和 person2 指向的是同一个对象
# 此时把 person1 所指向的对象 拷贝一份 赋值给 person2(这里不是变量赋值，而是对象赋值)
import copy  # 导包

person2 = copy.copy(person1)  # 浅拷贝
print(f'person1.dog == person2.dog吗?{person1.dog == person2.dog}')
# 再修改 person2 所指向的dog的属性
person2.dog.name = '小猫'
person1.dog.show()
person2.dog.show()

# 要是实在不理解，就记住，浅拷贝与深拷贝不同的结果，只是针对可变对象的，对于哪些不可变对象不存在这样的问题(字符串是不可变对象)
person2.name = '小红'
print(person2.name)
print(person1.name)  # 修改person2的name属性，person1的name属性不会发生改变

# 那如果要把浅拷贝改为深拷贝呢？可以利用 copy 模块中的 deepcopy函数，来将子对象来拷贝。因此我们上面的代码也只需要将copy.copy() 改为 copy.deepcopy()即可
person2 = copy.deepcopy(person1)  # 深拷贝
print(f'person1.dog == person2.dog吗?{person1.dog == person2.dog}')
