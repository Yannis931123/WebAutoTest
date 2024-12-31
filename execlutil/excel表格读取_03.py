# conding:utf-8
import xlrd
import xlwt
import xlutils
import os
import time

# 打开excel表格
data = xlrd.open_workbook('/TestExampleExecl/testdata.xls')

table1 = data.sheet_by_index(0)
table2 = data.sheet_by_index(1)
# table=data.sheet_by_name('Sheet1')

nrows1 = table1.nrows
ncols1 = table1.ncols
nrows2 = table2.nrows
nclos2 = table2.ncols

# print(table.row_values(2))
# print(table.col_values(1))

# 获取excel工作簿总数
nrows = table1.nrows
ncols = table1.ncols
# print(u"表数据行为(%d),列为(%d）"%(nrows1,ncols1))
# print(u"总行数为：",nrows)
# print(u"总列数为：",ncols)
# count=len(data.sheets())
# print(u"工作簿数为：",count)
#
# print(table2.row_values(2))
# print(table2.col_values(1))

# #循环读取数据sheet1
# for i in range(0,nrows1):
#     rowvalues1 = table1.row_values(i) #按行读取数据
#     #输出读取的数据
#     for sheet1 in rowvalues1:
#         print(rowvalues1,"")
#     print("")

# for i in range(nrows2):
#     if i == 0: #跳过首行，首行为title
#         continue
#     else:
#          rowvalue = table2.row_values(i)
#          print(rowvalue)

# #封装读取参数
# class ExcelUtil():
#     def __init__(self,excelPath,sheetName):
#         self.data = xlrd.open_workbook(excelPath)
#         self.table = self.data.sheet_by_name(sheetName)
#         #获取第一行作为key值
#         self.keys = self.table.row_values(0)
#         print(self.keys)
#         #获取总行数
#         self.rowNum = self.table.nrows
#         print(self.rowNum)
#         #获取总列数
#         self.colNum = self.table.ncols
#         print(self.colNum)
#
#     def dict_data(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
