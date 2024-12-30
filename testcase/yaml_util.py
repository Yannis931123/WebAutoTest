import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        '''
        通过init把文件传入到这个类
        :param yaml_file:
        '''
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        '''
        读取yaml，将yaml反序列化，就是把我们yaml格式转换成dict格式
        :return:
        '''
        try:
            with open(self.yaml_file, encoding="utf-8") as f:
                value = yaml.load(f,
                                  Loader=yaml.FullLoader)  # 文件流，加载方式 #推荐使用 FullLoader 作为默认的加载器，因为它提供了完整的 YAML 功能，同时避免了安全风险
                print(value)
                return value  # 返回解析后的值
        except FileNotFoundError:
            print(f"文件 {self.yaml_file} 未找到。")
        except yaml.YAMLError as e:
            print(f"YAML 解析错误: {e}")
        except Exception as e:
            print(f"发生未知错误: {e}")
        return None  # 如果发生错误，返回 None


if __name__ == '__main__':
    util = YamlUtil("../data/interface.yaml")
    data = util.read_yaml()  # 尝试读取 YAML 文件，并获取解析后的数据
    if data is not None:
        # 在这里处理 data，例如打印或进行其他操作
        pass
    else:
        print("未能成功解析 YAML 文件。")
