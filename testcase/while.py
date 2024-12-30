# for 变量名 in 可迭代对象
# 对每个变量做一些事情
# 字典名.keys() # 所有键
# 字典名.values() # 所有值
# 字典名.items() #所有键值对

# temperature_dict = {"111":36.4,"112":36.6,"113":36.2,"114":39}
# for staff_id,temperature in temperature_dict.items()
#     if temperature >= 38:
#     print(staff_id)
#

# range 左闭右开区间 右边取不到
total = 0
for i in range(1, 101):
    total = total + i
# print(total)

print("这是一个求平均值的程序")
total = 0
count = 0
user_input = input("请输入数字（完成所有数字输入后，请输入Q终止程序）")
while user_input != "Q":
    mum = float(user_input)
    total += mum
    count += 1
    user_input = input("请输入数字（完成所有数字输入后，请输入Q终止程序）")
if count == 0:
    result = 0
else:
    result = total / count
print("您输入的数字的平均值为" + str(result))
