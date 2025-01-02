import pytest
import xlrd


def get_data():
    filename = "../TestExampleExecl/testdata.xls"
    # 读取工作簿
    wb = xlrd.open_workbook(filename)
    # 读取第一个sheet页 根据索引
    test_sheet = wb.sheet_by_index(0)
    # test_sheet = wb.sheet_by_name('Sheet1')
    # 读取行
    rows = test_sheet.nrows
    # 读取列
    cols = test_sheet.ncols

    lst = []
    for row in range(rows):  # 遍历行
        for col in range(cols):  # 遍历列
            # 根据行列获得单元格数据
            cell_data = test_sheet.cell_value(row, col)  # 获取单元格数据
            lst.append(cell_data)
    return lst


@pytest.mark.parametrize('name', get_data())  # 参数化
def test1(name):
    print(name)


if __name__ == '__main__':
    pytest.main(['-sv', 'test.xls'])
