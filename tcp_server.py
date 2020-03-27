import threading
import socket


class Server(object):
    """服务端"""

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.Address = ("127.0.0.1",7890)
        self.server_socket.bind(self.Address)
        self.server_socket.listen(128)
        self.clientsocket = dict()
        self.count = 0
        self.isrunning = dict()

    def WaitClient(self):
        while True:
            print("正在等待客户端的连接......")
            clientsocket,clientAddresss = self.server_socket.accept()
            print("%s已经连接成功！" % str(clientAddresss))
            # print(clientsocket,clientAddresss)
            self.count += 1
            self.clientsocket[clientAddresss] = clientsocket
            print("当前客户端连接个数为：%d" % self.clientsocket.__len__())
            self.isrunning[self.count]=True
            print("集合中的元素为:%s" % str(self.isrunning.__len__()))
            t = threading.Thread(target=self.RecvMsg,args = (clientsocket,clientAddresss,self.isrunning,self.count))
            t1 = threading.Thread(target=self.SendMsg,args=(clientsocket,clientAddresss,self.isrunning,self.count))
            t.start()
            t1.start()

    def RecvMsg(self,client,clientaddress,isrun,count):
        if isrun[count] is True:
            while True:
                try:
                    recvmsg = client.recv(1024)
                    print("来自%s的消息为：%s" % (str(clientaddress),recvmsg.decode("utf-8")))
                except Exception as ret:
                    print("客户端%s已经离去！" % str(clientaddress))
                    client.close()
                    isrun[count] = False
                    self.clientsocket.pop(clientaddress)
                    break
        else:
            return

    def SendMsg(self,client,clientAddresss,isrun,count):
            while True:
                sendstr = input("请输入你要发送的消息:")
                if isrun[count] is True: # 先判断该客户端是否还在
                    if client:
                        client.send(sendstr.encode("utf-8"))
                    else:
                        isrun.pop(count)
                        return



def main():
    """测试函数"""
    S = Server()
    S.WaitClient()

if __name__ == '__main__':
    main()