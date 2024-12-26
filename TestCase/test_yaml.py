import pytest
import os
from TestCase.yaml_util import yamlUtil


class Test_yaml():

    @pytest.mark.parametrize("args", yamlUtil("../data/interface.yaml").read_yaml())
    def test_yaml(self, args):
        print(args)
        interfaceName = args['interfaceName']
        url = args["url"]
        headers = args["headers"]

        # assert 2 == args["data"]["type"]
