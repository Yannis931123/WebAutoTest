import pytest
import xlrd
def get_data():
    filename = "D:\\Program Files\\WebAutoTest\\TestExampleExecl\\testdata.xls"
    # 读取工作簿
    wb = xlrd.open_workbook(filename)
    # 读取第一个sheet页 根据索引
    ws1 = wb.sheet_by_index(0)
    # ws1 = wb.sheet_by_name('Sheet1')
    # 读取行
    rows = ws1.nrows
    # 读取列
    cols = ws1.ncols

    lst = []
    for row in range(rows):
        for col in range(cols):
            # 根据行列获得单元格数据
            cell_data = ws1.cell_value(row, col)
            lst.append(cell_data)
    return lst


@pytest.mark.parametrize('name', get_data())
def test1(name):
    print(name)


if __name__ == '__main__':
    pytest.main(['-sv', 'test.xls'])
