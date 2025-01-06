import pytest
import os

import common.excel_util
from testcase.yaml_util import YamlUtil
from common.excel_util import ExcelUtil  # 从common包中导入ExcelUtil类


class Test_yaml():

    @pytest.mark.parametrize("args", YamlUtil("../data/interface.yaml").read_yaml())
    def test_yaml(self, args):
        print(args)
        interfaceName = args['interfaceName']
        url = args["url"]
        headers = args["headers"]

    def read_excel(self):
        # 第一步：加载文件
        wb = common.excel_util.ExcelUtil()
        # 第二步：获得sheet对象
        sheet = wb.read_excel()
        # 第三步：获得excel的行数和列数
        # print(sheet.max_row, sheet.max_column)
        all_list = []
        for rows in range(2, sheet.max_row + 1):  # 第二行开始，去掉行标题
            temp_list = []
            for cols in range(1, sheet.max_column + 1):
                # print(sheet.cell(rows, cols).value)
                temp_list.append(sheet.cell(rows, cols).value)
            # print(temp_list)  # 1、登录名 2、密码 3、验证码
            all_list.append(temp_list)

        # assert 2 == args["data"]["type"]
