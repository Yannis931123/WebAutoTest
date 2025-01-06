"""
1.安装JDK 放到路径中 将bin目录加到环境变量
2.安装allure 放到路径中 将bin目录加到环境变量
3.安装allure-pytest
# 1. java验证 ：java --version # 2. python验证 ：python -V # 3. allure验证：allure --version # 4. pytest验证：pip show pytest
"""

"""
函数	说明	备注
@allure.epic()	敏捷中的概念	项目名称
@allure.feature()	模块名称	模块名
@allure.story()	用户故事	子模块
@allure.title(用例的标题)	用例标题	用例标题
@allure.severity()	用例等级	包括：blocker，critical，normal，minor，trivial
@allure.step()	操作步骤	测试步骤
@allure.description()	测试用例描述	可以写预期结果
@allure.testcase(url)	测试用例链接	链接到测试用例系统
@allure.issue(url)	测试bug链接	链接到bug系统
@allure.link(url)	链接	一般可以链接到被测系统地址
@allure.attachment()	附件	一般可以添加截图或者日志
"""

"""
定制报告
Feature: 标注主要功能模块
Story: 标注Features功能模块下的分支功能
Severity: 标注测试用例的重要级别
Step: 标注测试用例的重要步骤
Issue和TestCase: 标注Issue、Case，可加入URL
"""

import allure
import pytest

"""1、Features定制详解"""


@allure.feature('test_module_01')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0


@allure.feature('test_module_02')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])

"""2、Story定制详解"""


@allure.feature('test_module_01')
@allure.story('test_story_01')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0


@allure.feature('test_module_01')
@allure.story('test_story_02')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])

"""3、用例标题和用例描述定制详解"""


@allure.feature('test_module_01')
@allure.story('test_story_01')
# test_case_01为用例title
def test_case_01():
    """
    用例描述：这是用例描述，Test case 01，描述本人
    """
    # 注释为用例描述
    assert 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])

# 4、Severity定制详解
"""
4、Severity定制详解
Allure中对严重级别的定义：
1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
2、 Critical级别：临界缺陷（ 功能点缺失）
3、 Normal级别：普通缺陷（数值计算错误）
4、 Minor级别：次要缺陷（界面错误与UI需求不符）
5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
"""


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
def test_case_01():
    """
    用例描述：Test case 01
    """
    assert 0


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('critical')
def test_case_02():
    """
    用例描述：Test case 02
    """
    assert 0 == 0


@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('normal')
def test_case_03():
    """
    用例描述：Test case 03
    """
    assert 0


@allure.feature('test_module_01')
@allure.story('test_story_02')
@allure.severity('minor')
def test_case_04():
    """
    用例描述：Test case 04
    """
    assert 0 == 0


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])

"""5、Step定制详解"""


@allure.step("字符串相加：{0}，{1}")
# 测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])

"""6、Issue和TestCase定制详解"""


@allure.step("字符串相加：{0}，{1}")  # 测试步骤，可通过format机制自动获取函数参数
def str_add(str1, str2):
    print('hello')
    if not isinstance(str1, str):
        return "%s is not a string" % str1
    if not isinstance(str2, str):
        return "%s is not a string" % str2
    return str1 + str2


@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('blocker')
@allure.issue("http://www.baidu.com")
@allure.testcase("http://www.testlink.com")
def test_case():
    str1 = 'hello'
    str2 = 'world'
    assert str_add(str1, str2) == 'helloworld'


if __name__ == '__main__':
    pytest.main(['-s', '-q', '--alluredir', './report/xml'])

"""
7、attach定制详解
在报告中增加附件：allure.attach(’arg1’,’arg2’,’arg3’)：
arg1：是在报告中显示的附件名称
arg2：表示添加附件的内容
arg3：表示添加的类型(支持:HTML,JPG,PNG,JSON,OTHER,TEXTXML)
"""
file = open('../test.png', 'rb').read()
allure.attach('test_img', file, allure.attach_type.PNG)
