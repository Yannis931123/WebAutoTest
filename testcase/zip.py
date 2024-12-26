# 这个函数用于将两个（或多个）可迭代对象（例如列表、元组等）的元素组合成一个迭代器
# 组合list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
result = list(zip(list1, list2))
print(result)

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)

# 组合元组
head_data_tuple1 = ('a', 'b', 'c')
one_tuple1 = (1, 2, 3)

zipped = zip(head_data_tuple1, one_tuple1)

# 转化为列表以便查看结果
zipped_list = list(zipped)

print(zipped_list)
