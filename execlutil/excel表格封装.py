# coding:utf-8
import xlrd


class ExeclUtil:
    def __init__(self, excelpath, sheetname="Sheet1"):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        self.key = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.key[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    filepath = '/TestExampleExecl/testdata.xls'
    sheetName = "Sheet1"
    data = ExeclUtil(filepath, sheetName)
    print(data.dict_data())

    # def get_data(self,file_name,sheet_id):
    #     data = xlrd.open_workbook(file_name)
    #     tables = data.sheets()[sheet_id]
    #     return tables
    #
    # def get_lines(self):
    #     return self.data.nrows
    #
    # def get_column(self,line):
    #     return self.data.row_values(line)
    #
    # def get_cell_value(self,line,col):
    #     return self.data.cell_value(line,col)
    #
    # def get_data_by_line(self,line):
    #     return self.data.row_values(line)
    #
    # def get_data_by_col(self,col):
    #     return self.data.col_values(col)
    #
    # def get_data_by_index(self,index):
    #     return self.data.cell_value(index[0],index)
