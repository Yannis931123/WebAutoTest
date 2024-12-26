import allure
import requests
from py import log
from tools import time

# 定义最大重试次数
max_retry = 3

# 初始的 ywbsh
ywbsh = get_initial_ywbsh()

# 7.1 报文查询
retry_count = 0
msgList = None

while retry_count < max_retry:
    with allure.step(f"7.1 报文查询（报文模拟器），重试次数：{retry_count + 1}"):
        msgList = messageSimulator.message_search_common({"yewlb": "6-9", "url": msgUrl, "ywbsh": ywbsh})

    if msgList:
        # 如果成功获取到报文，退出循环
        break

    retry_count += 1
    log.info(f"未成功获取报文，进行第 {retry_count} 次重试")

    # 更新 ywbsh，可以根据实际需求重新获取
    ywbsh = get_new_ywbsh()

if not msgList:
    log.error("无法获取报文，重试次数已用尽")
else:
    # 7.2 报文发送
    with allure.step("7.2 报文发送（报文模拟器）"):
        messageSimulator.message_send(msgUrl, msgList, ywbsh, "", ywlb="6-9")

# 8 登录客户端 > 清算系统 > 指令确认
with allure.step("8 登录客户端 > 清算系统 > 指令确认"):
    time.sleep(3)
    qsDriver = ucfconn_I_1.ucfmainmenu1(ucfconn_I_1_menu, "清算业务", "4")
    params = data_util.assembleData(zh=cbjdbllc["出质方债券托管账号"], ywbsh=ywbsh, ywlb="常备借贷便利")
    expect = data_util.assembleData(tknr="确认成功")
    qsyw.handle_thirdzlqr_dbp(qsDriver, params, expect)
    ucfconn_I_1.menu_tab_close()

# 其他测试步骤...
