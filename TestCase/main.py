import pytest
import subprocess

if __name__ == '__main__':
    pytest.main(['-vs', 'test_example.py', "--alluredir=allure_file"])
    # subprocess.call('allure serve allure_file', shell=True)  # 收集的数据加载到报告中
    subprocess.call('allure generate allure_file -o allure_report --clean', shell=True)
    subprocess.call('allure open allure_report', shell=True)

    # # 定义Allure结果文件的输出目录
    # allure_results_dir = './allure_results'
    # # 定义Allure报告的输出目录
    # allure_report_dir = './allure_report'
    # # 确保Allure结果文件的输出目录存在
    # if not os.path.exists(allure_results_dir):
    #     os.makedirs(allure_results_dir)
    #
    # # 构建Allure生成报告的命令
    # allure_generate_command = f'allure generate {allure_results_dir} -o {allure_report_dir} --clean'
    # try:
    #     # 调用命令行执行Allure生成报告的命令
    #     subprocess.check_call(allure_generate_command, shell=True)
    #     print("Allure报告生成成功！")
    #
    #     # 构建打开Allure报告的命令
    #     allure_open_command = f'allure open {allure_report_dir}'
    #     # 调用命令行执行打开Allure报告的命令
    #     subprocess.Popen(allure_open_command, shell=True)
    # except subprocess.Called2567Error:
    #     print("Allure报告生成失败！")

# if __name__ == '__main__':
#     os.system(r"allure generate -c -o  allure_results")
#     os.system(r"allure serve allure_results")


# if __name__ == '__main__':
#     pytest.main(['-vs', "--alluredir=allure_file", "test_login.py"])
#     subprocess.call('allure generate allure_file -o allure_report --clean', shell=True)
#     subprocess.call('allure open allure_report', shell=True)

# 执行前删除allure_file
# pytest -v --alluredir=allure_file 或者 pytest  test_login.py -v --alluredir=allure_file
# allure generate allure_file -o allure_report --clean
# allure open allure_report 或者 allure serve allure_file
