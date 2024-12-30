import yaml

f = open('../data/test_data.yaml', 'r', encoding='utf-8')
cfg = f.read()
d = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load转字典
# yaml5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定Loader，通过默认加载器（FullLoader）禁止执行任意函数
# Loader=yaml.FullLoader 加上这行代码，告警就没了
print(d)

import yaml
import os


class GetYaml():
    def __init__(self, file_path):
        # 判断文件是否存在
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            print('没有找到%s文件路径' % file_path)

        self.data = self.read_yaml()

    def read_yaml(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            p = f.read()
            return p

    def get_data(self, key=None):
        result = yaml.load(self.data, Loader=yaml.FullLoader)
        # 判断key是否存在
        if key is None:
            return result
        else:
            return result.get(key)


if __name__ == '__main__':
    read_yaml = GetYaml('../data/test_data.yaml')  # 实例化，并且传递yaml文件的路径到类中
    r = read_yaml.get_data()
    print(r)
