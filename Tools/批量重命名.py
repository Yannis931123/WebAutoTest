"""批量重命名指定目录下的所有文件，添加前缀"""
import os
from datetime import date
import openpyxl

# 定义数据源表格
excel_file = r'D:\Program Files\WebAutoTest\TestExampleExecl\opensource_cve_2024.xlsx'
# 获取当前日期
current_date = date.today().strftime('%Y%m%d')

# 读取Excel文件
re = openpyxl.open(r'D:\Program Files\WebAutoTest\TestExampleExecl\opensource_cve_2024.xlsx')
# 遍历表格中的每一行数据的第一列和第二列，每一行的两个数据放在一起，格式为[{}，{}]，将所有数据存入列表
data = []
for row in re.active.iter_rows(min_row=2, values_only=True):  # min_row=2 表示从第二行开始读取数据 values_only=True 表示只读取单元格的值
    data.append([row[0], row[1]])  # 将第一列和第二列的数据放在一起，格式为[{}，{}] row[0]表示第一列的数据，row[1]表示第二列的数据
# 遍历列表中的每一个元素，每一个元素是一个列表，列表中的第一个元素是第一列的数据，第二个元素是第二列的数据
for item in data:
    # 获取第一列的数据
    first_column_data = item[0]
    # 获取第二列的数据
    second_column_data = item[1]
print(data)


def batch_rename_files(directory):  # 接受1个参数：directory（要重命名文件的目录
    index = 0  # 用于记录当前遍历到data列表中的位置索引
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        if index < len(data):  # 确保索引不超出data列表范围
            # 获取data列表中的第一个元素和第二个元素，分别赋值给first_name和second_name
            first_name = data[index][0]  # data[index][0]表示data列表中的第一个元素
            second_name = data[index][1]  # data[index][1]表示data列表中的第二个元素
            # 构造新文件名，格式为：从data[]中遍历每一组数据：first_column_data _ second_column_data _ current_date
            new_name = f"{first_name}_{second_name}_{current_date}.xlsx"
            # 使用os.rename函数重命名文件，第一个参数是原文件的完整路径，第二个参数是新文件的完整路径
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            index += 1  # 每次遍历完一个文件，将索引加1
            # 如果索引大于等于data列表的长度，则跳出循环
        else:
            break
        # 构造新文件名，格式为：从data[]中遍历每一组数据：first_column_data _ second_column_data _ current_date
        # 将data[]中的每一组数据遍历出来，每一组的first_column_data和second_column_data都取出来
        # 将first_column_data和second_column_data拼接起来，中间用下划线连接，再加上current_date，最后拼接成一个字符串
        # 将拼接好的字符串赋值给new_name

    print(f"已将目录 {directory} 下的所有文件重命名为带有对应前缀的文件名。")


# 使用示例
batch_rename_files(directory=r'D:\Program Files\WebAutoTest\TestExampleExecl\files_to_rename')
