import statistics  # 引入statistics模块

print(statistics.median([19, -5, 36])) # statistics是模块名，median是函数名 median是中位数
print(statistics.mean([19, -5, 36])) # statistics是模块名，mean是函数名 mean是平均值
# statistics是模块名，median mean是函数名
# 用模块名.函数名 或者 模块名.变量名 去调用

from statistics import median, mean  # 引入statistics模块下的median mean函数，这样在调用的时候就不用去.了

print(median([19, -5, 36]))
print(mean([19, -5, 36]))
