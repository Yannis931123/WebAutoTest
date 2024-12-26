import requests
from py import log
from tools import times


def message_send(url, data, ywbsh, cookie, ywlb=None):
    """报文报送 :param data: :param ywbsh: :return:"""
    if ywlb is None:
        ywlb = "4"
    reqData = ""
    if data != None and len(data) > 0:
        for item in data:
            id = item["id"]
            dataList = item["new"].split(",")
            ywzl = dataList[0]  # 业务种类
            resYwbsh = dataList[1]
            bwnr = dataList[2]
            fqfzh = dataList[3]
            sqfzh = dataList[4]
            lrsj = times.get_current_timeStamp()
            if dataList[1]=ywbsh:
                reqData += f"""<r id={id} state="modifiy"><o><v s="6"></v></o><n><v>{ywzl}</v><v>{resYwbsh}</v><v>{bwnr}</v><v>{fqfzh}</v><v>{sqfzh}</v><v>{lrsj}</v><v>true</v></n></r>
                """
            else:
                reqData += f"""<r id={id}><n><v>{ywzl}</v><v>{resYwbsh}</v><v>{bwnr}</v><v>{fqfzh}</v><v>{sqfzh}</v><v>{lrsj}</v><v></r>
                """
    payLoad = {
        "__type": "updateData",
        "__viewInstanceId": "com.cdc.cfets.view.MessageSend~com.cdc.cfets.view.model.MessageSendViewModel",
        "__xml": f""""""
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "cookie": cookie
    }
    sendRes = requests.post(url=url, data=payLoad)
    sendTxt = sendRes.textl
    log.info(f"3.发送报文返回结果：{sendTxt}")
    print("3.发送报文：===========", sendRes.text)
    if '<result succeed="true">' in sendRes.text:
        log.info(f"3.发送报文返回状态：========{sendRes.status_code}")
    else:
        log.info("3.发送报文：========出现问题")
