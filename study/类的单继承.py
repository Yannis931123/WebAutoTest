"""
在Python中一个子类可以继承N多个父类，这是与 Java决然不同的一点。Java属于单继承，而Python属于多继承，并且每个类都默认继承自object类。当然，一个子类可以有多个父类，一个父类也可以有多个子类。
类继承练习：人力系统
1.员工分为两类：全职员工 FullTimeEmployee 兼职员工 PartTimeEmployee
2.全职员工和兼职都有"姓名 name" "工号 id"属性
3.都具备打印信息 print_info（打印姓名、工号）的方法
4.全职员工有：月薪 monthly_salary 的属性 兼职员工有：日薪 daily_salary 每月工作天数 work_days 的属性
5.全职和兼职都有：计算月薪 calculate_monthly_pay 的方法，但是具体计算过程不一样
"""


# 定义一个父类 Employee
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Employee都有一个打印信息的方法
    def print_info(self):
        print(f"员工名字：{self.name},工号：{self.id}")


# 定义一个子类 FullTimeEmployee 继承 Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)  # 调用父类的构造函数，以初始化父类的属性name和id
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


# 定义一个子类 PartTimeEmployee 继承 Employee
class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)  # 调用父类的构造函数，以初始化父类的属性name和id
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days


zhangsan = FullTimeEmployee("张三", "1001", 6000)
lisi = PartTimeEmployee("李四", "1009", 230, 15)
zhangsan.print_info()
lisi.print_info()
print(zhangsan.calculate_monthly_pay())
print(lisi.calculate_monthly_pay())
