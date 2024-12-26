"""
捕获、抛出和处理异常
异常捕获的完整用法：
try:
    pass
except:
    pass
else:
    # 没有异常才会执行的代码
finally:
    # 无论是否出现错误，都会被执行的代码

（else 只有在没有异常时，才会执行的代码）
（finally 无论是否有异常，都会执行的代码）

"""

# try:
#     input_s = int(input("输入整数："))
# except:
#     print("输入异常，请重新输入")
#
# print("-" * 50)


# try:
#     input_s = int(input("输入整数："))
# except Exception as result:
#     print("输入异常，异常原因：%s,请重新输入" % result)


# try:
#     input_s = int(input("输入整数："))
#     print(8 / input_s)
# except ValueError as value_error:
#     print("输入值有误")
# except ZeroDivisionError as zero_division_error:
#     print("除0错误")
# except Exception as result:
#     print("输入异常，异常类型%s,异常信息%s,请重新输入" % (type(result), result))
#
# print("-" * 50)

try:
    input_s = int(input("输入整数："))
    result = 8 / input_s
except ValueError as value_error:
    print("输入值有误")
except ZeroDivisionError as zero_division_error:
    print("除0错误")
except Exception as result:
    print("输入异常，异常类型%s,异常信息%s,请重新输入" % (type(result), result))
else:
    print("没有异常，结果为：")
    print(result)
finally:
    print("无论是否出现错误，都会执行的代码")
    print("-" * 50)


def exception1():
    pwd = input("请输入密码")
    if len(pwd) < 8:
        raise Exception("初始化密码失败，密码不能少于8位")


try:
    exception1()
except Exception as res:
    print("输入异常，异常类型%s,异常信息%s,请重新输入" % (type(res), res))

