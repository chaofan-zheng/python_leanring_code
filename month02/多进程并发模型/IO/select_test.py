"""
IO 多路复用演示
"""
from socket import *
from select import *

file = open("mylog.txt")

udp_sock = socket(AF_INET, SOCK_DGRAM)

tcp_sock = socket()
tcp_sock.bind(("0.0.0.0", 8889))
tcp_sock.listen(5)

print("开始监控")
# rs, ws, xs = select([tcp_sock,udp_sock], [], [])
rs, ws, xs = select([], [tcp_sock,udp_sock], [])

print("rlist:", rs)
print("wlist:", ws)
print("xlist:", xs)
