# s = "hello"
# print(s.upper())
# s = s.upper()
# print(s)

shopping_list = ["键盘", "键帽"]
shopping_list.append("显示器")
print(shopping_list)
shopping_list.remove("键盘")
print(shopping_list)
print(len(shopping_list))
shopping_list[1] = "音响"
print(shopping_list)

price = [799, 1024, 200, 800]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
print(max_price)
print(min_price)
print(sorted_price)

name_list = ['itheima', 'itcast', 'python']
print(name_list)
print(type(name_list))

name_list.append('java')
print(name_list)

name_list.remove('itcast')
print(name_list)

statistic_list = [[1, 2, 3], [4, 5, 6]]
print(statistic_list)
print(type(statistic_list))

name_list1 = ["itheima", 666, True]
print(name_list1)
print(type(name_list1))
"""
下标索引
"""
# 通过下标索引取出对应位置的数据
print(name_list1[0])
print(name_list1[1])
print(name_list1[2])

# 取出嵌套元素列表
print(statistic_list[1][2])  # 取的是第二个列表的第三个元素
"""
列表常用的方法
列表.append(元素) ：向列表末尾添加新的元素
列表.remove(元素) ：删除列表中某个值的第一个匹配项
列表.pop([索引]) ：删除列表中某个值的第一个匹配项，并返回该元素
列表.clear() ：清空列表
列表.extend(容器) ：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表），将数据容器中的内容依次取出，追加到列表末尾
列表.insert(下标, 元素) ：将元素插入列表
del 列表[下标] ：删除列表中下标对应的元素
列表.index(元素) ：从列表中找出某个值第一个匹配项的索引位置
列表.count(元素) ：统计某个元素在列表中出现的次数
列表.sort() ：对原列表进行排序
列表.reverse() ：对原列表进行反转
列表.copy() ：返回列表的浅复制，也就是返回一个新的列表
len(列表) ：列表元素个数,统计容器内有多少个元素
列表[开始索引:结束索引:步长] ：切片操作
列表[开始索引:结束索引] ：切片操作
列表[开始索引:] ：切片操作
列表[:结束索引] ：切片操作
列表[::步长] ：切片操作
列表1 + 列表2 ：连接两个列表
列表1 * 2 ：复制列表
列表1 *= 2 ：复制列表  
列表1 < 列表2 ：比较两个列表的大小
列表1 > 列表2 ：比较两个列表的大小
列表1 == 列表2 ：比较两个列表的大小
列表1 != 列表2 ：比较两个列表的大小
列表1 <= 列表2 ：比较两个列表的大小
列表1 >= 列表2 ：比较两个列表的大小
列表1 in 列表2 ：判断一个列表是否是另一个列表的子集
列表1 not in 列表2 ：判断一个列表是否是另一个列表的子集
列表1 | 列表2 ：列表的并集
列表1 & 列表2 ：列表的交集
列表1 ^ 列表2 ：列表的差集
列表1 % 列表2 ：列表的对称差集
列表1 // 列表2 ：列表的元素除法
列表1 @ 列表2 ：列表的元素乘法
列表1 << 列表2 ：列表的元素左移动
列表1 >> 列表2 ：列表的元素右移动
列表1 |= 列表2 ：列表的并集赋值
列表1 &= 列表2 ：列表的交集赋值
列表1 ^= 列表2 ：列表的差集赋值
列表1 //= 列表2 ：列表的元素除法赋值
列表1 @= 列表2 ：列表的元素乘法赋值
列表1 <<= 列表2 ：列表的元素左移动赋值
列表1 >>= 列表2 ：列表的元素右移动赋值
列表1 | 列表2 ：列表的或运算
列表1 & 列表2 ：列表的与运算
列表1 ^ 列表2 ：列表的异或运算
列表1 |= 列表2 ：列表的或运算赋值
列表1 &= 列表2 ：列表的与运算赋值
列表1 ^= 列表2 ：列表的异或运算赋值
"""
