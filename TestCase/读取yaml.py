import yaml


class yamlUtil():
    def __init__(self, yaml_file):
        '''
        通过init把文件传入到这个类
        :param yaml_file:
        '''
        self.yaml_file = yaml_file

    # 读取ymal文件
    def read_yaml(self):
        '''
        读取yaml，将yaml反序列化，就是把我们yaml格式转换成dict格式
        :return:
        '''
        with open(self.yaml_file, encoding="utf-8") as f:
            value = yaml.load(f,
                              Loader=yaml.FullLoader)  # 文件流，加载方式 #推荐使用 FullLoader 作为默认的加载器，因为它提供了完整的 YAML 功能，同时避免了安全风险
            print(value)


if __name__ == '__main__':
    yamlUtil("./interface.yaml").read_yaml()
