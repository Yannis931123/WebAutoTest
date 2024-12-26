"""
random模块，用于生成伪随机数，之所以称之为伪随机数，是因为真正意义上的随机数（或者随机事件）在某次产生过程中是按照实验过程中表现的分布概率随机产生的，其结果是不可预测的，是不可见的
random.randint(起始整数, 结束整数)：随机生成一个在起始整数和结束整数之间的整数，包含起始整数和结束整数
random.random()：随机生成一个0到1之间的浮点数
random.choice(非空序列)：从序列中随机选择一个元素并返回
random.shuffle(序列)：将序列中的元素随机排序
random.uniform(起始值, 结束值)：随机生成一个在起始值和结束值之间的浮点数
random.randrange(起始值, 结束值, 步长)：随机生成一个在起始值和结束值之间的整数，步长
random.sample(序列, 数量)：从序列中随机选择指定数量个元素并返回，从序列中选择k个随机且独立的元素,返回一个列表
random.getrandbits(k)：随机生成一个k位二进制整数
random.seed(整数)：设置随机种子
random.choices(序列, 权重)：根据权重随机选择一个元素并返回
random.paretovariate(alpha)：生成一个帕累托分布的随机数
random.weibullvariate(alpha, beta)：生成一个威布尔分布的随机数
random.expovariate(lambda)：生成一个指数分布的随机数
random.gauss(mu, sigma)：生成一个高斯分布的随机数
random.lognormvariate(mu, sigma)：生成一个对数正态分布的随机数
random.vonmisesvariate(mu, k)：生成一个冯米塞斯分布的随机数
"""
# 打印随机数字，猜数字游戏
import random

num = random.randrange(1, 100)  # 随机一个1到100的正整数
print(num)
input1 = int(input("输入一个数字："))
if input1 == num:
    print("猜对了！")
else:
    print("猜错了！")

# ===randint=====================
print(random.randint(1, 100))
# ===choice======================
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(list_1))
# ===choices======================
list1 = [1, 2, 3, 4, 5]
list_weights = [0, 0, 0, 1, 0]
list_cum_weights = [1, 1, 1, 1, 1]
print(random.choices(population=list1, cum_weights=list_cum_weights, k=5))

"""
cum_weights=[1, 1, 1, 1, 1] 
• 等价于 weights=[1, 0, 0, 0, 0]
• [1,1+0,1+0+0,1+0+0+0,1+0+0+0+0]
• 看懂了没，太反人类了。。

cum_weights=[1, 4, 4, 4, 4] 
• 等价于 weights=[1, 3, 0, 0, 0]
• [1,1+3,1+3+0,1+3+0+0,1+3+0+0+0]
"""

print(random.sample([1, 2, 3, 4, 5], 3))
