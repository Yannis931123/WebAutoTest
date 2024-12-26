from functools import wraps
import unittest

testCaseName = {}
class decRelation:
    """
    :name:被依赖的用例名称
    :depend:依赖的用例名称
    =======example=======
    @decRelation(name='test_01')
    def test_01(self):
        self.assertEqual(2, 2)

    @decRelation(depend='test_01')
    def test_02(self):
        self.assertEqual(1, 2)
    """
    def __init__(self, name=None, depend=None):
        self.depend = depend
        self.name = name
        super(decRelation, self).__init__()

    def __call__(self, func):
        @wraps(func)
        def decoration(*args, **kwargs):
            try:
                if self.name:
                    if self.depend and testCaseName[self.depend] is True:
                        func(*args, **kwargs)
                        testCaseName[self.name] = True
                    elif self.depend is None:
                        func(*args, **kwargs)
                        testCaseName[self.name] = True
                if self.depend and testCaseName[self.depend] is not True:
                    unittest.TestCase().skipTest(reason="%s 测试用例执行失败，相关依赖用例跳过!!!" % (self.depend))
                    testCaseName[func.__name__] = 'Skip'
                else:
                    result = func(*args, **kwargs)
                    testCaseName[func.__name__] = True
                    return result
            except Exception as e:
                if self.name and self.name not in testCaseName.keys():
                    testCaseName[self.name] = False
                if self.depend and self.depend not in testCaseName.keys():
                    testCaseName[self.depend] = False
                raise e
        return decoration

