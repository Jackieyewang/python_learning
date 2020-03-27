import socket
import threading


class Client(object):
    """客户端"""

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.Address = ("127.0.0.1",9090)
        self.client_socket.bind(self.Address)
        self.server_Address = ("127.0.0.1",7890)

    def ConnectionServer(self):
        print(self.client_socket)
        self.client_socket.connect(self.server_Address)
        print("连接成功！")
        t1 = threading.Thread(target=self.SendMsg)
        t2 = threading.Thread(target=self.RecvMsg)
        t1.start()
        t2.start()


    def RecvMsg(self):
        while True:
            recvstr = self.client_socket.recv(1024)
            print("接收到来自服务器的消息维为：%s" % recvstr.decode("utf-8"))

    def SendMsg(self):
        while True:
            sendstr = input("请输入你要发送的消息：")
            self.client_socket.send(sendstr.encode("utf-8"))

def main():
    """测试函数"""
    C = Client()
    C.ConnectionServer()
    

if __name__ == '__main__':
    main()
