import unittest
import socket
from socket import AF_INET, SOCK_STREAM
from unittest.mock import Mock, patch
import io
import sys
from TCPServer import *

def listen(param0, number):
    pass

def bind(param0, serverName, serverPort):
    pass

def recv(param0, size):
    return 'ls'.encode()

def send(parm0, message):
    pass

class TestTCPServer(unittest.TestCase):
    def setUp(self):
        self.connectionSocket = socket.socket(AF_INET, SOCK_STREAM)

    def tearDown(self):
        self.connectionSocket.close()
    
    # @patch.object(socket.socket, '')
    @patch.object(socket.socket, 'recv', recv)
    @patch.object(socket.socket, 'send', send)
    def test_successfully_transimission(self):
        self.assertEqual(receive_and_send_success(connectionSocket=self.connectionSocket), True)

if __name__ == '__main__':
    unittest.main()
