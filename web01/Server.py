#coding=utf-8
from wsgiref.simple_server import make_server
from web01.hello import application

#创建服务，端口8080 处理函数 application:
httpd = make_server('', 8080, application)
print('Server http on port 8080 ......')
#监听http请求:
httpd.serve_forever()
