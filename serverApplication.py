#!/usr/local/bin/python3
#-*- coding:utf-8 -*-

import json
from urllib.parse import parse_qs


def isString(b):
    length = len(b)
    # 当字符串是被双引号括起来时，才认为是str类型，故长度小于3时，要么没有被双引号括起来，要么括起来的字符串为空
    if length < 3:
        return False

    elif b[0] == '"' and b[length - 1] == '"':
        return True

    else:
        return False


def application(environ, start_response):
    #发送HTTP响应码和HTTP Header
    start_response("200 OK", [("Content-Type", "text/html")])

    try:
        # 获取请求URL中提交方法
        method = environ["REQUEST_METHOD"]
        #获取请求URL中的参数，并分离参数
        params = parse_qs(environ['QUERY_STRING'])

    except:
        #若无法获取URL中的路径、提交方法、提交参数，返回系统错误
        result = {"err_code": 11, "err_msg": "system error"}
        return [json.dumps(result).encode("utf-8")]

    # 若路径不是默认路径 或 提交方法不是GET 则返回系统错误
    if method != "GET":
        result = {"err_code": 11, "err_msg": "system error"}
        return [json.dumps(result).encode("utf-8")]

    # 若仅有2个参数，并且参数名分别为a、b，那么进一步判断参数值的类型是否正确
    if len(params) == 2 and 'a' in params and 'b' in params:
        valueA = params.get('a', [''])[0]
        valueB = params.get('b', [''])[0]

        # a的值为int类型（不考虑负数的情况），并且b的值为str类型，那么返回success; 若a 或 b为空，则isdigit()和isString()都会返回False
        if valueA.isdigit() and isString(valueB):
            valueB = valueB[1:-1]
            refenence = "No." + valueA + " is " + valueB
            result = {"err_code": 0, "err_msg": "success", "refenence": refenence}
            return [json.dumps(result).encode("utf-8")]

        # 否则返回参数错误
        else:
            result = {"err_code": 21, "err_msg": "empry or wrong params"}
            return [json.dumps(result).encode("utf-8")]

    #若参数不是有且仅有a和b，则返回参数错误
    else:
        result = {"err_code": 21, "err_msg": "empry or wrong params"}
        return [json.dumps(result).encode("utf-8")]





