#!/usr/bin/python3

import socket
from client import Client

def Main():
    host = "127.0.0.1"
    port = 4001

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(10)

    while(1==1): # accept infinite number of clients

        soc, addr = mySocket.accept()
        print("Connection from: " + str(addr))

        client = Client(len(Client.client_list), "", soc)

        client.start()

        Client.client_list.append(client)

        print("Number of connected clients: %d" % len(Client.client_list))

        for client in Client.client_list:
            print("Client UID: " + str(client.get_uid()))
            print("Client name: " + str(client.get_name()))

if __name__ == '__main__':
    Main()


    # while True:
        #     data = conn.recv(1024).decode()
        #     if not data:
        #         break
        #     print("from connected  user: " + str(data))
        #
        #     data = str(data).upper()
        #     print("sending: " + str(data))
        #     conn.send(data.encode())
        #
        # conn.close()