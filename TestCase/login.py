my_name = 'yanxing'
my_password = '123456'


# input_name = input('请输入你的用户名：')
# input_password = input('请输入你的密码：')

def login():
    input_name = input('请输入你的用户名：')
    input_password = input('请输入你的密码：')

    if my_name == input_name and my_password == input_password:
        print('登录成功')
    else:
        print('登录失败')



    username = '123'
    userpassword = '12345'

    def loginUser():
        name = input('请输入你的用户名:')
        password = input('请输入你的密码:')

        if name == username and userpassword == password:
            print('登录成功~')
        else:
            print('登录失败')