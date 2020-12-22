"""
获取http响应和请求
"""
from socket import *

s = socket()
s.bind(("0.0.0.0", 8888))
s.listen(5)

c, addr = s.accept()
print("Connect from ", addr)
data = c.recv(1024 * 10)
print(data.decode())

# response = """HTTP/1.1 200 OK
# Content-Type:text/html
#
# Hello MotherF***** What's my name
# """
# 等同于
response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:text/html\r\n"
response += "\r\n"
response += "Hello MotherF***** What's my name"
c.send(response.encode())

c.close()
s.close()

# 在浏览器中输入127.0.0.1:8888
# Connect from  ('127.0.0.1', 55982)
# GET / HTTP/1.1
# Host: 127.0.0.1:8888
# Upgrade-Insecure-Requests: 1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15
# Accept-Language: zh-cn
# Accept-Encoding: gzip, deflate
# Connection: keep-alive


# 在浏览器中输入127.0.0.1:8888/abc.html
# Connect from  ('127.0.0.1', 55694)
# GET /abc.html HTTP/1.1
# Host: 127.0.0.1:8888
# Upgrade-Insecure-Requests: 1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15
# Accept-Language: zh-cn
# Accept-Encoding: gzip, deflate
# Connection: keep-alive

# 写完HTTP响应之后，在浏览器中输入127.0.0.1:8888
# 浏览器中会显示 hello world
