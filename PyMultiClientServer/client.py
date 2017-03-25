#!/usr/bin/python3

import socket
import threading

class Client(threading.Thread):
    '''This is the core class of the client'''

    def __init__(self, uid, name, socket):
        threading.Thread.__init__(self)
        self.uid = uid
        self.name = name
        self.socket = socket

    def get_socket(self):
        return self.socket

    def get_name(self):
        return self.name

    def get_uid(self):
        return self.uid

    def run(self):
        while True:
            data = self.socket.recv(1024).decode()
            # if not data:
            #     break
            print("from connected user: " + str(data))

            # data = str(data).upper()
            # print("sending: " + str(data))
            # conn.send(data.encode())
            if data == 'q!':
                self.socket.close()
                break