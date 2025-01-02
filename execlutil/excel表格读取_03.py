# conding:utf-8
import xlrd
import xlwt
import xlutils
import os
import time

# 打开excel表格
data = xlrd.open_workbook('../TestExampleExecl/testdata.xls')

# 根据sheet索引定位table
table1 = data.sheet_by_index(0)
table2 = data.sheet_by_index(2)
# table=data.sheet_by_name('Sheet1')

# 获取excel工作簿总行数和总列数
table1_rows = table1.nrows
table1_cols = table1.ncols
table2_rows = table2.nrows
table2_cols = table2.ncols

# print(table1.row_values(2))
# print(table2.col_values(1))
#
# print(u"表数据行为(%d),列为(%d）" % (table1_rows, table1_cols))
# print(u"总行数为：", table1_rows)
# print(u"总列数为：", table1_cols)
# count = len(data.sheets())
# print(u"工作簿数为：", count)
#
# print(table2.row_values(2))
# print(table2.col_values(1))

# 循环读取数据sheet1
# for i in range(0, table1_rows):
#     table1_row_values = table1.row_values(i)  # 按行读取数据
#     # 输出读取的数据
#     for sheet1 in table1_row_values:
#         print(table1_row_values, "")
#     print("")

for i in range(table2_rows):
    if i == 0:  # 跳过首行，首行为title
        continue
    else:
        table2_row_values = table2.row_values(i)
        print(table2_row_values)

# # 封装读取参数
# class ExcelUtil():
#     def __init__(self, excelPath, sheetName):
#         self.data = xlrd.open_workbook(excelPath)
#         self.table = self.data.sheet_by_name(sheetName)
#         # 获取第一行作为key值
#         self.keys = self.table.row_values(0)
#         print(self.keys)
#         # 获取总行数
#         self.rowNum = self.table.nrows
#         print(self.rowNum)
#         # 获取总列数
#         self.colNum = self.table.ncols
#         print(self.colNum)
#
#     def dict_data(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
