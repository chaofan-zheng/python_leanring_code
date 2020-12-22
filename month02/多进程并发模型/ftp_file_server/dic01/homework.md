- SERVER

  ```python
  """
  ftp文件服务器
  重要代码
  1。分为服务端和客户端，要求可以有多个客户端同时操作
  2。客户端可以查看服务器中有什么文件
  3。客户端可以从文件库中下载文件到本地 文件存在，文件不存在
  4。客户端可以上传一个本地文件到文件库 文件已经存在
  5。使用print在客户端打印命令输入提示
  
  所以如果请求是一种协议的话，
  响应也是一种协议
  响应码（HTTP协议也有这种响应码）
  """
  
  from socket import *
  from multiprocessing import Process
  import os
  from time import *
  
  
  # 具体处理客户端事务
  class Handle:
      def __init__(self, connfd):
          self.connfd = connfd
          self.files_list = os.listdir("dic01")
  
      def request(self, command, content):
          if command == "SH":
              self.show_files()
          elif command == "DL":
              self.download_files(content)
          elif command == "UP":
              pass
          elif command == "Q":
              pass
  
      def show_files(self):
          if self.files_list:
              for filename in self.files_list:
                  self.connfd.send(f"\n{filename}".encode())
              sleep(0.1)
              self.connfd.send(b"##")
          else:
              msg = "文件列表为空"
              self.connfd.send(msg.encode())
          # 留意沾包的情况
  
      def download_files(self, content):  # filename需要是utf8
          filename = content
          if filename in self.files_list:
              self.connfd.send("1".encode())  # 1代表成功
              file = open(f"dic01/{filename}", "rb")
              while True:
                  msg = file.read(1024*1024)  # msg是二进制码
                  if not msg:
                      sleep(0.1)  # 下面不sleep的话，会欠在缓存区里面
                      self.connfd.send(b"##")
                      break
                  else:
                      self.connfd.send(msg)
                      sleep(0.05)
  
  
  
          else:
              self.connfd.send("0".encode())  # 0代表失败
  
  
  # 为多个客户端创建多进程
  class ClientProcess(Process):
      def __init__(self, connfd):
          super().__init__(daemon=True)
          self.connfd = connfd
          self.handle = Handle(connfd)
  
      def run(self):
          while True:
              data = self.connfd.recv(1024)
              command = data.decode().split("_MYNCP_")[0]  # 通信协议
              content = data.decode().split("_MYNCP_")[1]
              self.handle.request(command, content)
  
  
  # 并发服务类
  class ConcurrentServer:
      def __init__(self, host="", port=0):
          self.host = host
          self.port = port
          self.addr = (self.host, self.port)
          self.sock = self.create_socket()
  
      def create_socket(self):
          tcp_socket = socket()
          tcp_socket.bind(self.addr)
          return tcp_socket
  
      def server_forever(self):
          print("Listen the port %d" % self.port)
          self.sock.listen(5)
          while True:
              connfd, addr = self.sock.accept()
              print("Connect from ", addr)
              process = ClientProcess(connfd)
              process.start()
  
  
  if __name__ == '__main__':
      server = ConcurrentServer("0.0.0.0", 6955)
      server.server_forever()
  ```

* CLIENT

  ```python
  from socket import *
  import os
  
  class FTPView:
      def __init__(self):
          self.__ftp = FTPHandle()
  
      def display_menu(self):
          print("1) 查看文件")
          print("2) 下载文件")
          print("3) 上传文件")
          print("4) 退出网盘")
  
      def select_menu(self):
          while True:
              choice = input(">>")
              if choice == "1":
                  self.__ftp.show_files()
              elif choice == "2":
                  self.__ftp.download_file()
              elif choice == "3":
                  pass
              elif choice == "3":
                  pass
              else:
                  print("输入指令有误，请重新输入")
                  continue
  
      # 入口程序启动方法
      def main(self):
          while True:
              self.display_menu()
              self.select_menu()
  
  
  class FTPHandle:
      SERVERADDR = ("127.0.0.1", 6955)
  
      def __init__(self):
          self.sock = self.connect_socket()
  
      def connect_socket(self):
          tcp_socket = socket()
          tcp_socket.connect(FTPHandle.SERVERADDR)
          return tcp_socket
  
      def show_files(self):
          msg = "SH_MYNCP_  "  # 加空格防止报错 split后索引超出范畴
          self.sock.send(msg.encode())
          while True:
              data = self.sock.recv(1024)
              if data == b"##":
                  break
              elif data.decode() == "文件列表为空":
                  print(data.decode())
                  break
              print(data.decode())
  
      def download_file(self):
          while True:
              filename = input("请输入你要下载的文件名")
              path = input("请输入你的下载路径(以当前文件夹为起点）")  # ./download 当前为.
              # 判断要下载的文件是不是已经在目录里了 同时判断文件路径是不是写错了
              try:
                  filelist = os.listdir(f"{path}")
              except Exception:
                  print("路径错误")
                  continue
              if filename in filelist:
                  print("该文件已经存在")
                  continue
              else:
                  new_file = open(f"{path}/{filename}", "wb")
                  name_message = "DL_MYNCP_" + filename
                  self.sock.send(name_message.encode())
                  data = self.sock.recv(1024)
                  if data.decode() == "0":
                      print("该文件不存在")
                  else:
                      while True:
                          data = self.sock.recv(1024*1024)
                          if data == b"##":
                              print("下载完成")
                              break
                          else:
                              new_file.write(data)
              break
  
  
  if __name__ == '__main__':
      view = FTPView()
      view.main()
  
  ```

  

