import pandas as pd

file = '/TestExampleExecl/testdata.xls'
wb = pd.read_excel(file, sheet_name='Sheet1', header=0)
# print(wb)

# # 获取行索引
# print(wb.index)
# print(wb.index[0])

# # 获取列索引
# print(wb.columns)
# print(wb.columns[1])

# #根据列索引选择数据
# #选择多列
# print(wb.iloc[:, 2])  # 读取前3列  wb.iloc[:, 2]

# # 选择连续的多列
# print(wb.iloc[:, 1:5])  # 读取所有行，列是1到5列；iloc[行切边，列切片]

# # 根据行索引选择数据
# row = [1]
# print(wb.loc[row])  # 读取行索引为1的一行（行索引从0开始），即读取第2行

# # 选择多行
# rows = [0, 2]
# print(wb.loc[rows])  # 读取行索引为0和2的多行， 即读取第1行和第3行

# # 选择连续的多行
# print(wb.iloc[0:1])  # 读取行索引从0到1的连续行，即读取第1行到第2行

# # 读取所有内容
# print(wb.values)

# # 读取指定单元格
# print(wb.iloc[1, 2])  # 读取行索引=1，第2个列索引的单元格，即读第2行第3列的单元格
