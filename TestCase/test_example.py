import allure


# 定义一个测试函数，使用 allure 的 feature 来标记测试的特性
@allure.feature("加法运算测试")
class TestAddition:
    # 使用 allure 的 story 来标记具体的测试场景
    @allure.story("测试两个正数相加")
    def test_add_positive_numbers(self):
        # 一个简单的断言
        assert 3 + 4 == 7

    # 使用 pytest 的 parametrize 来实现参数化测试 @pytest.mark.parametrize("x,y,expected", [(1, 2, 3), (3, 4, 7)])
    @allure.story("测试加法的参数化场景")
    def test_add_with_parameters(self, x, y, expected):
        # 参数化测试的断言
        assert x + y == expected


# 使用 allure 的 step 来记录测试步骤
@allure.step("执行加法操作")
def add_and_print_result(x, y):
    result = x + y
    print(f"The result of {x} + {y} is {result}")
    return result


# 测试用例中使用 allure step
def test_add_step():
    with allure.step("步骤1：输入两个参数"):
        x = 2
        y = 3

    result = add_and_print_result(x, y)
    with allure.step("步骤2：验证结果"):
        assert result == 5
