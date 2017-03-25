#!/usr/bin/python3

import socket
import threading

class Client(threading.Thread):
    '''This is the core class of the client'''

    client_list = []

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

    def push_to_client(_sender, name, msg):
        for c in Client.client_list:
            if name == c.get_name():
                c.get_socket().send((_sender + " -> " + msg).encode())
                return 1
        return -1

    def run(self):

        self.name = self.socket.recv(1024).decode()

        while True:
            data = self.socket.recv(1024).decode()
            if not data:
                break

            data_list = str(data).split(' ', 1)

            Client.push_to_client(self.name, data_list[0], data_list[1])

            print("from %s: %s" % (self.name, str(data)))

            # data = str(data).upper()
            # print("sending: " + str(data))
            # conn.send(data.encode())
            if data == 'q!':
                self.socket.close()
                break