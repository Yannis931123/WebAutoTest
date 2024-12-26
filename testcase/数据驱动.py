# 引入一个新包，pip install pandas
import pandas as pd


class readExcelMethod():
    """
    :fileName: 文件路径
    :sheetName: sheet页的名称
    """

    def __init__(self, fileName: str, sheetName='Sheet1'):
        self.fileName = fileName  # 文件路径
        self.sheetName = sheetName  # excel sheet页的名称
        super(readExcelMethod, self).__init__()

    def readExcel(cls):
        df = pd.read_excel(cls.fileName, sheet_name=cls.sheetName)
        df = df.T
        testData = []
        for i in range(len(df)):
            testData.append(list(df[i]))
        return testData
