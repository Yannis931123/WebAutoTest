import unittest
from ddt import ddt, data
from base.base_util import BasUtil


# DDT中的装饰器
# @ddt：装饰类，作用是用于申明当前类使用ddt数据驱动
# @data： 装饰函数，作用是给函数传值
# @unpack：装饰函数，作用是数据解包
# @file_data：装饰函数，作用是直接读yaml、json文件