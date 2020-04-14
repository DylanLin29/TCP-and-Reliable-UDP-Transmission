import ipaddress
import socket
from socket import AF_INET, SOCK_STREAM

ipaddress.ip_address('127.0.0.123')

clientSocket = socket.socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.123', 1234))