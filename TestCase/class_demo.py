"""
定义一个学生类
1.属性包括学生姓名、学号、以及语数英三科的成绩
2.能够设置学生某客户的成绩
3.能够打印出该学生的所有科目成绩
"""


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}  # 不需要从参数里获取，可以直接定义

    def set_grades(self, course, grade):
        if course in self.grades:  # 判断科目是否在成绩中存在，不存在则不做set
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}学号{self.student_id}的成绩为：")
        for every_course in self.grades:
            print(f"{every_course}:{self.grades[every_course]}分")


chen = Student("小陈", "10086")
chen.set_grades("语文", "60")
chen.set_grades("数学", "70")
chen.set_grades("英语", "90")
chen.print_grades()

zeng = Student("小曾", "10010")
zeng.set_grades("语文", "30")
zeng.set_grades("数学", "20")
zeng.set_grades("英语", "10")
zeng.print_grades()

# print(chen.name)
# print(zeng.grades)
