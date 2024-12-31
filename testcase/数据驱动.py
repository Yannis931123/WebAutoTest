# 引入一个新包，pip install pandas
import pandas as pd


class readExcelMethod():
    """
    :fileName: 文件路径
    :sheetName: sheet页的名称
    """

    def __init__(self, file_name: str, sheet_name='Sheet1'):
        self.fileName = file_name  # 文件路径
        self.sheetName = sheet_name  # excel sheet页的名称
        super(readExcelMethod, self).__init__()

    def read_excel(cls):
        df = pd.read_excel(cls.fileName, sheet_name=cls.sheetName)
        df = df.T
        test_data = []
        for i in range(len(df)):
            test_data.append(list(df[i]))
        return test_data

