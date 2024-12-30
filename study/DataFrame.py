import pandas as pd
import pickle

# 创建一个字典
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}

dataframes = pd.DataFrame(data)  # 将这个字典转换为一个 DataFrame 对象，然后将其赋值给变量 df
# print(dataframes)

# 序列化data字典
serialized_data = pickle.dumps(data)
# print(serialized_data)

# 反序列化data字典
deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)
