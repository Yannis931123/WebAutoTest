import pandas as pd


def read_execl(file, **kwargs):
    execl_data_dict = []
    try:
        data = pd.read_excel(file, **kwargs)
        execl_data_dict = data.to_dict(orient='records')
    finally:
        return execl_data_dict


if __name__ == '__main__':
    file = 'D:\\Program Files\\WebAutoTest\\TestExampleExecl\\testdata.xls'
    data_dict_1 = read_execl(file)
    print(data_dict_1)
