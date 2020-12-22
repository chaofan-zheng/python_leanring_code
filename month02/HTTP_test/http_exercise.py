"""
使用http协议，将一个文件的内容作为响应体发送给浏览器显示
（文本可以是文本也可以是图片）
Content-Type:image/jpeg
"""
from socket import *

tcp_socket = socket()
tcp_socket.bind(("0.0.0.0", 9999))
tcp_socket.listen(5)
connfd, addr = tcp_socket.accept()

print("Connect from ", addr)
data = connfd.recv(1024 * 10)
print(data.decode())

file = open("../多进程并发模型/ftp_file_server/dic01/timg.jpg", "rb")
content = file.read()
msg = "HTTP/1.1 200 OK\r\n"
msg += "Content-Type:image/jpeg\r\n"
msg += "\r\n"
# msg += f"{content}"
msg = msg.encode() + content
# connfd.send(msg.encode())
connfd.send(msg)
file.close()
connfd.close()
tcp_socket.close()
