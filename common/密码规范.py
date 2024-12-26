"""
Courier
New字体，23
磅行间距
"""
import re


def check_password(password):
    if not 6 <= len(password) <= 20:
        return False, "密码必须在6~20之间"
    if not re.findall(r"[a-z]", password):
        return False, "密码必须包含至少1个小写字母"
    if not re.findall(r"[A-Z]", password):
        return False, "密码必须包含至少一个大写字母"
    if not re.findall(r"[0-9]", password):
        return False, "密码必须包含至少一个数字"
    if not re.findall(r"[^0-9a-zA-Z]", password):
        return False, "必须包含至少1个特殊字符"
    return True, None
