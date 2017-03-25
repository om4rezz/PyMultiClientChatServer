#!/usr/bin/python3

import socket
import threading

def Main():
    host = '127.0.0.1'
    port = 4001

    mySocket = socket.socket()
    mySocket.connect((host, port))

    name = input("Provide your name, please -> ")

    mySocket.send(name.encode())

    # start sending and receiving
    objSender = Sender(mySocket, name)
    objReceiver = Receiver(mySocket, name)

    objSender.start()
    objReceiver.start()

class Sender(threading.Thread):
    '''the main sender as a thread'''

    message = ''

    def __init__(self, socket, name):
        threading.Thread.__init__(self)
        self.socket = socket
        self.name = name

    def run(self):
        while self.message != 'q!':
            # mySocket.send(message.encode())

            message = input(self.name + " -> ")

            self.socket.send(message.encode())

            # data = mySocket.recv(1024).decode()

            # print('Received from server: ' + data)
        self.socket.close()


class Receiver(threading.Thread):
    '''the main char receiver as a thread'''

    def __init__(self, socket, name):
        threading.Thread.__init__(self)
        self.socket = socket
        self.name = name

    def run(self):
        while 1==1:
            # mySocket.send(message.encode())

            # message = input(" -> ")

            # mySocket.send(message.encode())

            data = self.socket.recv(1024).decode()
            print(len(data))
            strData = str(data)
            print(data + "\n" + self.name + " -> ", end = '')





if __name__ == '__main__':
    Main()