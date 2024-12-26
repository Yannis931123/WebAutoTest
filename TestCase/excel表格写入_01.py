import os
import xlwt


def write_excel():
    wbk = xlwt.Workbook()
    # sheet表取名为order
    sheet01 = wbk.add_sheet('order')
    # 将每行数据放到一个元组中，将所有数据放到一个list中，写入excel
    testdata = [('id', 'title', 'env', 'url', 'method', 'request_data', 'status_code', 'res_type', 'extract',
                 'expect_data', 'sql'), ('1', '登录成功获取token', 'SIT', 'https://test-mrjade.com/admin/token', 'post',
                                         '{\n"json":{"password":"1234","username":mrjade"}\n}', '200', 'json',
                                         '[["token","$.."]]'), (
                '2', '注册', 'SIT', 'https://test-mrjade.com/admin/register', 'post',
                '{\n"json":{"password":"1234","username":mrjade"}\n}', '200', 'json')]
    # 遍历数组（excel行数据）
    for i in range(len(testdata)):
        print(testdata[i])
        # 遍历数组中的元组（行单元格数据）
        for j in range(len(testdata[i])):
            # 将数据写入excel，i表示第几行，j表示单元格
            sheet01.write(i, j, testdata[i][j])
    # excel保存目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_testdata = base_dir + '/../TestExampleExecl/testcases.xls'
    # 保存
    wbk.save(save_testdata)


if __name__ == '__main__':
    write_excel()