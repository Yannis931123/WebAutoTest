import xlrd

wb = xlrd.open_workbook('../TestExampleExecl/testdata.xls')  # 打开Excel文件
test_sheet = wb.sheet_by_name('Sheet1')  # 打开工作表 根据sheet名
rows = test_sheet.nrows
cols = test_sheet.ncols
name = test_sheet.name
# print('总行数：{}， 总列数：{}, 工作表名：{}'.format(rows, cols, name))
#
# # 按行读取
# row1 = test_sheet.row_values(0)  # 行的索引值是从0开始
# print('第一行内容：', row1)
#
# # 按列读取
# col1 = test_sheet.col_values(0)  # 列的索引值是从0开始
# print('第一列内容：', col1)
#
# # 单元格读取
# cell1 = test_sheet.cell(1, 0).value
# print('A2单元格内容：', cell1)

# 将每一行的值读取出来放在列表中
data = []
# 遍历从第二行（索引为1，因为索引从0开始计数）开始到最后一行
for row_idx in range(1, test_sheet.nrows):
    row_data = []
    # 遍历当前行的每一列
    for col_idx in range(0, test_sheet.ncols):
        cell_value = test_sheet.cell_value(row_idx, col_idx)
        row_data.append(cell_value)
    data.append(row_data)
print(data)
