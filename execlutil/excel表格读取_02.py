import xlrd

wb = xlrd.open_workbook('/TestExampleExecl/testdata.xls')  # 打开Excel文件
ws1 = wb.sheet_by_name('Sheet1')  # 打开工作表 根据sheet名
rows = ws1.nrows
cols = ws1.ncols
name = ws1.name
print('总行数：{}， 总列数：{}, 工作表名：{}'.format(rows, cols, name))

# 按行读取
row1 = ws1.row_values(0)  # 行的索引值是从0开始
print('第一行内容：', row1)

# 按列读取
col1 = ws1.col_values(0)  # 列的索引值是从0开始
print('第一列内容：', col1)

# 单元格读取
cell1 = ws1.cell(1, 0).value
print('A2单元格内容：', cell1)
