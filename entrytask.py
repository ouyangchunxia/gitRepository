#!/usr/local/bin/python3
#-*- coding:utf-8 -*-

from wsgiref.simple_server import make_server
from serverApplication import application

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8080
    #创建一个服务器，ip为本地IP，port为8080
    httpd = make_server(host, port, application)

    print("serving http on port {0}...".format(str(port)))

    #开始监听HTTP请求
    httpd.serve_forever()