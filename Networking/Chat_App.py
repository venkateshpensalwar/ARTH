import socket as soc
import os 
import threading

## your ip 
SenderIP = input("Enter Sender IP address: ")
SenderPort = int(input("Enter Sender port: "))

## Friends ip
ReciverIP = input("Enter Reciver IP address: ")
ReciverPort = int(input("Enter Reciver port: "))


## Creating UDP Socket
ReadySocket = soc.socket(soc.AF_INET,soc.SOCK_DGRAM)

## only for Reciving messages
ReadySocket.bind((SenderIP,SenderPort))

def SendMsg():
        while True:
                Message = input('Enter Message: ')
                if(Message == 'quite' or Message == 'bye' or Message == 'exit'):    
                       Message = 'Your Friend is offline'    
                       ReadySocket.sendto(Message.encode(),(ReciverIP,ReciverPort))
                       os._exit(1)
                else:
                     ReadySocket.sendto(Message.encode(),(ReciverIP,ReciverPort))


def RecvMsg():
        while True:
                Msg = ReadySocket.recvfrom(100)
                print(Msg[0].decode())


SendMsg()
RecvMsg()


