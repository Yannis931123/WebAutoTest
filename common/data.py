import pandas as pd

def read_execl(file,**kwargs):
    data_dict=[]
    try:
        data=pd.read_excel(file,**kwargs)
        data_dict=data.to_dict(orient='records')
    finally:
        return  data_dict

if __name__ == '__main__':
    file = 'D:/python/test.xlsx'
    data_dict = read_execl(file)
    print(data_dict)
