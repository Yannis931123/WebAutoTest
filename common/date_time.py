# datetime类包含了整个的时间（包括日期(年月日)+时间(时分秒)）
from datetime import datetime  # 导入datetime类


def base_url():
    return "https://passport.cnblogs.com/user/signinuser/signin"


def current_time():
    time = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(time)


def time_diff(start, end):
    time = "%a %b %d %H:%M:%S %Y"
    return datetime.strftime(end, time) - datetime.strftime(start, time)


# now()获取当前的系统时间(整个时间)
dt = datetime.now()
print(dt)

# 手动调用构造方法实例化一个类
dt = datetime(2024, 12, 20)  # 年月日必须要有
print(dt)
# 也可以拿到datetime的年月日这些参数
print(dt.year, dt.month, dt.day)

# datetime对象可以比较大小(对应的时间先后)
dt1 = datetime(2020, 1, 1)
dt2 = datetime(2024, 1, 1)
print('2020年1月1日 比 2024年1月1日 先到吗?', dt1 < dt2)  # 类似与数轴上的比较

# 格式化为字符串：将dt转换为 %Y-%m-%d 的格式
s = datetime.strftime(dt, '%Y-%m-%d')
print(s)

# 解析字符串：将字符串按照 %Y-%m-%d 的格式，转换为datetime对象
dt = datetime.strptime(s, '%Y-%m-%d')  # 格式一定要正确
print(dt)
