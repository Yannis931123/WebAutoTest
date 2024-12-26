import os.path
import time
import datetime
import allure

import messageSimulator
from datetime import timedelta
from tools import times

SYSTEM_NAME = "新担保品"
FEATURE_NAME = "常备借贷便利流程"
TESTER_NAME = "颜行"
TESTCASE_NAME = "质押"
IDs = "000"
env = EnvMember().env
xdbpglxt = XDBPGLXT()
yjywpt = YJYWPT()
qsyw = QSYW()
htcx = HTCX()
zlcx = ZLCX()
cbjdbllc = readtestdata_02_fomula(os.path.join(XDBPGLXT_EXCEL_DIR, f"担保品新一代——常备借贷便利(模拟器)_{env}.xlsx"),
                                  "常备借贷便利流程")
zjcs = readtestdata_02_fomula(os.path.join(XDBPGLXT_EXCEL_DIR, f"担保品新一代——常备借贷便利(模拟器)_{env}.xlsx"),
                              "中间参数")
qwjg = readtestdata_02_fomula(os.path.join(XDBPGLXT_EXCEL_DIR, f"担保品新一代——常备借贷便利(模拟器)_{env}.xlsx"),
                              "期望结果")
rgzh = readtestdata_02_fomula(os.path.join(XDBPGLXT_EXCEL_DIR, f"担保品新一代——常备借贷便利(模拟器)_{env}.xlsx"),
                              "人工置换")


def test_cbjdbllc_zy(ucfconn2, ucfconn2_menu, ucfconn1, ucfconn1_menu, ucfconn_I_1, ucfconn_I_1_menu, ucfconn_I_3,
                     ucfconn_I_3_menu, cbjdbllc, zjcs, qwjg, rgzh, env_setting):
    cbjdbllc["首期到期日"] = datetime.datetime.now().strftime('%￥%m%d')
    cbjdbllc["到期交割日"] = (datetime.datetime.now() + timedelta(days=1)).strftime('%￥%m%d')
    cbjdbllc["业务标识号"] = "CBJDBL" + times.datetime_strftime(fmt='%￥%m%d%f')
    ywbsh = cbjdbllc["业务识别号"]
    resobj = [cbjdbllc["业务识别号"], cbjdbllc["首期交割日"], cbjdbllc["到期交割日"]]
    write_resultlist_by_xh(os.path.join(XDBPGLXT_EXCEL_DIR, f"担保品新一代——常备借贷便利(模拟器)_{env}.xlsx"),
                           "常备借贷便利流程", int(cbjdbllc["序号"]) + 1, 14, resobj)

    with allure.step("1.新担保品管理系统-签约账号管理-发令方签约"):
        xdbpDriver = ucfconn2.ucfmainmenu1(ucfconn2_menu, "担保品管理系统（新）", "3")

    with allure.step("7 前后台接口录入常备借贷便利指令"):
        msgUrl = env_setting["msgUrl"]
        scjsje = cbjdbllc["首期结算金额（元）"]
        dqjsje = cbjdbllc["到期结算金额（元）"]
        cjr = times.timeToStamp(times.get_day(times.date_str_to_str(cbjdbllc["首期交割日"]), num=1) + "00:00:00")
        sjsj = times.timeToStamp(times.get_day(times.date_str_to_str(cbjdbllc["首期交割日"]), num=1) + "00:00:00")
        scjgr = times.timeToStamp(times.get_day(times.date_str_to_str(cbjdbllc["首期交割日"]), num=1) + "00:00:00")
        dqjgr = times.timeToStamp(times.get_day(times.date_str_to_str(cbjdbllc["首期交割日"]), num=1) + "00:00:00")
        zllrData = data_util.assembleData(ywbsh=ywbsh, cjr=cjr, jrjgtgzh=cbjdbllc["出质方债券托管账号"],
                                          rmyhtgzh=cbjdbllc["质权方债券托管账号"], scjsje=scjsje, dqjsje=dqjsje,
                                          scjgr=scjgr, dqjgr=dqjgr, ll=cbjdbllc["融资利率（%）"])
        messageSimulator.zllr_cbjdbl(zllrData, msgUrl)

    with allure.step("7.1报文查询 （报文模拟器）"):
        msgList = messageSimulator.message_search_common({"yewlb": "6-9", "url": msgUrl})
    with allure.step("7.2 报文发送（报文模拟器）"):
        messageSimulator.message_send(msgUrl, msgList, ywbsh, "", ywlb="6-9")

    with allure.step("8 登录客户端 > 清算系统 > 指令确认"):
        time.sleep(3)
        qsDriver = ucfconn_I_1.ucfmainmenu1(ucfconn_I_1_menu, "清算业务", "4")
        params = data_util.assembleData(zh=cbjdbllc["出质方债券托管账号"], ywbsh=ywbsh, ywlb="常备借贷便利")
        expect = data_util.assembleData(tknr="确认成功")
        qsyw.handle_thirdzlqr_dbp(qsDriver, params, expect)
        ucfconn_I_1.menu_tab_close()
