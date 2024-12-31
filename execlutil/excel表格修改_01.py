import os
import xlrd
from xlutils.copy import copy


def edit_excel():
    # excel目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_testdata = base_dir + '/../TestExampleExecl/testcases.xls'
    # 打开excel
    workbook = xlrd.open_workbook(save_testdata)
    workbook_new = copy(workbook)
    ws = workbook_new.get_sheet(0)
    # 将第3行，第2列修改为注册成功
    ws.write(2, 1, '注册成功')
    # 保存修改后的excel
    workbook_new.save(save_testdata)


if __name__ == '__main__':
    edit_excel()
