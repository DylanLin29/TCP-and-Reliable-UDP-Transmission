import socket
from socket import AF_INET, SOCK_STREAM
import ipaddress

def serverPort_is_valid(serverPort):
    if (not serverPort.isdigit()) or int(serverPort) > 65535 or int(serverPort) < 0:
        return False
    return True

def server_is_valid(serverName, serverPort):
    try:
        ipaddress.ip_address(serverName)
    except ValueError:
        return False
    # actual test to see if the server is on
    try:
        clientSocket.settimeout(0.5)
        clientSocket = socket.socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.settimeout(None)
    except:
        return False
    return True

def clientSocket_receive_response(clientSocket):
    try:
        clientSocket.settimeout(0.5)
        message = clientSocket.recv(2048)
        clientSocket.settimeout(None)
    except socket.timeout:
        return ''
    return message.decode()


def main():
    # Prompt users input
    serverName = input('Enter server name or IP address: ')
    serverPort = input('Enter port: ')
    while not serverPort_is_valid(serverPort):
        print('Invalid port number.')
        serverPort = input('Enter port: ')
    serverPort = int(serverPort)
    if not server_is_valid(serverName, serverPort):
        print('Could not connect to server.')
        exit()
    command = input('Enter command: ')
    
    # Build clientsocket and connect
    clientSocket = socket.socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    # Send command and receive command
    clientSocket.send(command.encode())
    message = clientSocket_receive_response(clientSocket)
    if not message:
        print('Did not receive response.')
        exit()
    
    # Store the data in local file
    if command[-1] == '>':
        command = command[:-1]
    elif '>' in command:
        filename = command.split('>')[-1].strip(' ')
    else:
        filename = command.split()[0] + '_cmd.txt'
    
    f = open(filename, 'w')
    f.write(message)
    print('File ', filename, ' successfuly saved')
    
if __name__ == '__main__':
    main()


