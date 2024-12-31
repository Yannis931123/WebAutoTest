import pandas as pd


def read_execl(file_path, **kwargs):
    execl_data_dict = []
    try:
        data = pd.read_excel(file_path, **kwargs)
        execl_data_dict = data.to_dict(orient='records')
    finally:
        return execl_data_dict


if __name__ == '__main__':
    file = 'D:\\Program Files\\WebAutoTest\\TestExampleExecl\\testdata.xls'
    data_dict = read_execl(file)
    print(data_dict)
