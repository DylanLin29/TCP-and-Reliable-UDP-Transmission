import socket
from socket import AF_INET, SOCK_STREAM
from subprocess import Popen, PIPE, STDOUT

def main():
    serverPort = 12345
    serverSocket = socket.socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(2)
    while True:
        connectionSocket, address = serverSocket.accept()
        command = connectionSocket.recv(2048)
        command = command.decode()

        popen = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        output = popen.stdout.read()
        output = output.decode()

        # Store data in local file
        if command[-1] == '>' or '>' not in command:
            if command[-1] == '>':
                command = command[:-1]
            filename = command.split()[0] + '_cmd.txt'
        else:
            filename = command.split('>')[-1].strip(' ')
        
        f = open(filename, 'w')
        f.write(output)

        # Send data back to the client
        with open(filename, 'rb') as f:
            message = f.read()
            connectionSocket.send(message)
        connectionSocket.close()
        print('Successful file transmission.')

        



if __name__ == '__main__':
    main()