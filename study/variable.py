"""
银行案例，可以在主菜单中查询余额、存款、取款和退出
"""

money = 5000000

name = input("请输入您的姓名：")


def query(show_header):
    if show_header:
        print("查询余额")
    print(f"{name}，您好，您的账户余额：{money}元")


def saving(num):
    global money
    money += num
    print("存款")
    print(f"{name}，存款成功，当前余额：{money}元")
    query(False)


def get_money(num):
    global money
    if num <= money:
        money -= num
        print("取款")
        print(f"{name}，取款成功，当前余额：{money}元")
    else:
        print("余额不足")
    query(False)


# 定义主菜单函数
def main_menu():
    print("主菜单")
    print(f"{name}，您好，欢迎来到银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")


# 设置无线循环，除非用户选择退出
while True:
    keyword_input = main_menu()
    if keyword_input == '1':
        query(True)
        continue
    elif keyword_input == '2':
        saving(float(input("请输入存款金额：")))
        continue
    elif keyword_input == '3':
        get_money(float(input("请输入取款金额：")))
        continue
    elif keyword_input == '4':
        print("感谢使用本系统，再见！")
    else:
        print("无效输入，请重新输入！")
        break
