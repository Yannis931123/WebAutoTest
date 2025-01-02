"""
conftest.py层级作用域
conftest.py在项目根目录下，则项目下的所有测试用例，均可使用conftest.py中定义的fixture。
即项目根目录下的conftest.py，作用域是整个项目.
conftest.py在子目录下，则该目录下的测试用例，均可使用conftest.py中定义的fixture。
即子目录下的conftest.py，作用域是子目录及其子目录下的所有测试用例。

测试用例在执行时，调用fixture的顺序，按 就近原则 调用
测试用例文件中的fixture > 当前目录中的fixture > 上级目录中的fixture > 根目录中的fixture
"""
